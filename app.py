"""
Income Control System V1.2
Jorge Andres Gandara Oliveros - T00065470
Robert Andres Pantoja Calderon - T00060394
Diego Andres Garcia Alvarez - T00064583
Angelo Alexander Howell Diaz - T00061114
"""

import uvicorn
from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

from logic.event import event
from logic.event_controller import eventController

from logic.item import item
from logic.item_controller import itemController

from logic.client import client
from logic.client_controller import clientController

app = FastAPI()
st_object_event = eventController()
st_object_client = clientController()
st_object_item = itemController()
origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def read_root():
    return {"200": "Welcome To Income Control System API"}

@app.get("/api/client", )
async def root_client():
    return st_object_client.show()

@app.post("/api/client")
async def add_client(id: str, name: str, lastName: str, address: str, phone: str, email: str, stayTime: int, event: str, allowedPlaces: str):
    cli = client(id=id, name=name, lastName=lastName, 
                  address=address, phone=phone,
                  email=email, stayTime=stayTime, 
                  event=event, allowedPlaces=allowedPlaces)
    return st_object_client.add(cli)

@app.get("/api/item")
async def root_item():
    return st_object_item.show()

@app.post("/api/item")
async def add_item(id: str, name: str, description: str, allowedPlaces: str, status: str):
    return st_object_item.add(item(id=id, name=name, description=description, allowedPlaces=allowedPlaces, status=status))

@app.get("/api/event")
async def root_event():
    return st_object_event.show()

@app.post("/api/event")
async def add_event(id: str, name: str, eventTime: int, place: str):
    return st_object_event.add(event(id=id, name=name, eventTime=eventTime, place=place))

if __name__ == "__main__":
    uvicorn.run(app, port=33507)
