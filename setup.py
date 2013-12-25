from setuptools import setup

from setuptools.command.test import test as TestCommand
import sys

class PyTest(TestCommand):
    def finalize_options(self):
        TestCommand.finalize_options(self)
        self.test_args = []
        self.test_suite = True
    def run_tests(self):
        #import here, cause outside the eggs aren't loaded
        import pytest
        errno = pytest.main(self.test_args)
        sys.exit(errno)

setup(name='flint-md',
	  version='1.1.0',
	  description='Dynamic Markdown Templating',
	  author='Charles Dawson',
	  author_email='charles.dwsn@gmail.com',
	  url='http://cdawson.net/flint',
	  download_url='http://github.com/TheBritKnight/Flint',
	  install_requires=['markdown >= 2.3.1'],
	  tests_require=['pytest'],
	  cmdclass={'test': PyTest},
	  py_modules=['flint'],
	  license="MIT License",
	  classifiers=[
	  	'License :: OSI Approved :: MIT License',
	  	'Programming Language :: Python',
	  	'Programming Language :: Python :: 3',
	  	'Operating System :: OS Independent',
	  	'Topic :: Text Processing :: Markup',
	  	'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
	  	'Intended Audience :: Developers',
	  	'Environment :: Web Environment']
	  )