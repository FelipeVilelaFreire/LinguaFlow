from django.core.management.base import BaseCommand

from apps.adventure.seeds.runner import seed_language_sections


class Command(BaseCommand):
    help = "Seed PT -> IT A1 T1 sections"

    def add_arguments(self, parser):
        parser.add_argument("--reset", action="store_true")
        parser.add_argument("--phase", type=int, choices=range(1, 26), metavar="1-25")

    def handle(self, *args, **options):
        phases = [options["phase"]] if options["phase"] else list(range(1, 26))
        total = seed_language_sections(
            self.stdout,
            self.style,
            lang_code="it",
            chapter_slug="it-a1-t1",
            phases=phases,
            reset=options["reset"],
        )
        self.stdout.write(self.style.SUCCESS(f"\nIT section seed complete: {total} created\n"))
