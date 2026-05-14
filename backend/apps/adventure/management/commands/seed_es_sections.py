from django.core.management.base import BaseCommand

from apps.adventure.seeds.runner import seed_language_sections


class Command(BaseCommand):
    help = "Seed das secoes ES A1 T1 em lote"

    def add_arguments(self, parser):
        parser.add_argument(
            "--reset",
            action="store_true",
            help="Apaga e recria as secoes existentes",
        )
        parser.add_argument(
            "--phase",
            type=int,
            choices=range(1, 26),
            metavar="1-25",
            help="Roda somente uma fase especifica",
        )

    def handle(self, *args, **options):
        phases = [options["phase"]] if options["phase"] else list(range(1, 26))

        self.stdout.write("\nSeed secoes ES A1 T1\n")
        total = seed_language_sections(
            self.stdout,
            self.style,
            lang_code="es",
            chapter_slug="es-a1-t1",
            phases=phases,
            reset=options["reset"],
        )
        self.stdout.write(self.style.SUCCESS(f"\nSeed de secoes concluido: {total} criadas\n"))
