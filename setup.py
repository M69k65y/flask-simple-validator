from setuptools import setup


setup(
	name = "flask-simple-validator",
	version = "1.0",
	description = "A simple JSON validator for use in Python projects. (Built in Python 3)",
	url = "https://github.com/M69k65y/json-simple-validator",
	author = "M69k65y",
	license = "MIT",
	packages = ["json-simple-validator"],
	zip_safe=False,
	install_requires = [
		"phonenumbers"
	],
	classifiers = [
		"Development Status :: 3 - Alpha",
		"Framework :: Flask",
		"License :: OSI Approved :: MIT License",
		"Programming Language :: Python :: 3"
	],
	keywords = "flask json validation validator"
)