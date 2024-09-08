import uvicorn

from fastapi import FastAPI

from routers.llm import router as llm_router
from routers.ping import router as ping_router

app = FastAPI(swagger_ui_parameters={"syntaxHighlight": False})
app.include_router(llm_router.router)
app.include_router(ping_router.router)


if __name__ == "__main__":

    # uvicorn.run(app, host="0.0.0.0", port=8888)
    uvicorn.run("app:app", host="0.0.0.0", port=8888, reload=True)
