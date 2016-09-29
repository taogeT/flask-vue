===============
Flask-Vue
===============
.. image:: https://img.shields.io/pypi/v/Flask-Vue.svg
    :target: https://pypi.python.org/pypi/Flask-Vue/
.. image:: https://img.shields.io/pypi/dm/Flask-Vue.svg
    :target: https://pypi.python.org/pypi/Flask-Vue/
.. image:: https://img.shields.io/pypi/l/Flask-Vue.svg
    :target: https://pypi.python.org/pypi/Flask-Vue
.. image:: https://img.shields.io/pypi/pyversions/Flask-Vue.svg
    :target: https://pypi.python.org/pypi/Flask-Vue/
.. image:: https://img.shields.io/pypi/status/Flask-Vue.svg
    :target: https://pypi.python.org/pypi/Flask-Vue/

Flask-Vue packages `Vue.js
<http://vuejs.org>`_ into an extension. It can also create links to serve Vue
from a CDN and works with no boilerplate code in your application.

Usage
-----

Here is an example::

  from flask_vue import Vue

  [...]

  Vue(app)

  or

  vue = Vue()
  vue.init_app(app)

