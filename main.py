from fastapi import FastAPI



app = FastAPI()
@app.get("/")
def check_test():
    return{
        "msg":"testing rendor"
    }
# https://github.com/programbits/fastapi_dep.git