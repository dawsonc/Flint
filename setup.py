from distutils.core import setup

setup(name='flint',
	  version='1.0',
	  description='Dynamic Markdown Templating',
	  long_description=open("README.md").read(),
	  author='Charles Dawson',
	  author_email='charles.dwsn@gmail.com',
	  url='http://cdawson.net/flint',
	  download_url='http://github.com/TheBritKnight/Flint',
	  require='markdown',
	  py_modules=['flint'],
	  classifiers=['License :: OSI Approved :: MIT License']
	  )