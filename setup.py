from setuptools import find_packages , setup
from typing import List

HYPHEN_E_DOT = '-e.'
def get_requirements(file_path:str)->List[str]:
    '''
    this function will return the requirmenets.
    '''
    requirement = []
    with open("requirement.txt") as file_obj:
        requirement = file_obj.readlines()
        requirement = [req.replace("\n","")for req in requirement]
        if HYPHEN_E_DOT in requirement:
            requirement.remove(HYPHEN_E_DOT)
        return requirement    


setup(
    name='Phishing Website Detection',
    version='0.0.1',
    author='Arjun',
    author_email='kaushikarjun109@gmail.com',
    packages= find_packages(),
    install_requires= get_requirements("requirement.txt")
)