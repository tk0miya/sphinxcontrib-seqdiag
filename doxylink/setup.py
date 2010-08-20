# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

with open('README.rst') as stream:
    long_desc = stream.read()

requires = ['Sphinx>=0.6', 'pyparsing']

setup(
    name='sphinxcontrib-doxylink',
    version='0.4',
	url='http://packages.python.org/sphinxcontrib-doxylink',
    download_url='http://pypi.python.org/pypi/sphinxcontrib-doxylink',
    license='BSD',
    author='Matt Williams',
    author_email='matt@milliams.com',
    description='Sphinx extension doxylink',
    long_description=long_desc,
    keywords=['sphinx','doxygen','documentation','c++'],
    zip_safe=False,
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Console',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Documentation',
        'Topic :: Utilities',
    ],
    platforms='any',
    packages=find_packages(),
    include_package_data=True,
    install_requires=requires,
    namespace_packages=['sphinxcontrib'],
)
