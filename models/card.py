from pydantic import BaseModel
from typing import Union

class Card(BaseModel):
    ID  : str
    CardID :  str
    User_Contact:  str
    Pickup_Timestamp: Union[str, None] = None
    Delivered_Timestamp: Union[str, None] = None
    Delivery_Exception: Union[str, None] = None
    Delivery_Exception_Timestamp: Union[str, None] = None
    Returned_Timestamp: Union[str, None] = None
    Attempt_left: Union[int, int] = 2