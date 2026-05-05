from django.core.management.base import BaseCommand

from content.seeds.seed_complete_courses import seed_complete_courses


class Command(BaseCommand):
    help = "Seed LinguaFlow complete learning courses."

    def handle(self, *args, **options):
        totals = seed_complete_courses()
        self.stdout.write(
            self.style.SUCCESS(
                f"LinguaFlow complete courses seeded: {totals['phrases']} phrases, {totals['lessons']} lessons, {totals['study_days']} study days."
            )
        )
