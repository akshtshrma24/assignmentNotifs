import requests 
import constants as constants
import json
import datetime

from logger import * 

# This will just print it for now
def parse_and_send(jsonClass):
    if (len(jsonClass) != 0):
        for k in jsonClass:
            if ('due_at' in k['assignment']):
                dueJson = json.loads(json.dumps(k['assignment']))
                if(time_difference(str(datetime.datetime.now()), str(parse_time(dueJson['due_at'])))):
                    discordMessage(k['context_name'], dueJson['name'])
    else:
        success("No Homework")


def parse_time(time):
    time = time.split('T')
    utcHour = int(str(time[1]).split(':')[0])
    utcHour -= 7
    if (utcHour < 0):
        day = (int(str(time[0]).split('-')[2]) - 1)
        time[0] = str(time[0]).replace(str(time[0]).split('-')[2], str(day))
        time[1] = str(time[1]).replace(
            str(time[1]).split(':')[0], str(utcHour + 24))
        return ' '.join(time)[0:-1]
    else:
        time[1] = str(time[1]).replace(
            str(time[1]).split(':')[0], str(utcHour))
    return ' '.join(time)[0:-1]


def time_difference(time1, time2):
    if (int(time2.split(" ")[0].split("-")[2]) == int(time1.split(" ")[0].split("-")[2]) and
            int(time2.split(" ")[1].split(":")[0]) - int(time1.split(" ")[1].split(":")[0]) < 3):
        return True
    return False


def discordMessage(className, assignmentName):
    # webhook url, from here: https://i.imgur.com/f9XnAew.png
    url = constants.DISCORD_WEBHOOK

    # for all params, see
    # https://discordapp.com/developers/docs/resources/webhook#execute-webhook
    data = {
        "content": "Assignment Due",
        "username": className
    }
    data["embeds"] = [
        {
            "description": f"{assignmentName} is due within 3 hours make sure you do it.",
            "title": className}]
    response = requests.post(url, json=data)
    if(response.status_code < 400):
        success("Sent Discord Message")
    else:
        error("Error sending Message")
