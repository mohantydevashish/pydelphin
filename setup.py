#!/usr/bin/env python3

import os
from setuptools import setup

base_dir = os.path.dirname(__file__)
about = {}
with open(os.path.join(base_dir, "delphin", "__about__.py")) as f:
    exec(f.read(), about)

with open(os.path.join(base_dir, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

repp_requires = ['regex==2019.11.1']

# thanks: https://snarky.ca/clarifying-pep-518/
doc_requirements = os.path.join(base_dir, 'docs', 'requirements.txt')
if os.path.isfile(doc_requirements):
    with open(doc_requirements) as f:
        docs_require = f.readlines()
else:
    docs_require = []

tests_require = repp_requires + [
    'pytest',
]

setup(
    name=about['__title__'],
    version=about['__version__'],
    description=about['__summary__'],
    long_description=long_description,
    long_description_content_type='text/markdown',
    url=about['__uri__'],
    author=about['__author__'],
    author_email=about['__email__'],
    license=about['__license__'],
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'Intended Audience :: Information Technology',
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Topic :: Scientific/Engineering :: Information Analysis',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Text Processing :: Linguistic',
        'Topic :: Utilities'
    ],
    keywords='nlp semantics hpsg delph-in linguistics',
    packages=[
        'delphin',
        'delphin.codecs',
        'delphin.mrs',
        'delphin.eds',
        'delphin.dmrs',
        'delphin.web',
    ],
    install_requires=[
        'penman==0.9.0',
    ],
    extras_require={
        'docs': docs_require,
        'tests': tests_require,
        'dev': docs_require + tests_require + [
            # https://packaging.python.org/guides/making-a-pypi-friendly-readme
            'setuptools >= 38.6.0',
            'wheel >= 0.31.0',
            'twine >= 1.11.0'
        ],
        'web': ['requests==2.22.0', 'falcon==2.0.0'],
        'repp': repp_requires,
    },
    entry_points={
        'console_scripts': [
            'delphin=delphin.main:main'
        ],
    },
)
