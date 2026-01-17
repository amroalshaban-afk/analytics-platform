from fastapi import FastAPI
from api.utils.func1 import add


def generator(app: FastAPI):

    @app.get('/')
    async def endpoint1():
        return {"endpoint1": f"Hello, MOM! {add(1, 1)}"}