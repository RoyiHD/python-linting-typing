"""
Manage project packages and metadata
"""

from setuptools import find_packages, setup # type: ignore

setup(
    name = "Python Linting",
    description = "Linting setup for python applications",
    version = "0.0.1",
    packages = find_packages(exclude=["*.tests"]),
    include_packages_data = True,
    install_requires = [
        "Flask==3.0.0",
        "mypy==1.6.1",
        "pydantic==2.4.2",
        "pylint==3.0.0"
    ]
)
