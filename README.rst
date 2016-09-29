===============
Flask-Vue
===============

.. image:: https://travis-ci.org/mbr/flask-vue.png?branch=master
   :target: https://travis-ci.org/mbr/flask-vue

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

