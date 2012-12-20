import os
from setuptools import setup


def read(fname):
	return open(os.path.join(os.path.dirname(__file__), fname)).read()
	
setup(
	name="Python-wrapper",
	version="0.8.0",
	author="Maxime Santerre",
	author_email="msanterre@lymbix.com",
	description="A wrapper for the Lymbix API that allows you to easily use the service's methods",
	license="MIT",
	keywords="lymbix api sentiment analysis",
	url="https://github.com/lymbix/Python-wrapper",
	long_description=read("README"),
	py_modules=['lymbix'],
	classifiers=[
		"Development Status :: 4 - Beta",
		"Natural Language :: English",
		"Operating System :: OS Independent",
		"Topic :: Scientific/Engineering :: Information Analysis"
	]
)
