from setuptools import setup, find_packages
import os

version = '0.1'

setup(name='ploomcake.theme_collection_accessibility',
      version=version,
      description="A collection of Ploomcake addictional styles designed for partially sighted people",
      long_description=open("README.txt").read() + "\n" +
                       open(os.path.join("docs", "HISTORY.txt")).read(),
      # Get more strings from
      # http://pypi.python.org/pypi?:action=list_classifiers
      classifiers=[
        "Framework :: Plone",
        "Programming Language :: Python",
        ],
      keywords='',
      author='Maurizio Lupo',
      author_email='maurizio.lupo@redomino.com',
      url='https://github.com/ploomcake/ploomcake.theme_collection_accessibility',
      license='GPL',
      packages=find_packages(exclude=['ez_setup']),
      namespace_packages=['ploomcake'],
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          'setuptools',
          'ploomcake.theme'
          # -*- Extra requirements: -*-
      ],
      entry_points="""
      # -*- Entry points: -*-

      [z3c.autoinclude.plugin]
      target = plone
      """,
#      setup_requires=["PasteScript"],
#      paster_plugins=["ZopeSkel"],
      )
