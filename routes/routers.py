from fastapi import APIRouter
from models.card import Card
from config.database import connection
from schemas.card import cardEntity, listOfCardEntity, csv_reader
import threading

# from bson import ObjectId

card_router = APIRouter()
data_process_router = APIRouter()

@data_process_router.get('/')
async def start_data_process_thread():
    csv_reader_thread = threading.Thread(target=csv_reader)
    csv_reader_thread.start()
    return "hello world"

@card_router.get('/get_card_status/{CardID}')
async def find_card_by_id(cardId):
    return cardEntity(connection.local.card.find_one({"CardID": cardId}))

    # if card_exists:
    #     return cardEntity(connection.local.card.find_one({"CardID": cardId}))
    # else:
    #     ##process received file from organization/companies
    #     return csv_reader(cardId)

@card_router.post('/card_add')
async def add_card(card: Card):
    connection.local.card.insert_one(dict(card))
    return listOfCardEntity(connection.local.card.find())