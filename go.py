import datetime
from time import sleep

from shoorveer import continuity, aaj_ka_bazaar, krishna

while True:
    print("Running now at time", datetime.datetime.now())
    continuity.run()
    aaj_ka_bazaar.run()
    krishna.run()
    sleep(100)
