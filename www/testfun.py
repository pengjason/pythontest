#!/usr/bin/env python3
# -*- coding: utf-8 -*-
__author__ = 'jason'
'''
async web application.
'''

import logging; logging.basicConfig(level=logging.INFO)

import asyncio,os,json,time
from datetime import datetime

from aiohttp import web
from jinja2 import Environment, FileSystemLoader

from config import configs
#test user 
import orm
from models import User,Blog,Comment
import orm
from coroweb import add_routes, add_static

from handlers import cookie2user, COOKIE_NAME
'''
test
'''
async def test():
#     await orm.create_pool(loop=loop, user='root',password='peng',db='awesome')
    await orm.create_pool(loop=loop, host='127.0.0.1', port=3306, user='root', password='peng',db='awesome')

    
    u = User(name='Test3', email='test3@example.com', passwd='123456',image='about:blank',id='112')
    await u.save()
    
@asyncio.coroutine
def destory_pool():
    global __pool
    if __pool is not None :
        __pool.close()
        yield from __pool.wait_closed()

loop = asyncio.get_event_loop()
loop.run_until_complete(test())
  
destory_pool()
