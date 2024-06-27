  #helps to create ml application as a package
from setuptools import find_namespace_packages,setup
from typing import List

def get_requirements(file_path:str)->List[str]:
    '''
    this function will return the list of requirements

    '''
    requirements=[]
    with open(file_path) as file_obj:
        requirements=file_obj.readlines()
        requirements=[req.replace("\n","") for req in requirements]
        if "-e ." in requirements:
            requirements.remove("-e .")

            
setup(
    name='mlproject',
    version='0.0.1',
    author='Shweta',
    author_email='tripathishweta129@gmail.com',
    packages=find_namespace_packages(),
    #install_requires=['pandas','seaborn','numpy'],
    install_requires=get_requirements('requirements.txt')
)