try:
	from setuptools import setup
except ImportError:
	from distutils.core import setup

config = {
	'description': 'Quick and dirty particle modeling.',
	'author': 'Lukas WinklerPrins',
	'url': '',
	'download_url': '',
	'author_email': 'lukaswinklerprins@protonmail.com',
	'version': '0.1',
	'install_requires': ['nose'],
	'packages': ['sandstorm'],
	'scripts': [],
	'license': 'MIT',
	'name': 'Sandstorm Particle Modeling'
}

setup(**config)
