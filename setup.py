from setuptools import setup, find_packages
import os

version = '0.1.1.dev0'

setup(name='gites.gdwadmin',
      version=version,
      description="",
      long_description=open("README.txt").read() + "\n" + open(os.path.join("docs", "HISTORY.txt")).read(),
      # Get more strings from http://www.python.org/pypi?%3Aaction=list_classifiers
      classifiers=[
          "Programming Language :: Python",
          "Topic :: Software Development :: Libraries :: Python Modules",
      ],
      keywords='',
      author='',
      author_email='',
      url='',
      license='GPL',
      packages=find_packages(exclude=['ez_setup']),
      namespace_packages=['gites'],
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          'zope.app.testing>=3.5',
          'setuptools',
          'gites.core',
          'affinitic.db',
          'Products.SQLAlchemyDA',
          'collective.js.jqueryui',
          'python-google-places',
          'z3c.table',
      ],
      entry_points={})
