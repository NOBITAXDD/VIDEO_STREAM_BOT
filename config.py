import os
from os import getenv
from dotenv import load_dotenv

if os.path.exists("local.env"):
    load_dotenv("local.env")

load_dotenv()
admins = {}
SESSION_NAME = getenv("SESSION_NAME", "session")
BOT_TOKEN = getenv("BOT_TOKEN")
BOT_NAME = getenv("BOT_NAME", "Video Stream")
API_ID = int(getenv("API_ID"))
API_HASH = getenv("API_HASH")
OWNER_NAME = getenv("OWNER_NAME", "NOBITA_XD")
ALIVE_NAME = getenv("ALIVE_NAME", "NOBITA_OP")
BOT_USERNAME = getenv("BOT_USERNAME", "Nobita_bot")
ASSISTANT_NAME = getenv("ASSISTANT_NAME", "Nobita_assistant")
GROUP_SUPPORT = getenv("GROUP_SUPPORT", "AAPLI_YAARI")
UPDATES_CHANNEL = getenv("UPDATES_CHANNEL", "AAPLI_YAARI")
UPSTREAM_REPO = getenv("UPSTREAM_REPO", "https://github.com/kuldiprathod/video-stream-1")
SUDO_USERS = list(map(int, getenv("SUDO_USERS").split()))
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/ ! .").split())
ALIVE_IMG = getenv("ALIVE_IMG", "https://telegra.ph/file/a0adbb89423c5aa6770d4.jpg")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "60"))
IMG_1 = getenv("IMG_1", "https://telegra.ph/file/a0adbb89423c5aa6770d4.jpg")
IMG_2 = getenv("IMG_2", "https://telegra.ph/file/a0adbb89423c5aa6770d4.jpg")
IMG_3 = getenv("IMG_3", "https://telegra.ph/file/a0adbb89423c5aa6770d4.jpg")
