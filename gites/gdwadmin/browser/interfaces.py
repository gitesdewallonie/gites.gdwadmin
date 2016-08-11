# -*- coding: utf-8 -*-

from zope.interface import Interface
from zope.publisher.interfaces.browser import IDefaultBrowserLayer


class IGdwAdminCoreLayer(IDefaultBrowserLayer):
    """
    Layer for all GdwAdmin developments
    """


class ICommuneView(Interface):
    """
    ICommuneView
    """


class ILocaliteView(Interface):
    """
    ICommuneView
    """


class IProvinceView(Interface):
    """
    IProvinceView
    """
