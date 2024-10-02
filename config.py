from os import environ 

class Config:
    API_ID = os.environ.get("API_ID", "21723836")
    API_HASH = os.environ.get("API_HASH", "f755ab041ac9ab14ab0c25606dd92156")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "7939476396:AAEGZIF4RHNpykMXmoR7Q6JV3YPJ2NqLqJw") 
    BOT_SESSION = os.environ.get("BOT_SESSION", "forward-bot") 
    DB_URL = os.environ.get("DB_URL", "mongodb+srv://forwardbot17:rvforward1@cluster0.ubuxz.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
    DB_NAME = os.environ.get("DB_NAME", "Cluster0")
    OWNER_ID = [int(id) for id in os.environ.get("OWNER_ID", '7052947046').split()]
    
class temp(object): 
    lock = {}
    CANCEL = {}
    forwardings = 0
    BANNED_USERS = []
    IS_FRWD_CHAT = []
    
