from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()

REPO_NAME = "Books Recommendation System"
AUTHOR_USER_NAME = "ANH TRUONG"
SRC_REPO = "Book_Recommendation"
LIST_OF_REQUIREMENTS = []

setup(
    name=SRC_REPO,
    version="0.0.1",
    author="ANH TRUONG",
    description="Test for a recommendation system",
    long_description=long_description,
    url="https://github.com/anhtruong2307/Book_Recommendation",
    author_email="anhtruong23072004@gmail.com",
    packages=find_packages(),
    python_requires=">=3.10",
    install_requires=LIST_OF_REQUIREMENTS
)