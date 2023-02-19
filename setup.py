from setuptools import setup
version = '0.0.1'

with open("README.md", "r") as fi:
    long_description = fi.read()

keywords = ["json", "zip"]

classifiers = [
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3'
    ]

setup(
    name="zipjson",
    packages=["zipjson"],
    version=version,
    description="A tool to create and read compressed JSON files",
    author="Vladimir Guzov",
    author_email="guzov.mail@gmail.com",
    url="https://github.com/vguzov/zipjson",
    keywords=keywords,
    long_description=long_description,
    long_description_content_type='text/markdown',
    install_requires=[],
    classifiers=classifiers
)
