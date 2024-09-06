# Message Sender Interface (MSI)

import sys
import json
import engine
import time

# open browser
pywp = engine.PyWp()

# recieve group names and message
rawdata = sys.stdin.read()

# process the data and send
data = json.loads(rawdata)
message = data.pop()
for i in data:
    pywp.send_message(i, message)
    
time.sleep(120)

