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
<http://vuejs.org>`_ and many extended scripts into an extension.

It can also create links to serve Vue from a CDN and works with no boilerplate code in your application.

-----
Contain Scripts
-----

Scripts List

+---------------+--------+
|vue            | 1.0.26 |
+===============+========+
|vue-async-data | 1.0.2  |
+---------------+--------+
|vue-form       | 0.3.1  |
+---------------+--------+
|vue-i18n       | 4.6.0  |
+---------------+--------+
|vue-resource   | 1.0.3  |
+---------------+--------+
|vue-router     | 0.7.13 |
+---------------+--------+
|vue-validator  | 2.1.7  |
+---------------+--------+
|vuex           | 0.8.2  |
+---------------+--------+

-----
Usage
-----

Here is an example::

  from flask_vue import Vue

  [...]

  Vue(app)

  or

  vue = Vue()
  vue.init_app(app)

