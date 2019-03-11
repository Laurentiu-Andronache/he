.. he documentation master file, created by
   sphinx-quickstart on Sun Mar 10 15:53:56 2019.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Welcome to he's documentation!
==============================

+------------------------------------------------+----------------------------------------------------------+
|.. image:: _static/he.svg                       | License: `MIT`                                           |
|   :alt: he - a library of Python helpers!      |                                                          |
|   :align: left                                 | Requires: `Python 3.7 or higher`                         |
|                                                |                                                          |
|                                                | Repository: https://github.com/Laurentiu-Andronache/he   |
+------------------------------------------------+----------------------------------------------------------+

------

`he` is a library of Python helpers

It exists to aid Python developers in not reinventing the wheel.

Explore the available functions in the **Contents** section, by choosing the modules that interest you.

Install it with: `pip install he`

Example usage, where :func:`pprint.pprint` from the standard library is also needed::

   >>> from he.http_tools import get_json_parsed_from

   >>> parsed = get_json_parsed_from('https://www.reddit.com/user/spez/moderated_subreddits.json')

   >>> from pprint import pprint

   >>> pprint(parsed)
   {'data': [{'banner_img': '',
           'banner_size': None,
   ...

All functions are well documented, typed and use telling parameter names. Example:

.. autofunction:: he.http_tools.get_json_parsed_from

------


.. toctree::
   :maxdepth: 2
   :caption: Contents:

   he


Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
