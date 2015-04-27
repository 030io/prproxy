#!/usr/bin/env python
# -*- coding:utf-8 -*-
###===========================###
#  File Name: start.py
#  Author: 030 
#  Site: 030.io 
#  Created Time: 2015/04/27 17:39
###===========================###

import sys
sys.path.insert(0, '../')

from tornado.httpserver import HTTPServer
from tornado.ioloop import IOLoop

from prproxy import app, configs


server = HTTPServer(app)
server.listen(
    port=configs.getint('core', 'port'),
    address=configs.get('core', 'address', fallback='127.0.0.1'),
    )
IOLoop().instance().start()
