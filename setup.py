from setuptools import setup,find_packages
from typing import List ## All the datatype coming from typing module
""" Importing the pckage vaiables """

PROJECT_NAME = "Nuverlan Housing Predictor"
VERSION="0.0.2"
AUTHOR="kavi arasu"
DESCRIPTION="FSDS End To End Project Developement."
PACKAGES=["housing"]
REQUIREMENT_FILE_NAME = "requirements.txt"


def getRequirementList()->List[str]:
    """
    Description : This function is going to return the list of packages from requirements.txt file
    """
    with open(REQUIREMENT_FILE_NAME) as requirement_file:
        return requirement_file.readlines().remove("-e .")

setup(version=VERSION,
name=PROJECT_NAME,
author=AUTHOR,
description=DESCRIPTION,
#packages=PACKAGES, # Package 
packages=find_packages(), # (OR)   packages=PACKAGES
install_requires=getRequirementList() # Install requires for installing the package mentioned in requirement.txt file
)


if __name__ == "__main__":
    print(getRequirementList())