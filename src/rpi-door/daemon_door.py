#!/usr/bin/python3 -u
#
import serial
import psycopg2 as psycopg
import slack
import time
import yaml
import RPi.GPIO as GPIO

try:
    from yaml import CLoader as Loader, CDumper
except ImportError:
    from yaml import Loader


CONFIG_FILE = 'config.cfg'
cfg = yaml.load(open(CONFIG_FILE, 'r'), Loader=Loader)

DOORBOT_TOKEN = cfg['doorbot-token']

slack_client = slack.WebClient(token=DOORBOT_TOKEN)

# Door lock control GPIO setup
DOOR_LOCK_PIN = 40 # GPIO21 in the raspberry pi map
GPIO.setmode(GPIO.BOARD)
GPIO.setup(DOOR_LOCK_PIN, GPIO.OUT)

def open_door():
    GPIO.output(DOOR_LOCK_PIN, GPIO.HIGH)
    time.sleep(1)
    GPIO.output(DOOR_LOCK_PIN, GPIO.LOW)
    print("Door opened!")

def slack_notify(username):
    channel = "#door-events"
    message = '%s entered' % username
    try:
        slack_client.chat_postMessage(channel=channel, text=message, as_user=True)
    except:
        pass

def get_user(key):
    print("Get user for key:", key)
    USER_COLUMN = 1
    DOOR_COLUMN = 3
    conn = psycopg.connect(user = cfg['db-config']['user'],
                                  password = cfg['db-config']['password'],
                                  host=cfg['db-config']['server'],
                                  port=cfg['db-config']['port'],
                                  database='visitors')
    c = conn.cursor()
    c.execute("SELECT * FROM users WHERE key='%s'" % (key.decode('utf-8')))
    user = c.fetchone()
    conn.close()
    print("Query data:", user)
    if user:
        return user[USER_COLUMN], user[DOOR_COLUMN]
    else:
        return None

ser = serial.Serial('/dev/ttyUSB0', 115200)

while True:
    try:
        serial_data = ser.readline().rstrip()
        print(serial_data)
        user = get_user(serial_data)
        print(user)
        if user and user[1]:
            open_door()
            slack_notify(user[0])
    except KeyboardInterrupt:
        ser.close()
        break
