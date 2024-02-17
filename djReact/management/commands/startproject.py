# myapp/management/commands/generate_template.py
import os
import shutil
from sys import stdout
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = "Generates a Django project with React integration"

    def add_arguments(self, parser):
        parser.add_argument("project_name", type=str, help="Name of the Django project")

    def handle( *args, **kwargs):
        project_name = kwargs["project_name"]

        # Create a new Django project
        os.system(f"django-admin startproject {project_name}")

        # Navigate into the newly created project directory
        os.chdir(project_name)

        # Create a new Django app
        os.system("python manage.py startapp myapp")

        # Navigate into the newly created app directory
        os.chdir("myapp")

        # Create a new React app
        os.system("npx create-react-app frontend")

        # Navigate into the React app directory
        os.chdir("frontend")

        # Copy template files for React
        src_dir = os.path.join(os.getcwd(), "src")
        shutil.rmtree(
            src_dir
        )  # Remove the default src directory created by create-react-app
        os.mkdir(src_dir)

        # Copy template files for React
        templates_dir = os.path.join(
            os.path.dirname(os.path.abspath(__file__)), "templates"
        )
        shutil.copytree(templates_dir, src_dir)

        # Navigate back to the project directory
        os.chdir("..")

        stdout.write(
            
                f"Successfully created Django project with React integration: {project_name}"
        )
