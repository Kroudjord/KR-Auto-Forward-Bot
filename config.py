from os import getenv

class Config(object):
      API_HASH = getenv("API_HASH", "9339063403c1f9af11061ec2515083f5)
      API_ID = int(getenv("API_ID", "28104411"))
      AS_COPY = True if getenv("AS_COPY", True) == "`{file_name}`" else True
      BOT_TOKEN = getenv("BOT_TOKEN", "7137476245:AAHwdzoY6FCo405q5ESTvGfoYWTwrt5gdCk")
      CHANNEL = list(x for x in getenv("CHANNEL_ID", "-1001722984461:-1001623633000").replace("\n", " ").split(' '))


# Don't Remove Credit @VJ_Botz
# Subscribe YouTube Channel For Amazing Bot @Tech_VJ
# Ask Doubt on telegram @KingVJ01
