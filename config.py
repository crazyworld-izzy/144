import re
from os import getenv

from dotenv import load_dotenv
from pyrogram import filters

load_dotenv()

# Get this value from my.telegram.org/apps
API_ID = "13569561"
API_HASH = "a689fce8b9f1c32c899b53811451385f"

# Get your token from @BotFather on Telegram.
BOT_TOKEN = "7788838360:AAFbtcOHOiLJKvQYelMc3ZYGsFbpRpcti-o"
# -------------------------------------------------------
OWNER_USERNAME = getenv("OWNER_USERNAME","OwnerofTheDenki")
# --------------------------------------------------------
BOT_USERNAME = getenv("BOT_USERNAME","DenkiMusicBot")
# --------------------------------------------------------
BOT_NAME = getenv("𝟷𝟺𝟺 ᴍᴜsɪᴄ 🎶 ʙᴏᴛ")
# ---------------------------13569561------------------------------


# Get your mongo url from cloud.mongodb.com
MONGO_DB_URI = "mongodb+srv://ftyvfbgubhu7:hDZwwlNzlKBzls84@ameliamusicbot.f7dzw.mongodb.net/?retryWrites=true&w=majority&appName=AmeliaMusicbot"

DURATION_LIMIT_MIN = int(getenv("DURATION_LIMIT", 17000))

# Chat id of a group for logging bot's activities
LOGGER_ID = int(getenv("LOGGER_ID",  -1002329626146))

# Get this value from @PURVI_HELP_BOT on Telegram by /id
OWNER_ID = 7941950690


# make your bots privacy from telegra.ph and put your url here 
PRIVACY_LINK = getenv("PRIVACY_LINK", "https://graph.org/PRIVACY-FOR-TEAM-PURVI-BOTS-09-18")

## Fill these variables if you're deploying on heroku.
# Your heroku app name
HEROKU_APP_NAME = getenv("HEROKU_APP_NAME")
# Get it from http://dashboard.heroku.com/account
HEROKU_API_KEY = getenv("HEROKU_API_KEY")

UPSTREAM_REPO = getenv(
    "UPSTREAM_REPO",
    "https://github.com/crazyworld-izzy/144",
)
UPSTREAM_BRANCH = getenv("UPSTREAM_BRANCH", "master")
GIT_TOKEN = getenv(
    "GIT_TOKEN", None
)  # Fill this variable if your upstream repository is private

SUPPORT_CHANNEL = getenv("SUPPORT_CHANNEL", "https://t.me/denkimusic")
SUPPORT_CHAT = getenv("SUPPORT_CHAT","https://t.me/denkimusic")

# Set this to True if you want the assistant to automatically leave chats after an interval
AUTO_LEAVING_ASSISTANT = bool(getenv("AUTO_LEAVING_ASSISTANT", False))


# Get this credentials from https://developer.spotify.com/dashboard
SPOTIFY_CLIENT_ID = getenv("SPOTIFY_CLIENT_ID", None)
SPOTIFY_CLIENT_SECRET = getenv("SPOTIFY_CLIENT_SECRET", None)


# Maximum limit for fetching playlist's track from youtube, spotify, apple links.
PLAYLIST_FETCH_LIMIT = int(getenv("PLAYLIST_FETCH_LIMIT", 555))


# Telegram audio and video file size limit (in bytes)
TG_AUDIO_FILESIZE_LIMIT = int(getenv("TG_AUDIO_FILESIZE_LIMIT", 904857600))
TG_VIDEO_FILESIZE_LIMIT = int(getenv("TG_VIDEO_FILESIZE_LIMIT", 9073741824))
# Checkout https://www.gbmb.org/mb-to-bytes for converting mb to bytes


# Get your pyrogram v2 session from @StringFatherBot on Telegram
STRING1 = "BQDNvmIAd8YAUsE5grRjfpcyu6SbKSfJH8fFA9VSvpZ6-yJT5tFI9tDEq_aZKHCAIMZ1saUD7n2bf1ErK5MLKr_UEHxi6AYVDiYvrY90BXdtDZEJB8i0yIP31D6suxZNMtkh8QfD_FX4cGRI1vmx3gqYSsbc2CrrLF5ETNK7yxU6Q2IMhESCCFwgqZgwL4Op26FTNir03NFAKNkCUIt_aYaLr8P4esxXmWMQ44BvBobt-Uu3SKM3UDmi23nDkwfJCIJiB3UMxF6NXildo2QQgvI2Ln9l2XLIpPKcI103sGUBPJuKGm1EE105RrxbpUTSzTDW0Vc2k5rmbY04flQBvDHMxtalwwAAAAG8rlp7AA"
STRING2 = getenv("STRING_SESSION2", None)
STRING3 = getenv("STRING_SESSION3", None)
STRING4 = getenv("STRING_SESSION4", None)
STRING5 = getenv("STRING_SESSION5", None)


BANNED_USERS = filters.user()
adminlist = {}
lyrical = {}
votemode = {}
autoclean = []
confirmer = {}


START_IMG_URL = getenv(
    "START_IMG_URL", "https://envs.sh/kCQ.jpg"
)
PING_IMG_URL = getenv(
    "PING_IMG_URL", "https://envs.sh/k3F.jpg"
)
PLAYLIST_IMG_URL = "https://envs.sh/k3F.jpg"
STATS_IMG_URL = "https://envs.sh/k3F.jpg"
TELEGRAM_AUDIO_URL = "https://telegra.ph/file/51cb8a22e65caa4382879.jpg"
TELEGRAM_VIDEO_URL = "https://telegra.ph/file/51cb8a22e65caa4382879.jpg"
STREAM_IMG_URL = "https://te.legra.ph/file/bd995b032b6bd263e2cc9.jpg"
SOUNCLOUD_IMG_URL = "https://te.legra.ph/file/bb0ff85f2dd44070ea519.jpg"
YOUTUBE_IMG_URL = "https://te.legra.ph/file/6298d377ad3eb46711644.jpg"
SPOTIFY_ARTIST_IMG_URL = "https://te.legra.ph/file/37d163a2f75e0d3b403d6.jpg"
SPOTIFY_ALBUM_IMG_URL = "https://te.legra.ph/file/b35fd1dfca73b950b1b05.jpg"
SPOTIFY_PLAYLIST_IMG_URL = "https://te.legra.ph/file/95b3ca7993bbfaf993dcb.jpg"


def time_to_seconds(time):
    stringt = str(time)
    return sum(int(x) * 60**i for i, x in enumerate(reversed(stringt.split(":"))))


DURATION_LIMIT = int(time_to_seconds(f"{DURATION_LIMIT_MIN}:00"))


if SUPPORT_CHANNEL:
    if not re.match("(?:http|https)://", SUPPORT_CHANNEL):
        raise SystemExit(
            "[ERROR] - Your SUPPORT_CHANNEL url is wrong. Please ensure that it starts with https://"
        )

if SUPPORT_CHAT:
    if not re.match("(?:http|https)://", SUPPORT_CHAT):
        raise SystemExit(
            "[ERROR] - Your SUPPORT_CHAT url is wrong. Please ensure that it starts with https://"
        )
