from setuptools import setup, find_packages

setup(
	name='data_analysis',
	version='0.0.1',
	url='www.github.com/tprinkki/data_analysis',
	license='BSD',
	author='Ty Prinkki',
	packages=find_packages(),
	install_requires=['PyQt5', 
					  'pandas', 
					  'SQLAlchemy',
					  'nltk',
					  'numpy',
					  'jupyter',
					  'python-twitter'],
	entry_points={},
	extras_require={'dev': ['flake8',]},
	)
