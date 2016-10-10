# -*- coding: UTF-8 -*-
from flask import url_for


class CDN(object):
    """Base class for CDN objects."""

    def __init__(self, **kwargs):
        for key, val in kwargs.items():
            setattr(self, key, val)

    def get_resource_url(self):
        """Return resource url for filename."""
        raise NotImplementedError


class LocalCDN(CDN):
    """ A CDN that serves content from the local application. """
    static_endpoint = 'vue.static'

    def get_resource_url(self):
        filename = '{}{}.js'.format(self.name, '.min' if self.use_minified else '')
        return url_for(self.static_endpoint, filename=filename)


class CloudflareCDN(CDN):
    """ Serves files from the Web. """
    baseurl = '//cdnjs.cloudflare.com/ajax/libs/{name}/{version}/{filename}'

    def get_resource_url(self):
        filename = '{}{}.js'.format(self.name, '.min' if self.use_minified else '')
        return self.baseurl.format(name=self.name, version=self.version, filename=filename)


class JsdelivrCDN(CDN):
    """ Serves files from the Web. """
    baseurl = '//cdn.jsdelivr.net/{name}/{version}/{filename}'

    def get_resource_url(self):
        name = self.name.replace('-', '.')
        filename = '{}{}.js'.format(self.name, '.min' if self.use_minified else '')
        return self.baseurl.format(name=name, version=self.version, filename=filename)


cloudflare = CloudflareCDN
jsdelivr = JsdelivrCDN
