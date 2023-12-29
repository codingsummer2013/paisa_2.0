import datetime
from time import sleep

from chitragupta import averaging_util_wrapper
from shoorveer import continuity, aaj_ka_bazaar, krishna, averaging_util

while True:
    print("Running now at time", datetime.datetime.now())
    continuity.run()
    aaj_ka_bazaar.run()
    krishna.run()
    averaging_util.run()
    sleep(100)
