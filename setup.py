
from setuptools import setup,find_packages

setup (
    name= "Libardo_Delavega",
    version= "0.0.1",
    author= "Libardo_Delavega",
    author_email= "libardo.delavega@est.iudigital.edu.co",
    description= "",
    py_modules= ["actividad_1"],
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
