from setuptools import setup

setup(name='flint-md',
	  version='1.0.5',
	  description='Dynamic Markdown Templating',
	  author='Charles Dawson',
	  author_email='charles.dwsn@gmail.com',
	  url='http://cdawson.net/flint',
	  download_url='http://github.com/TheBritKnight/Flint',
	  install_requires=['markdown >= 2.3.1'],
	  py_modules=['flint'],
	  license="MIT License",
	  classifiers=[
	  	'License :: OSI Approved :: MIT License',
	  	'Programming Language :: Python',
	  	'Operating System :: OS Independent']
	  )