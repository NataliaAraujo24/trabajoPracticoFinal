from typing import Optional
from fastapi import FastApi
from pydantic import BaseModel
class Mensaje(BaseModel):
    id: Optional[int]= None
    user:str
    message: str

app = FastAPI()

mensaje =[]

"get>>>>> OBTIENE"

@app.get("/")
def listar_mensajes():
    return mensaje
@app.get("/mensajes/{id}", response_model=Mensaje)
def obtener_mensaje(id: int):
    for mensaje in mensaje:
        if mensaje["id"]== id:
            return mensaje   
    return {"error":"Mensaje no encontrado"}

"post>>>>>>>>> CREA Y AGREGA A BASE DE DATOS"
@app.post("mensajes", response_model=Mensaje)
def crear_mensaje(mensaje: Mensaje):
    mensaje.id = len(mensaje) + 1
    mensaje.append(mensaje)
    return mensaje


"put>>>>>>>>>ACTUALIZA UNA PERSONA EXISTENTE"
app.put("/mensajes/{id}", response_model=Mensaje)
def actualizar_mensaje(mensaje_id :int, mensaje: Mensaje):
    for index in enumerate(mensaje):
        if mensaje.id == mensaje.id:
           mensaje [index].update(mensaje)
           return mensaje[index]
    return {"Error":"Mensaje no Encontrado"}

"delete>>>>>>>>>ELIMINA PERSONA POR ID"
@app.delete("/mensajes/{id}", response_model=Mensaje)
def borrar_mensaje(mensaje_id :int, mensaje: Mensaje):
    for index in enumerate(mensaje):
        if mensaje.id == mensaje.id:
           mensaje [index].delete(mensaje)

           return mensaje[index]
    return {"Error":"Mensaje no Encontrado"}



                        



