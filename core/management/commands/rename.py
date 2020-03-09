import os
from django.core.management.base import BaseCommand
from djangox_project.settings import BASE_DIR


class Command(BaseCommand):
    help = "Renames a Django project"

    def add_arguments(self, parser):
        parser.add_argument(
            "new_project_name", type=str, help="The new Django project name"
        )

    def handle(self, *args, **kwargs):
        new_project_name = kwargs["new_project_name"]

        files_to_rename = [
            os.path.join(BASE_DIR, "djangox_project\settings.py"),
            os.path.join(BASE_DIR, "djangox_project\wsgi.py"),
            os.path.join(BASE_DIR, "manage.py"),
            os.path.join(BASE_DIR, "start.sh"),
        ]
        folder_to_rename = "djangox_projectx"

        for f in files_to_rename:
            with open(f, "r") as file:
                filedata = file.read()

            filedata = filedata.replace("djangox_project", new_project_name)

            with open(f, "w") as file:
                file.write(filedata)

        os.rename(folder_to_rename, new_project_name)

        self.stdout.write(
            self.style.SUCCESS("Project has been renamed to %s" % new_project_name)
        )

