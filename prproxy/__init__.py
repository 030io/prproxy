#!/usr/bin/env python
# -*- coding:utf-8 -*-
###===========================###
#  File Name: __init__.py
#  Author: 030 
#  Site: 030.io 
#  Created Time: 2015/04/16 21:55
###===========================###

__version__ = '0.0.1'

from tornado.web import Application

try:
#if 1:
    from .handler import handlers, settings
    from .config import configs

    app = Application(handlers=handlers, **settings)
except Exception as e:
    print(e)
