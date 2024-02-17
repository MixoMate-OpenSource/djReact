# app/management/commands/generate_template.py
import os
import shutil
from sys import stdout
import sys
from django.core.management.base import BaseCommand

from djReact.management.commands import APP_INITIALIZER_CONTENT


class Command(BaseCommand):
    help = "Generates a Django project with React integration"

    def handle(*args, **kwargs):
        project_name = sys.argv[1]

        # Create a new Django project
        os.system(f"django-admin startproject {project_name}")

        # Navigate into the newly created project directory
        os.chdir(project_name)

        # Create a new Django app
        os.system("python manage.py startapp app")

        # Navigate into the newly created app directory
        os.chdir("app")

        # Create a new React app
        os.system("npx create-vite@latest frontend --template react")

        # Navigate into the React app directory
        os.chdir("frontend")
        src_dir = os.path.join(os.getcwd(), "src", "App.jsx")

        while not os.path.exists(src_dir):
            break
        with open(src_dir, "w") as app:
            app.write(APP_INITIALIZER_CONTENT)
        # Copy template files for React

        # Navigate back to the project directory
        os.chdir("..")

        stdout.write(
            f"Successfully created Django project with React integration: {project_name}"
        )
