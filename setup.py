from setuptools import setup, find_packages
import sys, os

version = '0.1.0'

setup(name='django-telegram',
      version=version,
      description="A messaging framework that supports email, irc, notify my android and others",
      long_description="""\
""",
      classifiers=[], # Get strings from http://pypi.python.org/pypi?%3Aaction=list_classifiers
      keywords='messaging, push, django',
      author='Kyle Terry',
      author_email='kyle@kyleterry.com',
      url='',
      license='',
      packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          # -*- Extra requirements: -*-
          'django-jsonfield',
      ],
      entry_points="""
      # -*- Entry points: -*-
      """,
      )
