__author__ = 'Renchen'
from distutils.core import setup

setup(
	name='woeid',
	version='1.0.0',
	author='Renchen Sun',
	author_email='sunrenchen@gmail.com',
	packages=['woeid', 'woeid.test'],
	url='https://github.com/Ray-SunR/woeid',
	license='LICENSE.txt',
	description='A python REST APIs for Yahoo GeoPlanet web services (https://developer.yahoo.com/geo/geoplanet/guide/)',
	long_description=open('README.rst').read(),
	install_requires=['future', 'requests', 'six'],
	keywords=['woeid', 'geoplanet', 'yahoo'],
	package_data={'': ['LICENSE.txt']}
)
