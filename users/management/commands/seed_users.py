
from django.core.management.base import BaseCommand
from users.models import User
from django_seed import Seed

NAME = {"users"}


class Command(BaseCommand):

    help = f"This command creates {NAME}"

    def add_arguments(self, parser):
        parser.add_argument(
            '--numbers', help="How many {NAME} do you want me to create?")

    def handle(self, *args, **options):

        number = options.get("number")

        seeder = Seed.seeder()
        seeder.add_entity(
            User, number, {"is_staff": False, "is_superuser": False})
        seeder.execute()
        self.stdout.write(self.style.SUCCESS(f"{NAME} created!"))
