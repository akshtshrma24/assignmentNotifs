import time 

from dataHandler import * 
from logger import *
from canvasData import * 
from constants import * 

warning(f"Discord Webhook URL set to {DISCORD_WEBHOOK}")

warning("Starting Scraper")
while(True):
    parse_and_send(getRawClasses())
    time.sleep(TWO_HOURS)