from setuptools import find_packages, setup

# py -m build
# twine upload dist/*
VERSION = "0.0.2"
DESCRIPTION = "A helper library for pygame applications"
LONG_DESCRIPTION = """
A helper library for pygame applications 
that includes common utilies such as cached font loading,
particle systems, entity and tilemap management etc.
"""

# Setup
setup(
    name="pglib",
    version=VERSION,
    author="Disa, Axis, Snek",
    email="blankRiot96@gmail.com",
    description=DESCRIPTION,
    long_description=LONG_DESCRIPTION,
    packages=find_packages(),
    install_requires=["pygame", "pytmx"],
    python_requires=">=3.10",
    keywords=["pygame", "helper library"],
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Topic :: Software Development :: Libraries :: pygame",
    ],
)
