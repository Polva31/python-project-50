from setuptools import setup, find_packages

setup(
    name="hexlet-code",
    version="0.1.0",
    packages=find_packages(),
    include_package_data=True,
    install_requires=["pyyaml>=6.0"],
    entry_points={
        "console_scripts": [
            "gendiff = gendiff.cli:main",
        ],
    },
)
