"""
Income Control System V1.1.1
Jorge Andres Gandara Oliveros - T00065470
Robert Andres Pantoja Calderon - T00060394
Diego Andres Garcia Alvarez - T00064583
Angelo Alexander Howell Diaz - T00061114
"""

import uvicorn
from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

from logic.evento import evento
from logic.evento_controller import EventoController

from logic.objeto import objeto
from logic.objeto_controller import ObjetoController

from logic.cliente import cliente
from logic.cliente_controller import ClienteController

app = FastAPI()
st_object_evento = EventoController()
st_object_cliente = ClienteController()
st_object_objeto = ObjetoController()
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
    return {"200": "Welcome To Evento Restful API"}

@app.get("/api/cliente", )
async def root_cliente():
    return st_object_cliente.show()

@app.post("/api/cliente")
async def add_cliente(id: str, nombre: str, apellido: str, direccion: str, telefono: str, 
                      email: str, tiempoPermanencia: int, evento: str, lugaresPermitidos: str):
    cli = cliente(id=id, nombre=nombre, apellido=apellido, 
                  direccion=direccion, telefono=telefono,
                  email=email, tiempoPermanencia=tiempoPermanencia, 
                  evento=evento, lugaresPermitidos=lugaresPermitidos)
    return st_object_cliente.add(cli)

@app.get("/api/objeto")
async def root_objeto():
    return st_object_objeto.show()

@app.post("/api/objeto")
async def add_objeto(id: str, nombre: str, descripcion: str, lugaresPermitidos: str, estado: str):
    return st_object_objeto.add(objeto(id=id, nombre=nombre, descripcion=descripcion, lugaresPermitidos=lugaresPermitidos, estado=estado))

@app.get("/api/evento")
async def root_evento():
    return st_object_evento.show()

@app.post("/api/evento")
async def add_evento(id: str, nombre: str, tiempoEvento: int, lugar: str):
    return st_object_evento.add(evento(id=id, nombre=nombre, tiempoEvento=tiempoEvento, lugar=lugar))

if __name__ == "__main__":
    uvicorn.run(app, port=33507)
