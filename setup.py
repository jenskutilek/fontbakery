# coding: utf-8
# Copyright 2017 The Font Bakery Authors. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
# See AUTHORS.txt for the list of Authors and LICENSE.txt for the License.
import os
from setuptools import setup


setup(
    name="fontbakery",
    use_scm_version=True,
    url='https://github.com/googlefonts/fontbakery/',
    description='Font Bakery is a set of command-line tools'
                ' for ensuring the quality of font projects.',
    author='Font Bakery Authors: Dave Crossland, Felipe Sanches, Lasse Fister, Marc Foley, Vitaly Volkov',
    author_email='dave@lab6.com',
    package_dir={'': 'Lib'},
    packages=['fontbakery',
              'fontbakery.reporters',
              'fontbakery.specifications',
              'fontbakery.commands'
              ],
    package_data={'fontbakery': ['data/*.cache']},
    classifiers=[
        'Environment :: Console',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Apache Software License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7'
    ],
    setup_requires=['setuptools_scm'],
    install_requires=[
        'lxml',
        'defusedxml',
        'requests',
        'unidecode',
        'protobuf',
        'bs4',
        'fontTools',
        'font-v',
        'defcon',
        'ufolint',
        'future',
    ],
    entry_points={
        'console_scripts': ['fontbakery=fontbakery.cli:main'],
    }
)


# check for ttfautohint
found_ttfautohint = False
for p in os.environ.get('PATH').split(':'):
    if os.path.exists(os.path.join(p, 'ttfautohint')):
        found_ttfautohint = True

if not found_ttfautohint:
    print('WARNING: Command line tool `ttfautohint` is recommended. Install it with'
           ' `apt-get install ttfautohint` or `brew install ttfautohint`')
