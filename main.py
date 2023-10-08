import uvicorn
from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

import config
from routes import auth, student

app = FastAPI()

origins = ['http://localhost:3000', 'http://192.168.178.23:3000']  # add your front-end ip:port here

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(auth.router)
app.include_router(student.router)

if __name__ == '__main__':
    uvicorn.run(
        app,
        host=config.get("application", "application.host"),
        port=int(config.get("application", "application.port"))
    )
