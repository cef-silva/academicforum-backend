from fastapi import FastAPI
from routers import empresa
from routers import usuario
from routers import vaga
from autorize import *
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(usuario.router)
app.include_router(empresa.router)
app.include_router(vaga.router)
