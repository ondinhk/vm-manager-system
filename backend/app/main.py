from app.context.zeromq_context import zero_queue_context
from app.controller.action_controller import action_route
from app.controller.excute_controller import execute_route
from app.controller.video_controller import video_route
from app.controller.vm_controller import vm_router
from app.queue.zeromq import ZeroMQ
from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware
from uvicorn import run

app = FastAPI(debug=True)
origins = ["*"]
queue_init = ZeroMQ()
zero_queue_context.set(queue_init)

app.add_middleware(CORSMiddleware, allow_origins=origins, allow_credentials=True, allow_methods=["*"],
                   allow_headers=["*"])

app.include_router(action_route)
app.include_router(video_route)
app.include_router(vm_router)
app.include_router(execute_route)

if __name__ == "__main__":
    run(app, host="0.0.0.0", port=9000)
