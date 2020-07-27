from setuptools import setup

setup(
    name="boats.py",
    version="0.1.1",
    packages=["discordboats"],
    url="https://discord.boats",
    license="MIT",
    author="Epic",
    author_email="surtla100@gmail.com",
    description="API wrapper for discord.boats",
    long_desciption=open("README.md").read(),
    long_description_content_type="text/markdown",
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent"
    ]
)
