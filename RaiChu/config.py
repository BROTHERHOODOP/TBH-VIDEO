## Coder are here

import os
from os import getenv
from dotenv import load_dotenv

if os.path.exists("local.env"):
    load_dotenv("local.env")

load_dotenv()
admins = {}
SESSION_NAME = getenv("SESSION_NAME", "AQB34wTqm2_1S_UpifFuVEZJIcQaTl_ARHipQtS5xZN_rZRCvoGK5Rbap87FgVFmQSjEZVLsA5DP03R7OpI0gxrhuBFmFAIg6Q-WNT-6uvIZDQNf27YVKuhM20QHoFAtb5lFGHPMex5Xl7ie8Cl4HJUB9q-YR8CqSUeMK2ccUQKnoRqxzEflHQxzWXhOC3huxoTjzOTlrbHBWyrtdNsxkJiZ3GTsqqhpJbYNt-LJrdk1cC5EniLq4qs4HJiLYS0LZ6QGy1paF_CgCozJORuW4j9uaHcaGxNN3VcgnINMvYQ70Peswd1V_U6k5EicJAjBtH8XHPIfkBxiGNkFY_LtoxcwAAAAAUBkHSkA")
BOT_TOKEN = getenv("5569648753:AAEYbBQzWxHggDEBX3s4NXSjmavg8MrgBF0")
BOT_NAME = getenv("༄ᵗᵇʰ᭄✿Mᴜsɪᴄ࿐")
API_ID = int(getenv("API_ID", "8186557"))
API_HASH = getenv("API_HASH", "efd77b34c69c164ce158037ff5a0d117")
OWNER_NAME = getenv("OWNER_NAME", "HELLBOY")
ALIVE_NAME = getenv("ALIVE_NAME", "HELLBOY")
ASSISTANT_USERNAME = getenv("ASSISTANT_USERNAME", "TBH_ASSISTANT2")
BOT_USERNAME = getenv("TBH_X_MUSIC_BOT")
ASSISTANT_NAME = getenv("ASSISTANT_NAME", "⏤͟͟͞͞𝑻𝑩𝑯ꗄ𝑨𝑺𝑰𝑺𝑻𝑨𝑵𝑻")
GROUP_SUPPORT = getenv("GROUP_SUPPORT")
UPDATES_CHANNEL = getenv("UPDATES_CHANNEL")
SUDO_USERS = list(map(int, getenv("SUDO_USERS").split()))
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/ ! .").split())
ALIVE_IMG = getenv("ALIVE_IMG", "https://telegra.ph/file/4d83f2e52df49e973e18d.jpg")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "350"))
UPSTREAM_REPO = getenv("UPSTREAM_REPO", "https://github.com/AMANTYA1/RaiChu-MusicV2")
IMG_1 = getenv("IMG_1", "https://telegra.ph/file/d6f92c979ad96b2031cba.png")
IMG_2 = getenv("IMG_2", "https://telegra.ph/file/6213d2673486beca02967.png")
IMG_3 = getenv("IMG_3", "https://telegra.ph/file/f02efde766160d3ff52d6.png")
IMG_4 = getenv("IMG_4", "https://telegra.ph/file/be5f551acb116292d15ec.png")
IMG_5 = getenv("IMG_5", "https://telegra.ph/file/c3401a572375b569138c3.png")
IMG_6 = getenv("IMG_6", "https://telegra.ph/file/d8f8fc1de9110b93ca94c.jpg")
YOUTUBE_IMG_URL = getenv("YOUTUBE_IMG_URL", "https://telegra.ph/file/58da23d726b601dc3b18e.jpg")
