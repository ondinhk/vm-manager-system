from app.context.zeromq_context import zero_queue_context
from app.queue.zeromq import ZeroMQ
from fastapi import APIRouter

execute_route = APIRouter(tags=['Execute manage'])


@execute_route.get("/vms/execute/chrome-open")
async def open_chrome():
    queue: ZeroMQ = zero_queue_context.get()
    data = {'action': 'chrome-open', 'data': ''}
    queue.publish_message(data=data)
    return 'success'


@execute_route.get("/vms/execute/chrome-actions")
async def login_chrome():
    queue: ZeroMQ = zero_queue_context.get()
    data = {'action': 'chrome-actions', 'data': ''}
    queue.publish_message(data=data)
    return 'success'


@execute_route.get("/vms/execute/chrome-youtube")
async def youtube_chrome():
    queue: ZeroMQ = zero_queue_context.get()
    data = {'action': 'chrome-youtube', 'data': ''}
    queue.publish_message(data=data)
    return 'success'


@execute_route.post("/vms/execute/input")
async def input_value(data: dict):
    queue: ZeroMQ = zero_queue_context.get()
    data = {'action': 'input-value', 'data': data['input_value']}
    queue.publish_message(data=data)
    return 'success'


@execute_route.get("/vms/execute/screen")
async def take_screen():
    queue: ZeroMQ = zero_queue_context.get()
    data = {'action': 'take-screen', 'data': ""}
    queue.publish_message(data=data)
    return 'success'


@execute_route.get("/vms/execute/chrome-proxy")
async def youtube_chrome():
    queue: ZeroMQ = zero_queue_context.get()
    data = {'action': 'chrome-proxy', 'data': ''}
    queue.publish_message(data=data)
    return 'success'


@execute_route.get("/vms/execute/chrome-proxy-refresh")
async def youtube_chrome():
    queue: ZeroMQ = zero_queue_context.get()
    data = {'action': 'chrome-proxy-refresh', 'data': ''}
    queue.publish_message(data=data)
    return 'success'
