'''
Created on Nov 24, 2015

@author: tguo
'''


# coding=UTF-8

from url import url

import tornado.web
import os

settings = dict(
    template_path = os.path.join(os.path.dirname(__file__), "templates"),
    static_path = os.path.join(os.path.dirname(__file__), "statics")
    )

application = tornado.web.Application(
    handlers = url,
    **settings
    )