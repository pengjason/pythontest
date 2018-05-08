import logging; logging.basicConfig(level=logging.INFO)

import asyncio,os,json,time
from datetime import datetime

from aiohttp import web
from jinja2.loaders import FileSystemLoader,Environment
from coroweb import add_routes, add_static
def init_jinja2(app,**kw):
    logging.info('init jinja2')
    options = dict(
        autoescape = kw.get('autoescape',True),
        block_start_string = kw.get('block_start_string','{%'),
        block_end_string = kw.get('block_end_string','%}'),
        variable_start_string = kw.get('variable_start_string','{{'),
        variable_end_string = kw.get('variable_end_string','}}'),
         auto_reload = kw.get('auto_reload',True)                          
    )
    path = kw.get('path',None)
    if path is None:
        path = os.path.join(os.path.dirname(os.path.abspath(__file__)),'templates')
    logging.info('set jinja2 template path: %s' % path)
    env = Enviroment(loader=FileSystemLoader(path),**options)
    filters = kw.get('filters',None)
    if filters is not None:
        for name, f in filters.items():
            env.filters[name] = f
    app['__templating__'] = env
    
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
    