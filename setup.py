from setuptools import setup, find_packages

setup(
	name='project1',
	version='1.0',
	author='Bala Ravi Teja',
	author_email='balaraviteja10@gmail.com',
	packages=find_packages(exclude=('tests', 'docs')),
	setup_requires=['pytest-runner'],
	tests_require=['pytest']	
)
