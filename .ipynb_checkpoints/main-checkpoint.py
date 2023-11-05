from fastapi import fastApi
from fasttapi.middleware.cors import CORSMiddleware
from uvicorn import run
import os

app = fastApi()


# headers
origins = ["*"]
methods = ["*"]
headers = ["*"]


app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=methods,
    allow_headers=headers,
)
