from fastapi import FastAPI
# import uvicorn
app = FastAPI()

@app.get("/")
def func(number : int):
    return number * 2



@app.get('/ruta')
def func2():
    return {'ruta' : 'otra ruta'}


#if __name__ == '__main__':
#    uvicorn.run(app, host='0.0.0', port=8001)

