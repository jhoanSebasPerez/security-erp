from django.core.management.base import BaseCommand
from seguridad.populate_db import run

class Command(BaseCommand):
    help = 'Populate the database with initial data'

    def handle(self, *args, **kwargs):
        run()
        self.stdout.write(self.style.SUCCESS('Database populated successfully'))