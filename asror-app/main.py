import uvicorn
from fastapi import FastAPI, Request

app = FastAPI(
    title="Asror",
    version="9.0",
    description="test description`"
)


@app.get("/")
async def root(request: Request):
    client_host = request.client.host

    return {
        "message": "Welcome to NLP Core API!",
        "client_ip": client_host
    }


if __name__ == '__main__':
    host = "localhost"
    port = 44334
    environment = "development"

    if environment == "development":
        uvicorn.run("main:app", host=host, port=port, reload=True)
    else:
        uvicorn.run(app, host=host, port=port)