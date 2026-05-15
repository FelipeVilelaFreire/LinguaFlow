from django.core.management.base import BaseCommand

from apps.adventure.seeds.runner import seed_language_sections


DE_SECTION_STEP_TARGETS = {
    "narrativa": 8,
    "revisao_srs": 12,
    "pratica_aplicada": 13,
    "gramatica_narrativa": 10,
    "reforco": 11,
    "obstaculo": 13,
}


class Command(BaseCommand):
    help = "Seed EN -> DE A1 T1 sections"

    def add_arguments(self, parser):
        parser.add_argument(
            "--reset",
            action="store_true",
            help="Delete and recreate existing sections",
        )
        parser.add_argument(
            "--phase",
            type=int,
            choices=range(1, 26),
            metavar="1-25",
            help="Run only one phase",
        )

    def handle(self, *args, **options):
        phases = [options["phase"]] if options["phase"] else list(range(1, 26))

        self.stdout.write("\nSeed sections EN -> DE A1 T1\n")
        total = seed_language_sections(
            self.stdout,
            self.style,
            lang_code="de",
            chapter_slug="de-a1-t1",
            phases=phases,
            reset=options["reset"],
            step_targets=DE_SECTION_STEP_TARGETS,
        )
        self.stdout.write(self.style.SUCCESS(f"\nDE section seed complete: {total} created\n"))
