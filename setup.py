from setuptools import setup, find_packages

setup(
    name="djReact",
    version="2.1",
    packages=find_packages(),
    include_package_data=True,
    long_description_content_type="text/markdown",
    install_requires=["Django>=3.0"],
    entry_points={
        "console_scripts": [
            "djReact = djReact.management.commands.startproject:Command.handle",
        ],
    },
    data_files=[("data", ["djReact/frontend/frontend.zip","README.md", "README.md"])],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.10",
)
