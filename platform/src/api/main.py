import uvicorn
from fastapi import FastAPI
from api.routes.endpoints import paths as api_paths


app = FastAPI()
for api_path in api_paths:
    api_path(app)


if __name__ == '__main__':
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)