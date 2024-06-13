from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def read_main():
<<<<<<< HEAD
    return {"msg": "Thank You Patrick"}
=======
    return {"msg": "THANK YOU Gauthier"}
>>>>>>> fe65e9be4dd531fe8ce8d1eb3d4693aa6735122f


