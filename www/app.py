import logging; logging.basicConfig(level=logging.INFO)

import asyncio,os,json,time
from datetime import datetime

from aiohttp import web

def index(request):
    return web.Response(body=b'<h1> Awesome </h1>',content_type='text/html')
#       return web.Response(body=u'<h1> Awesome 你好</h1>'.encode(encoding='gbk'),content_type='text/html')


@asyncio.coroutine
def init(loop):
    app = web.Application(loop=loop)
    app.router.add_route('GET','/',index)
    srv = yield from loop.create_server(app.make_handler(), '127.0.0.1', 9000)
    logging.info('server started at http://127.0.0.1:9000...')
    return srv    
# loop = asyncio.get_event_loop()
# loop.run_until_complete(init(loop))
# loop.run_forever()

#test user 
import orm
from models import User,Blog,Comment

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
# loop.close()
# for x in test(loop):
#     pass
destory_pool()
    