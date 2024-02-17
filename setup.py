from setuptools import setup, find_packages

setup(
    name="djReact",
    version="1.0",
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        "Django>=5.0",
    ],
    entry_points={
        "console_scripts": [
            "djReact = djReact.management.commands.startproject:Command.handle",
        ],
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.10",
)
