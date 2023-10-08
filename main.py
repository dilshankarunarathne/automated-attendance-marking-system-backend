from fastapi import FastAPI

from routes import auth

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

