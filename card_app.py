###import statement

from fastapi import FastAPI
from routes.routers import card_router, data_process_router

#Create app
app = FastAPI()

#Register your router
app.include_router(data_process_router)
app.include_router(card_router)
