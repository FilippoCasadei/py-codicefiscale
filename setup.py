from setuptools import setup, find_packages

setup(
    name="codicefiscale",
    version="1.0.0",
    description="Libreria per generare e validare codici fiscali italiani",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    author="Filippo Casadei",
    author_email="filippo.casadei2004@gmail.com",
    url="https://github.com/utente/progetto",
    packages=find_packages(exclude=["tests*"]),
    include_package_data=True,
    package_data={"codicefiscale": ["data/*.csv"]},
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.7',
)
