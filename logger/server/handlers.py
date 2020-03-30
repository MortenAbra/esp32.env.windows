import asyncio, time
from aiohttp import web
from aiohttp_jinja2 import render_template

class Handlers:

    def __init__(self):
        self.routes =   [
                            web.get('/', self.main),
                            web.post('/store/public', self.store_public),
                            web.post('/store/local', self.store_local)
                        ]

    async def main(self, request):
        return web.Response(text='touch ma balls')

    async def store_local(self, request):

        # read incoming bytes
        # structure is: timestamp, lux, temp, i-> 123456789,34,23,0
        payload = (await request.read()).decode('utf-8')

        # TODO: process payload such that: str(time_send,lux,temp,iteration)
        processed_payload = payload.decode('utf-8').split(',')

        # just use the helper method
        self.store(processed_payload, str(round(time.time())))

        return web.Response(text='')
    
    async def store_public(self, request):

        # read incoming bytes
        # structure is: timestamp, lux, temp, i-> 123456789,34,23,0
        payload = (await request.read()).decode('utf-8')

        # TODO: process payload such that: str(time_send,lux,temp,iteration)
        processed_payload = str(payload.split(','))   

        # just use the helper method
        self.store(processed_payload, str(round(time.time())))

        return web.Response(text='')
        
    def store(self, payload, time_received):

        print('Payload recieved at: ', time_received)

        # open file as append
        with open('log.txt', 'a') as f:

            # write to file
            # will be: ts_received,ts_send,lux,temp,index\n
            f.write('%s,%s\n'%(time_received, payload))
            # verify that file is satisfactory (run a test)

