#!/usr/bin/env python
# -*- coding:utf-8 -*-
###===========================###
#  File Name: handler.py
#  Author: 030 
#  Site: 030.io 
#  Created Time: 2015/04/16 21:57
###===========================###

import chardet
from tornado.web import RequestHandler
from tornado.httpclient import HTTPRequest
from tornado.gen import coroutine
from tornado.httpclient import AsyncHTTPClient, HTTPError


from .config import configs


class ReverseProxy(RequestHandler):
    @coroutine
    def get(self, url):
        if configs.get('host', 'local', fallback=False) \
           and self.request.host != configs.get('host', 'local'):
            self.send_error(400)
            return

        self.request.headers['Host'] = configs.get('host', 'target')
        request = HTTPRequest(
            url='http://'+configs.get('host', 'target')+self.request.uri,
            method=self.request.method,
            headers=self.request.headers,
            #body=self.request.body,
        )
        try:
            ahc = AsyncHTTPClient()
            response = yield ahc.fetch(request)
        except HTTPError as e:
            self.set_status(e.code)
            return
        #except Exception as e:
            #self.send_error(500)
            #return

        if configs.get('host', 'replace', fallback=0) != 0 \
           and response.headers.get('Content-Type', '').startswith('text'):
            encoding = chardet.detect(response.body)['encoding']
            write_ = response.body.decode(encoding, 'ignore').replace(
                    configs.get('host', 'target'),
                    configs.get('host', 'local'),
            ).encode(encoding, 'ignore')
            self.write(write_)
            response.headers['Content-Length'] = len(write_)
        else:
            self.write(response.body)

        for name, value in response.headers.items():
            self.set_header(name, value)



handlers = [
    (r'(.*)', ReverseProxy),
]

settings = {
    'debug' : configs.getint('core', 'debug', fallback=0) != 0,
    'compress_response' : configs.getint('core', 'compress_response', fallback=1) != 0,
}
