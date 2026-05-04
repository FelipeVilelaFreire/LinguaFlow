from django.core.management.base import BaseCommand

from content.seeds.seed_german_a1 import seed_german_a1
from content.seeds.seed_scenarios import seed_scenarios


class Command(BaseCommand):
    help = "Populate LinguaFlow with scenarios, phrases, lessons, and study days."

    def handle(self, *args, **options):
        seed_scenarios()
        result = seed_german_a1()
        self.stdout.write(self.style.SUCCESS(f"Seed complete: {result['phrases']} phrases, {result['lessons']} lessons, {result['study_days']} study days."))
