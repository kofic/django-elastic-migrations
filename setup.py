#!/usr/bin/env python
# -*- coding: utf-8 -*-
# pylint: disable=C0111,W6005,W6100
from __future__ import absolute_import, print_function

import os
import re
import sys

from setuptools import setup


def get_version(*file_paths):
    """
    Extract the version string from the file at the given relative path fragments.
    """
    filename = os.path.join(os.path.dirname(__file__), *file_paths)
    version_file = open(filename).read()
    version_match = re.search(r"^__version__ = ['\"]([^'\"]*)['\"]",
                              version_file, re.M)
    if version_match:
        return version_match.group(1)
    raise RuntimeError('Unable to find version string.')


VERSION = get_version('django_elastic_migrations', '__init__.py')

# usage: python setup.py tag pushes a new version tag
# if sys.argv[-1] == 'tag':
#     print("Tagging the version on github:")
#     os.system("git tag -a %s -m 'version %s'" % (VERSION, VERSION))
#     os.system("git push origin %s" % VERSION)
#     sys.exit()

README = open(os.path.join(os.path.dirname(__file__), 'README.md')).read()
CHANGELOG = open(os.path.join(os.path.dirname(__file__), 'CHANGELOG.md')).read()

setup(
    name='django-elastic-migrations',
    version=VERSION,
    description="""Migrate Elasticsearch Schemas in Django""",
    long_description=README + '\n\n' + CHANGELOG,
    author='Harvard Business School, HBX Department',
    author_email='dschroeder@hbs.edu',
    url='https://stash.hbxcloud.com/users/pnore/repos/django-elastic-migrations/browse',
    packages=[
        'django_elastic_migrations',
    ],
    include_package_data=True,
    install_requires=[
        "Django>=1.8,<2.1", "django-model-utils>=2.0", "elasticsearch-dsl>=6.0.0", "texttable>=1.2.1"
    ],
    zip_safe=False,
    keywords='Django Elasticsearch',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Framework :: Django',
        'Framework :: Django :: 1.8',
        'Framework :: Django :: 1.11',
        'Framework :: Django :: 2.0',
        'Intended Audience :: Developers',
        'License :: Other/Proprietary License',
        'Natural Language :: English',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
    ],
)
