from __future__ import annotations

from importlib import import_module

from django.conf import settings
from django.core.management.base import BaseCommand, CommandError

from apps.adventure.audio import (
    audio_file_path,
    audio_identity,
    iter_voice_targets,
    synthesize_with_piper,
)
from apps.adventure.models import PhaseSection
from apps.adventure.voice_config import configured_voice_rows, piper_model_for


class Command(BaseCommand):
    help = "Generate cached adventure voice files for NPC lines using a local TTS provider."

    def add_arguments(self, parser):
        parser.add_argument("--lang", default="ES", help="Language code, e.g. ES.")
        parser.add_argument("--phase", type=int, default=None, help="Generate only one phase number.")
        parser.add_argument("--provider", default=None, help="Provider: piper or manifest.")
        parser.add_argument("--model", default=None, help="Piper model path (.onnx).")
        parser.add_argument("--piper-exe", default=None, help="Piper executable path.")
        parser.add_argument("--voices", action="store_true", help="List configured character voice env vars.")
        parser.add_argument("--overwrite", action="store_true", help="Regenerate existing files.")
        parser.add_argument("--dry-run", action="store_true", help="Only count/list files; do not generate.")

    def handle(self, *args, **options):
        language_code = options["lang"].upper()
        if options["voices"]:
            self._print_voice_config(language_code)
            return

        provider = (options["provider"] or settings.ADVENTURE_TTS_PROVIDER).lower()
        phase_filter = options["phase"]

        if provider not in {"piper", "manifest"}:
            raise CommandError("Provider must be 'piper' or 'manifest'. Use manifest to only report cache paths.")

        model_override = options["model"]
        piper_exe = options["piper_exe"] or settings.ADVENTURE_TTS_PIPER_EXE

        generated = 0
        skipped = 0
        missing_models = 0
        planned = 0

        phase_numbers = [phase_filter] if phase_filter else range(1, 26)
        for number in phase_numbers:
            module = import_module(f"apps.adventure.seeds.{language_code.lower()}.phases.f{number:02d}")
            for section in module.SECTIONS:
                content = self._section_content(language_code, number, section)
                for target in iter_voice_targets(content):
                    text = target["text"]
                    if not text:
                        continue
                    identity = audio_identity(
                        language_code=language_code,
                        npc=target["npc"],
                        text=text,
                        pace=target["pace"],
                        speech_rate=target["speech_rate"],
                        voice=target["voice"],
                    )
                    output_path = audio_file_path(identity)
                    planned += 1

                    if output_path.exists() and not options["overwrite"]:
                        skipped += 1
                        continue

                    model_path, model_source = piper_model_for(
                        target["npc"],
                        language_code=language_code,
                        override=model_override,
                    )
                    if provider == "piper" and not model_path:
                        missing_models += 1
                        self.stderr.write(
                            f"missing model for npc={target['npc'] or 'narrator'} "
                            f"expected={model_source} output={output_path}"
                        )
                        continue

                    if options["dry_run"] or provider == "manifest":
                        self.stdout.write(f"{output_path}  [{model_source}]")
                        continue

                    synthesize_with_piper(
                        text=text,
                        output_path=output_path,
                        model_path=model_path,
                        piper_exe=piper_exe,
                    )
                    generated += 1

        self.stdout.write(self.style.SUCCESS(
            f"planned={planned} generated={generated} skipped={skipped} missing_models={missing_models}"
        ))

    @staticmethod
    def _section_content(language_code: str, phase_number: int, section: dict):
        row = PhaseSection.objects.filter(
            phase__chapter__language__code=language_code,
            phase__number=phase_number,
            section_number=section["section_number"],
        ).first()
        return row.content if row else section["content"]

    def _print_voice_config(self, language_code: str):
        rows = configured_voice_rows(language_code)
        if not rows:
            self.stdout.write("No character voice config for this language yet.")
            return

        self.stdout.write("Character voice model env vars:")
        for row in rows:
            status = row["model"] or "(not set)"
            self.stdout.write(f"- {row['name']} [{row['key']}]: {row['env']} = {status}")
            self.stdout.write(f"  {row['description']}")
        default_model = settings.ADVENTURE_TTS_PIPER_DEFAULT_MODEL or "(not set)"
        self.stdout.write(f"- Fallback: ADVENTURE_TTS_PIPER_DEFAULT_MODEL = {default_model}")
