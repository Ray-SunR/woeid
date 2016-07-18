__author__ = 'Renchen'
from distutils.core import setup

setup(
    name='woeid',
    version='0.1.4',
    author='Renchen Sun',
    author_email='sunrenchen@gmail.com',
    packages=['woeid', 'woeid.test'],
    url='https://github.com/Ray-SunR/woeid',
    download_url="https://github.com/Ray-SunR/woeid/archive/0.1.zip",
    license='LICENSE.txt',
    description='A python REST apis for getting Yahoo GeoPlanet web services (https://developer.yahoo.com/geo/geoplanet/guide/)',
    long_description=open('README.md').read(),
    keywords=['woeid', 'geoplanet', 'yahoo'],
    package_data={'': ['LICENSE.txt']}
)
