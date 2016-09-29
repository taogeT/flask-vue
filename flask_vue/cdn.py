# -*- coding: UTF-8 -*-
from flask import url_for


class CDN(object):
    """Base class for CDN objects."""

    def get_resource_url(self):
        """Return resource url for filename."""
        raise NotImplementedError


class LocalCDN(object):
    """A CDN that serves content from the local application.

    :param static_endpoint: Endpoint to use.
    """

    def __init__(self, static_endpoint='vue.static'):
        self.static_endpoint = static_endpoint

    def get_resource_url(self, filename):
        return url_for(self.static_endpoint, filename=filename)


class CdnjsCDN(object):
    """Serves files from the Web.

    :param baseurl: The baseurl. Filenames are simply appended to this URL.
    """

    def __init__(self):
        self.baseurl = '//cdnjs.cloudflare.com/ajax/libs/{name}/{version}/{filename}'

    def get_resource_url(self, name, version, use_minified=True):
        filename = '{}{}.js'.format(name, '.min' if use_minified else '')
        return self.baseurl.format(name, version, filename)
