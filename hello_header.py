from fastapi import FastAPI, Header

app = FastAPI()

@app.post("/hi")
def greed_header(who: str = Header()):
    return f"Hello! {who}!"

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("hello_header:app", reload=True)