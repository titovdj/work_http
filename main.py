from fastapi import FastAPI
from routers import router


app=FastAPI()


app.include_router(router)


@app.on_event("startup")
async def startup_event():
    pass