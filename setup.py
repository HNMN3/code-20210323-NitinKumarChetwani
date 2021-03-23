from setuptools import setup

REQUIREMENTS = ['pandas']

CLASSIFIERS = [
    'Programming Language :: Python',
]

# calling the setup function
setup(name='BMI Calculator App',
      version='1.0.0',
      description="An application to calculate BMI scores",
      url='https://github.com/HNMN3/code-20210323-NitinKumarChetwani',
      author='Nitin Kumar Chetwani',
      author_email='hnmn3.nitin@gmail.com',
      classifiers=CLASSIFIERS,
      install_requires=REQUIREMENTS
      )
