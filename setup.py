from setuptools import setup

setup(
    name="Pure Tabix",
    version="1.0.0",
    author="Adam Faulconbridge",
    author_email="afaulconbridge@googlemail.com",
    packages=["puretabix"],
    description="Pure python implementation Tabix reader.",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/afaulconbridge/puretabix",
    install_requires=[],
    extras_require={
        "dev": [
            "pytest-cov",
            "flake8",
            "black",
            "pylint",
            "pip-tools",
            "pipdeptree",
            "pre-commit",
        ],
    },
)