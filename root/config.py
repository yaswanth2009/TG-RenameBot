"""
© Mrvishal2k2
RenameBot
This file is a part of mrvishal2k2 rename repo
Dont kang !!!
© Mrvishal2k2
"""
import os


class Config(object):
    APP_ID = int(os.environ.get("APP_ID","11253846"))
    API_HASH = os.environ.get("API_HASH","8db4eb50f557faa9a5756e64fb74a51a")
    TG_BOT_TOKEN = os.environ.get("TG_BOT_TOKEN","5332419326:AAGz2Nwo8ZPGa4LusUuaPtdOU2_ibvqMGSA")
    AUTH_USERS = [int(x) for x in os.environ.get("AUTH_USERS", "").split()]
    DOWNLOAD_LOCATION = "./bot/DOWNLOADS"
    DB_URI = os.environ.get("DATABASE_URL")
    # owner is for log cmd only owner can use (this can be multiple users)
    OWNER_ID = [int(i) for i in os.environ.get("OWNER_ID").split("883128927")]
    OWNER_USERNAME = os.environ.get("OWNER_USERNAME", "Yaswanth_venkata_naga_sai")
    CUSTOM_CAPTION = os.environ.get("CUSTOM_CAPTION", False)
