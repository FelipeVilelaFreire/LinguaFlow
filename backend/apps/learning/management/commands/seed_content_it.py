from django.core.management.base import BaseCommand

from content.seeds.seed_it_phrases import seed_it_phrases


class Command(BaseCommand):
    help = "Seed Italian (PT→IT) learning content: phrases, lessons and study days."

    def handle(self, *args, **options):
        totals = seed_it_phrases()
        self.stdout.write(
            self.style.SUCCESS(
                f"Italian content seeded: "
                f"{totals['phrases']} phrases, "
                f"{totals['lessons']} lessons, "
                f"{totals['study_days']} study days."
            )
        )
