try:
  from setuptools import setup
except ImportError:
  from distutils.core import setup

config = {
  'description': 'my project',
  'author': 'roberto santos',
  'url': '',
  'download_url': '',
  'author_email': 'py5gol@gmail.com',
  'version': '0.1',
  'install_requires': ['nose'],
  'packages': ['NAME'],
  'scripts': [],
  'name': 'projectname'
}

setup(**config)

