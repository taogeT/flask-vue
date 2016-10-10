# -*- coding: UTF-8 -*-
"""
Flask-Vue
-------------
Flask supports for Vue.js 1.0+ (Python3 version).
"""
try:
    from setuptools import setup
except:
    from distutils.core import setup

import codecs

version = '0.3.4'

setup(
    name='Flask-Vue',
    version=version,
    url='https://github.com/taogeT/flask-vue',
    license='Apache',
    author='Zheng Wentao',
    author_email='zwtzjd@gmail.com',
    description='Vue.js 1.0+ integration for Flask (Python 3 version)',
    long_description=codecs.open('README.rst', 'r', 'utf-8').read(),
    packages=['flask_vue'],
    zip_safe=False,
    include_package_data=True,
    platforms='any',
    install_requires=[
        'Flask>=0.11'
    ],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Web Environment',
        'Framework :: Flask',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Apache Software License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ]
)
