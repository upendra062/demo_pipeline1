from setuptools import setup, find_packages

setup(name="census-income",
      version="0.1",
      author="Rocky Singh Bhadauria",
      author_email="rockybhadauria26@gmail.com",
      packages=find_packages(),
      install_requires=["pandas", "numpy", "flask"]
      )