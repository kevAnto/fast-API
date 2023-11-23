from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def read_main():
    return {"msg": "NOV23 BDO INT - MC1 - Introduction to DevOps"}


