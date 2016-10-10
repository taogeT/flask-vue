# -*- coding: UTF-8 -*-
from flask import current_app, Blueprint

from . import cdn
from .cdn import LocalCDN, CDN
from .config import VUE_CONFIGURATION


def vue_find_resource(name, use_minified=None):
    """Resource finding function, also available in templates.

    :param name: Script to find a URL for.
    :param use_minified': If set to True/False, use/don't use minified.
                          If None, honors VUE_USE_MINIFIED.
    :return: A URL.
    """
    target = list(filter(lambda x: x['name'] == name, current_app.config['VUE_CONFIGURATION']))
    if not target:
        raise ValueError('Can not find resource from configuration.')
    target = target[0]
    use_minified = (isinstance(use_minified, bool) and use_minified) or current_app.config['VUE_USE_MINIFIED']
    CdnClass = LocalCDN if target['use_local'] else getattr(cdn, target['cdn'], CDN)
    resource_url = CdnClass(name=name, version=target.get('version', ''),
                            use_minified=use_minified).get_resource_url()
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
        app.config.setdefault('VUE_CONFIGURATION', None)

        real_vue_config = [dict(x, use_local=app.config['VUE_SERVE_LOCAL']) for x in VUE_CONFIGURATION]
        if isinstance(app.config['VUE_CONFIGURATION'], list):
            while len(app.config['VUE_CONFIGURATION']) > 0:
                selfconfig = app.config['VUE_CONFIGURATION'].pop()
                for vueconfig in real_vue_config:
                    if selfconfig['name'] == vueconfig['name']:
                        for key, val in selfconfig.items():
                            vueconfig[key] = val
                        break
                else:
                    real_vue_config.append(selfconfig)
        app.config['VUE_CONFIGURATION'] = real_vue_config

        blueprint = Blueprint('vue', __name__, template_folder='templates',
                              static_folder='static', static_url_path=app.static_url_path + '/vue',
                              subdomain=app.config['VUE_LOCAL_SUBDOMAIN'])
        app.register_blueprint(blueprint)

        app.jinja_env.globals['vue_find_resource'] = vue_find_resource
