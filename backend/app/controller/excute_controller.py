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
async def proxy_chrome():
    queue: ZeroMQ = zero_queue_context.get()
    data = {'action': 'chrome-proxy', 'data': ''}
    queue.publish_message(data=data)
    return 'success'


@execute_route.get("/vms/execute/chrome-proxy-refresh")
async def proxy_refresh_chrome():
    queue: ZeroMQ = zero_queue_context.get()
    data = {'action': 'chrome-proxy-refresh', 'data': ''}
    queue.publish_message(data=data)
    return 'success'


@execute_route.get("/vms/execute/stop-actions")
async def stop_action():
    queue: ZeroMQ = zero_queue_context.get()
    data = {'action': 'stop-actions', 'data': ''}
    queue.publish_message(data=data)
    return 'success'


@execute_route.get("/vms/execute/start-actions")
async def login_chrome():
    queue: ZeroMQ = zero_queue_context.get()
    data = {'action': 'start-actions', 'data': ''}
    queue.publish_message(data=data)
    return 'success'

@execute_route.get("/vms/execute/press-enter")
async def login_chrome():
    queue: ZeroMQ = zero_queue_context.get()
    data = {'action': 'press-enter', 'data': ''}
    queue.publish_message(data=data)
    return 'success'

