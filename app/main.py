from fastapi import FastAPI
from . import routes  # Asegúrate de importar las rutas correctamente

# Instancia de FastAPI
app = FastAPI()

# Incluir rutas desde routes.py
app.include_router(routes.router)
