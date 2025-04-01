from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .routers import contents, categories

app = FastAPI()

app.include_router(contents.router)
app.include_router(categories.router)

origins = [
    "http://localhost:3000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=False,
    allow_methods=["*"],
    # allow_headers=["*"],
)