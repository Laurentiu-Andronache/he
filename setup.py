from os import path

from setuptools import setup, find_packages

here = path.abspath(path.dirname(__file__))

# Get the long description from the README file
with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='he',
    # Versions should comply with PEP 440:
    # https://www.python.org/dev/peps/pep-0440/
    version='2019.03',
    description='A library of Python helpers.',
    long_description=long_description,
    # Denotes that our long_description is in Markdown; valid values are
    # text/plain, text/x-rst, and text/markdown
    #
    # Optional if long_description is written in reStructuredText (rst) but
    # required for plain-text or Markdown
    long_description_content_type='text/markdown',
    url='https://github.com/Laurentiu-Andronache/pe',
    author='Laurențiu Andronache',
    author_email='laurentiu.andronache@trailung.ro',
    # https://pypi.org/classifiers/
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Libraries',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.7',
        'Typing :: Typed',
    ],
    keywords='helpers library common useful functions decorators contexts classes',
    # You can just specify package directories manually here if your project is
    # simple. Or you can use find_packages().
    #
    # Alternatively, if you just want to distribute a single Python file, use
    # the `py_modules` argument instead as follows, which will expect a file
    # called `my_module.py` to exist:
    #
    #   py_modules=["my_module"],
    #
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    package_data={'he': ['data/*.txt']},
    python_requires='>=3.7',
    install_requires=['requests'],
    # List additional groups of dependencies here (e.g. development
    # dependencies). Users will be able to install these using the "extras"
    # syntax, for example:
    #
    #   $ pip install sampleproject[dev]
    #
    # Similar to `install_requires` above, these must be valid existing
    # projects.
    extras_require={
        'dev': ['pre-commit', 'wheel', 'twine', 'tox', 'tox-venv'],
        'tox-manual': [
            'flake8',
            'flake8-bugbear',
            'pylint',
            'pytest-xdist',
            'mypy',
            'check-manifest',
        ],
        'test': ['pytest', 'pytest-cov', 'pytest-sugar', 'pytest-icdiff'],
    },
    # To provide executable scripts, use entry points in preference to the
    # "scripts" keyword. Entry points provide cross-platform support and allow
    # `pip` to create the appropriate form of executable for the target
    # platform.
    #
    # For example, the following would provide a command called `he` which
    # executes the function `main` from this package when invoked:
    entry_points={'console_scripts': ['he=he:main']},  # Optional
    project_urls={
        'Bug Reports': 'https://github.com/Laurentiu-Andronache/he/issues',
        'Say Thanks!': 'https://saythanks.io/to/Laurentiu-Andronache',
        'Source': 'https://github.com/Laurentiu-Andronache/he',
    },
)
