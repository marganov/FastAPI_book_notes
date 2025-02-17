from fastapi import FastAPI, Response

app = FastAPI()

@app.get("/header/{name}/{value}")
def hello_restp(name: str, value: str, response: Response):  
    response.headers[name] = value
    return "response body"



if __name__ == "__main__":
    import uvicorn
    uvicorn.run("app_response:app", reload=True)