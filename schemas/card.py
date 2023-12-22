# schemaa helps to serialize and also convert mangodb format json to our UI needed
import pandas, os
import csv
from config.database import connection
from models.card import Card
import shutil
import time
# from routes.routers import add_card

CSV_FILE_PATH = 'data'
PROCESSED_CSV_FILE_PATH = 'processed_data'

def cardEntity(db_item) -> dict:
    # return (str(db_item))
    return {
        "ID":   str(db_item["ID"]),
        "CardID"    : db_item["CardID"],
        "Pickup_Timestamp": db_item["Pickup_Timestamp"],
        "User_Contact": db_item["User_Contact"],
        "Delivered_Timestamp": db_item["Delivered_Timestamp"],
        "Returned_Timestamp": db_item["Returned_Timestamp"],
        "Delivery_Exception_Timestamp": db_item["Delivery_Exception_Timestamp"],
        "Delivery_Exception": db_item["Delivery_Exception"],
        "Attempt_left"  :   db_item["Attempt_left"],
    }

def listOfCardEntity(db_item_list) -> list:
    list_card_entity = []
    for item in db_item_list:
        list_card_entity.append(cardEntity(item))
    return list_card_entity

def add_card_from_csv(card: Card):
    if card:
        if connection.local.card.find_one('CardID'):
            # connection.local.card.find_one_and_update
            connection.local.card.find_one_and_update({"CardID": card['CardID']}, {"$set": dict(card)})
        else:
            connection.local.card.insert_one(card)
    return cardEntity(connection.local.card.find_one({"CardID": card['CardID']}))

def move_processed(file):
    shutil.move(file, PROCESSED_CSV_FILE_PATH)

def csv_reader() -> dict:

    while True:
        time.sleep(30)
        print("sleeping 30 second")
        card_status = {}
        for dirpath, dirnames, files in os.walk(CSV_FILE_PATH):
            for file_name in files:
                tmp_file_name_match = file_name.upper()
                if file_name.split('.')[-1] == 'csv':
                    file = os.path.join(CSV_FILE_PATH, file_name)
                    if 'PICKUP' in tmp_file_name_match:
                        with open(file, 'r') as infile:
                            reader = csv.DictReader(infile)
                            for _data in reader:
                                # customize data according to model fields
                                json_dict = {
                                    "ID":   None,
                                    "CardID"    : None,
                                    "User_Contact": None,
                                    "Pickup_Timestamp": None,
                                    "Delivered_Timestamp": None,
                                    "Returned_Timestamp": None,
                                    "Delivery_Exception_Timestamp": None,
                                    "Delivery_Exception": None,
                                    "Attempt_left"  :   None,
                                }
                                json_dict['ID'] = _data['ID']
                                json_dict['CardID'] = _data['Card ID']
                                json_dict['User_Contact'] = _data['User contact']
                                json_dict['Pickup_Timestamp'] = _data['Timestamp']
                                add_card_from_csv(json_dict)
                            move_processed(file)
                            # return listOfCardEntity(connection.local.card.find())
                    elif 'DELIVERED' in tmp_file_name_match:
                        # ID ,Card ID,User contact,Timestamp,Comment
                        # return "Raju"

                        with open(file, 'r') as infile:
                            reader = csv.DictReader(infile)
                            for _data in reader:
                                # return _data
                                # customize data according to model fields
                                json_dict = {
                                    "ID":   None,
                                    "CardID"    : None,
                                    "Pickup_Timestamp": None,
                                    "User_Contact": None,
                                    "Delivered_Timestamp": None,
                                    "Delivery_Exception": None,
                                    "Delivery_Exception_Timestamp": None,

                                    "Returned_Timestamp": None,
                                    "Attempt_left"  :   None,
                                }
                                json_dict['ID'] = _data['ID']
                                json_dict['CardID'] = _data['Card ID']
                                json_dict['User_Contact'] = _data['User contact']
                                json_dict['Delivered_Timestamp'] = _data['Timestamp']
                                json_dict['Delivery_Exception'] = _data['Comment']
                                add_card_from_csv(json_dict)
                            move_processed(file)
                            # return listOfCardEntity(connection.local.card.find())
                    #deliverd case
                        pass
                    elif 'RETURNED' in tmp_file_name_match:
                        with open(file, 'r') as infile:
                            reader = csv.DictReader(infile)
                            for _data in reader:
                                # customize data according to model fields
                                json_dict = {
                                    "ID":   None,
                                    "CardID"    : None,
                                    "Pickup_Timestamp": None,
                                    "User_Contact": None,
                                    "Delivered_Timestamp": None,
                                    "Delivery_Exception": None,
                                    "Delivery_Exception_Timestamp": None,

                                    "Returned_Timestamp": None,
                                    "Attempt_left"  :   None,
                                }
                                # ID,Card ID,User contact,Timestamp

                                json_dict['ID'] = _data['ID']
                                json_dict['CardID'] = _data['Card ID']
                                json_dict['User_Contact'] = _data['User contact']
                                json_dict['Returned_Timestamp'] = _data['Timestamp']
                                add_card_from_csv(json_dict)
                            move_processed(file)
                            # return listOfCardEntity(connection.local.card.find())
                    elif 'EXCEPTION' in tmp_file_name_match:

                        #ID,Card ID,User contact,Timestamp,Comment

                        with open(file, 'r') as infile:
                            reader = csv.DictReader(infile)
                            is_card_found = False
                            for _data in reader:
                                # customize data according to model fields
                                json_dict = {
                                    "ID":   None,
                                    "CardID"    : None,
                                    "Pickup_Timestamp": None,
                                    "User_Contact": None,
                                    "Delivered_Timestamp": None,
                                    "Delivery_Exception": None,
                                    "Returned_Timestamp": None,
                                    "Delivery_Exception_Timestamp": None,
                                    "Attempt_left"  :   None,
                                }
                                json_dict['ID'] = _data['ID']
                                json_dict['CardID'] = _data['Card ID']
                                json_dict['User_Contact'] = _data['User contact']
                                json_dict['Delivery_Exception_Timestamp'] = _data['Timestamp']
                                json_dict['Delivery_Exception'] = _data['Comment']
                                add_card_from_csv(json_dict)
                            move_processed(file)
                    else:
                        pass

