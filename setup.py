from setuptools import find_packages, setup
from typing import List

HYPEN_E_DOT = "-e ."  # You need to define this variable.

def get_requirements(file_path: str) -> List[str]:
    requirements = []
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.replace("\n", "") for req in requirements]

        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)
    return requirements

setup(
    name="xray",
    version="0.0.1",
    author="Prasad Kharche",  # Corrected typo from 'auther' to 'author'
    author_email="prasadkharche02@gmail.com",
    install_requires=get_requirements("requirements.txt"),  # Path to the requirements file
    packages=find_packages()
)
