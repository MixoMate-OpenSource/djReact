# app/management/commands/generate_template.py
import os
import shutil
from sys import stdout
import sys
from django.core.management.base import BaseCommand
from .build_dir.file_content import (
    get_manage_py_file_content,
    get_asgi_file_content,
    get_wsgi_file_content,
    get_djReact_content,
    get_default_urls_content,
)
from djReact.management.commands import APP_INITIALIZER_CONTENT
import shutil
import djReact.frontend


class Command(BaseCommand):
    help = "Generates a Django project with React integration"

    def handle(*args, **kwargs):
        project_name = sys.argv[1]
        frontend_path = djReact.frontend.__path__[0] + "/frontend.zip"
        # exit()
        # Create a new Django project
        os.system(f"django-admin startproject {project_name}")

        # Navigate into the newly created project directory
        os.chdir(project_name)

        proj_dir = os.path.abspath(os.path.curdir)
        main_app_dir = os.path.join(proj_dir, project_name)

        asgi_file_pth = os.path.join(main_app_dir, "asgi.py")
        with open(asgi_file_pth, "w") as app:
            app.write(get_asgi_file_content(project_name))

        wsgi_file_pth = os.path.join(main_app_dir, "wsgi.py")
        with open(wsgi_file_pth, "w") as app:
            app.write(get_wsgi_file_content(project_name))

        dj_react_file_pth = os.path.join(main_app_dir, "djReact.py")
        with open(dj_react_file_pth, "w") as app:
            app.write(get_djReact_content(project_name))

        manage_py_content = os.path.join(proj_dir, "manage.py")
        with open(manage_py_content, "w") as app:
            app.write(get_manage_py_file_content(project_name))

        main_urls_file_path = os.path.join(main_app_dir, "urls.py")
        with open(main_urls_file_path, "w") as app:
            app.write(get_default_urls_content(project_name))
        # Create a new Django app
        # os.system("django-admin startapp webapp")

        # Navigate into the newly created app directory
        # os.chdir("webapp")

        # Create a new React app
        # os.system("npx create-vite@latest frontend --template react")

        # os.chdir("frontend")
        shutil.unpack_archive(frontend_path, os.curdir)
        os.chdir("frontend")
        # Copy template files for React
        os.system("npm install")
        os.system("npm install autoprefixer")
        os.system("npm run build")
        # Navigate back to the project directory
        os.chdir("..")

        with open(os.path.join(proj_dir, "requirements.txt"), "w") as app:
            app.write("\ndjango\ndjango-spa\nwhitenoise")

        stdout.write(
            f"\nSuccessfully created Django project with React integration: {project_name}"
        )
        stdout.write(f"\nrun below command in your virtual env:")
        stdout.write(f"\npython manage.py runserver")
