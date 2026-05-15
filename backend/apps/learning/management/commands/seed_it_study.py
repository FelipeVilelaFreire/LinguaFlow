from django.core.management.base import BaseCommand

from apps.adventure.seeds.it.content import CHAPTER, PHASES, PHRASES, SCENARIOS, SOURCE_LANGUAGE, TARGET_LANGUAGE
from apps.learning.seeds.study import seed_study_from_adventure


class Command(BaseCommand):
    help = "Seed study modules, scenarios and canonical days for IT A1"

    def handle(self, *args, **options):
        self.stdout.write("\nSeed study PT -> IT A1 T1\n")
        stats = seed_study_from_adventure(
            stdout=self.stdout,
            source_language=SOURCE_LANGUAGE,
            target_language=TARGET_LANGUAGE,
            chapter=CHAPTER,
            scenarios=SCENARIOS,
            phrases=PHRASES,
            phases=PHASES,
        )
        self.stdout.write(self.style.SUCCESS(
            f"\nDone. IT study seed complete: {stats['days']} canonical days.\n"
        ))
