from setuptools import setup, find_packages

with open("README.md", "r") as f:
    description = f.read()

setup(
    name="djReact",
    version="2.1.2",
    packages=find_packages(),
    include_package_data=True,
    install_requires=["Django>=3.0"],
    entry_points={
        "console_scripts": [
            "djReact = djReact.management.commands.startproject:Command.handle",
        ],
    },
    data_files=[("data", ["djReact/frontend/frontend.zip"])],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.10",
    long_description=description,
    long_description_content_type="text/markdown",
)

