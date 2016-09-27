# -*- coding: UTF-8 -*-
from flask import current_app, Blueprint

from .cdn import StaticCDN, WebCDN, ConditionalCDN

VUE_VERSION = '1.0.26'
VUE_RESOURCE_VERSION = '1.0.3'


def vue_find_resource(filename, cdn, use_minified=None):
    """Resource finding function, also available in templates.

    :param filename: File to find a URL for.
    :param cdn: Name of the CDN to use.
    :param use_minified': If set to True/False, use/don't use minified.
                          If None, honors VUE_USE_MINIFIED.
    :return: A URL.
    """
    if (isinstance(use_minified, bool) and use_minified) or current_app.config['VUE_USE_MINIFIED']:
        filename = '%s.min.%s' % tuple(filename.rsplit('.', 1))
    resource_url = current_app.extensions['vue']['cdns'][cdn].get_resource_url(filename)

    if resource_url.startswith('//') and current_app.config['VUE_CDN_FORCE_SSL']:
        resource_url = 'https:%s' % resource_url

    return resource_url


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

        vue_cdn = WebCDN('//cdnjs.cloudflare.com/ajax/libs/vue/%s/'.format(VUE_VERSION))
        vue_resource_cdn = WebCDN('//cdnjs.cloudflare.com/ajax/libs/vue-resource/%s/'.format(VUE_RESOURCE_VERSION))
        local = StaticCDN('vue.static')
        app.extensions['vue'] = {
            'cdns': {
                'local': local,
                'static': StaticCDN(),
                'vue': ConditionalCDN('VUE_SERVE_LOCAL', local, vue_cdn),
                'vue-resource': ConditionalCDN('VUE_SERVE_LOCAL', local, vue_resource_cdn)
            }
        }
