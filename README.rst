===============
Flask-Vue
===============
.. image:: https://img.shields.io/pypi/v/Flask-Vue.svg
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

+===============+========+
|vue            | 1.0.26 |
+---------------+--------+
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
|vue-table      | 1.5.3  |
+---------------+--------+

-----
Usage
-----

Here is an example on init Vue::

  from flask_vue import Vue

  [...]

  Vue(app)

  or

  vue = Vue()
  vue.init_app(app)

-----
Configuration
-----
There are configuration options used by Flask-Vue.

+--------------------+------------------+--------------------------------------------------------------------+
|Option              | Default          |                                                                    |
+====================+==================+====================================================================+
|VUE_USE_MINIFIED    | True             |Whether or not to use the minified scripts.                         |
+--------------------+------------------+--------------------------------------------------------------------+
|VUE_SERVE_LOCAL     | False            |If True, scripts will be served from the local instance.            |
+--------------------+------------------+--------------------------------------------------------------------+
|VUE_LOCAL_SUBDOMAIN | None             |Passes a subdomain parameter to the generated Blueprint.            |
|                    |                  |Useful when serving assets locally from a different subdomain.      |
+--------------------+------------------+--------------------------------------------------------------------+
|VUE_CDN_FORCE_SSL   | True             |If a CDN resource url starts with //, prepend 'https:' to it.       |
+--------------------+------------------+--------------------------------------------------------------------+
|VUE_CONFIGURATION   | flask_vue.config |Individualized setting about each script.                           |
|                    |                  |It supports to config CDN scripts which do not have local instance. |
+--------------------+------------------+--------------------------------------------------------------------+
