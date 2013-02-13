# -*- coding: utf-8 -*-

import json

from Products.Five.browser import BrowserView


class MapBlacklist(BrowserView):
    """
    Map blacklist view
    """

    def __call__(self):
        return json.dumps(['hello', 'world'])
