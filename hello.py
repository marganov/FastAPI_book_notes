from fastapi import FastAPI

app = FastAPI() # объект FastAPI верхнго уровня представляющий собой всё веб-приложение

@app.get("/hi")
#Декоратор сообщающий: запрос к эндпоинту "/hi" должен быть направлен на следующую функцию(ниже).
#Этот декоратор применяется только к GET (другие глаголы можно, но с отдельными функциями).
def greet(who: str):
    return f"Hello? {who}?"

# запуск Uvicorn внутри приложения
if __name__ == "__main__":
    import uvicorn
    uvicorn.run("hello:app", reload=True) # можно вписать host="...", port=... вместо стандартных
    
# для запуска из командной строки $ uvicorn hello:app --reload
