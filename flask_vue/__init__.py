# -*- coding: UTF-8 -*-
from flask import current_app, Blueprint
from jinja2 import Markup

from .cdn import LocalCDN, CdnjsCDN, CDN
from .resource import plugins

import os


def vue_find_resource(pluginname, use_minified=None):
    """Resource finding function, also available in templates.

    :param pluginname: Plugin to find a URL for.
    :param use_minified': If set to True/False, use/don't use minified.
                          If None, honors VUE_USE_MINIFIED.
    :return: A URL.
    """
    pluginf = list(filter(lambda x: x['name'] == pluginname, plugins))
    return _get_resource_url(pluginf[0], use_minified=use_minified,
                             use_local=current_app.config['VUE_SERVE_LOCAL'])


def _get_resource_url(plugin, use_local=None, use_minified=None):
    islocal = (isinstance(use_local, bool) and use_local) or current_app.config['VUE_SERVE_LOCAL']
    ismin = (isinstance(use_minified, bool) and use_minified) or current_app.config['VUE_USE_MINIFIED']
    if islocal:
        filename = os.path.join(plugin['local'], '{}{}.js'.format(plugin['name'], '.min' if ismin else ''))
        lcdn = LocalCDN(static_endpoint='static') if plugin['cdn'] == 'static' else LocalCDN()
        resource_url = lcdn.get_resource_url(filename)
    elif plugin['cdn'] == 'cdnjs':
        resource_url = CdnjsCDN().get_resource_url(plugin['name'], plugin['version'], use_minified=ismin)
    else:
        resource_url = CDN().get_resource_url()
    if resource_url.startswith('//') and current_app.config['VUE_CDN_FORCE_SSL']:
        resource_url = 'https:%s' % resource_url
    return resource_url


class _Vue(object):

    def __init__(self):
        for eplugin in plugins:
            setattr(self, 'include_{}'.format(eplugin['name'].replace('-', '_')), self._include_plugin(eplugin))

    def _include_plugin(self, eplugin):
        def _inner_wrapper(use_local=None, use_minified=None):
            resource_url = _get_resource_url(eplugin, use_local=use_local, use_minified=use_minified)
            return Markup('<script src="{}"></script>\n'.format(resource_url))
        return _inner_wrapper


class Vue(object):
    def __init__(self, app=None):
        if app is not None:
            self.init_app(app)

    def init_app(self, app):
        app.config.setdefault('VUE_USE_MINIFIED', True)
        app.config.setdefault('VUE_CDN_FORCE_SSL', False)
        app.config.setdefault('VUE_SERVE_LOCAL', False)
        app.config.setdefault('VUE_LOCAL_SUBDOMAIN', None)

        blueprint = Blueprint('vue', __name__, template_folder='templates',
                              static_folder='static', static_url_path=app.static_url_path + '/vue',
                              subdomain=app.config['VUE_LOCAL_SUBDOMAIN'])
        app.register_blueprint(blueprint)

        app.jinja_env.globals['vue_find_resource'] = vue_find_resource
        if not hasattr(app, 'extensions'):
            app.extensions = {}
        app.extensions['vue'] = _Vue()

        def context_processor():
            return {
                'vue': current_app.extensions['vue']
            }
        app.context_processor(context_processor)
