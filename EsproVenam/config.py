import os
from os import getenv

class Config:
    BOT_TOKEN = getenv("BOT_TOKEN", None)
    BOT_TOKEN1 = getenv("BOT_TOKEN1", None)
    BOT_TOKEN2 = getenv("BOT_TOKEN2", None)
    BOT_TOKEN3 = getenv("BOT_TOKEN3", None)
    BOT_TOKEN4 = getenv("BOT_TOKEN4", None)
    BOT_TOKEN5 = getenv("BOT_TOKEN5", None)
    BOT_TOKEN6 = getenv("BOT_TOKEN6", None)
    BOT_TOKEN7 = getenv("BOT_TOKEN7", None)
    BOT_TOKEN8 = getenv("BOT_TOKEN8", None)
    BOT_TOKEN9 = getenv("BOT_TOKEN9", None)
    
    STRING_SESSION = getenv("STRING_SESSION", None)
    API_HASH= getenv('API_HASH')
    API_ID=int(getenv('API_ID'))
        
    if not API_HASH:
        raise ValueError("API_HASH not set")

    if not API_ID:
        raise ValueError("API_ID not set")
    if not BOT_TOKEN:
        raise ValueError("BOT_TOKEN not set")
