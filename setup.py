import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

name = "teIethon"
version = "1.1"
author = "sppidy"
author_email = "sppidytg@gmail.com"
description = "A Powerful Python-Telethon Based Library For Spidy's Bots."
license = "GNU AFFERO GENERAL PUBLIC LICENSE (v3)"
url = "https://github.com/sppidy"

setuptools.setup(
    name=name,
    version=version,
    author=author,
    author_email=author_email,
    description=description,
    long_description=long_description,
    long_description_content_type="text/markdown",
    url=url,
    license=license,
    packages=setuptools.find_packages(),
    install_requires=[
    	"utilsrobot",
        "telethon==1.19.5",
        "cryptg",
        "python-dotenv==0.15.0",
        "redshift-sqlalchemy",
        "SQLAlchemy==1.3.0",
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)
