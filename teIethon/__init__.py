from bot.utilsbot import *
from bot.callbacks import *
from bot.helptexts import (
    welcomehelpp,
    filterrhelp,
    promotehelpp,
    banhelpp,
    kickhelpp,
    pinhelpp,
    purgehelpp,
    notesshelp,
    lockktypes,
    lockhelpp,
)

import csv
import json
import os
import re
import time
import uuid
from io import BytesIO
from telethon import *
from telethon.tl import *
from telethon.tl.types import User
from telethon.tl.types import MessageMediaDocument, DocumentAttributeFilename

admin_cmd = cmd
adminbot = utilsbot
gtransbot = utilsbot
