from fastapi import FastAPI, Response, Query,HTTPException
from .cars import create_cars, get_car_by_id

cars = create_cars(100)  # Здесь хранятся список машин
app = FastAPI()


@app.get("/")
def index():
    return Response("<a href='/cars'>Cars</a>")

@app.get("/cars")
def pagination_cars(page: int = Query(0, ge=0), limit: int = Query(21, gt=0)):
    return cars[page:page + limit]

@app.get("/cars/{id}", response_model=dict)

def read_car(id: int):
    car = get_car_by_id(id, cars)
    if car:
        return car
    else:
        raise HTTPException(status_code=404, detail="Not found")

