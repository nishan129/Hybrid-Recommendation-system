from setuptools import setup, find_packages

with open("requirements.txt") as f:
    requirements = f.read().splitlines()
    
setup(
    name= "Hybrid Recomndation System",
    version="0.1",
    author= "Nishant Borkar",
    packages=find_packages(),
    install_requires = requirements
)