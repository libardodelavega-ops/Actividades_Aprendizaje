
from setuptools import setup,find_packages

setup (
    name= "nini_guitierrez",
    version= "0.0.1",
    author= "Nini gutierrez",
    author_email= "nini.gutierrez@est.iudigital.edu.co",
    description= "",
    py_modules= ["actividad_1 y 2"],
    install_requires= [
       "kagglehub[pandas-datasets]>=0.3.8",
        "matplotlib>=3.5.0",
        "seaborn>=0.11.2",
        "pandas",
        "numpy",
        "matplotlib",
        "openpyxl",
        "requests"
 
 ]
 )
