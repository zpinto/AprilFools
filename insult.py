import time
import random
import os

# launchctl load ~/Library/LaunchAgents/insults.plist
# launchctl unload ~/Library/LaunchAgents/insults.plist

if __name__ == "__main__":
    insult_file_name = "insults.txt"
    insult_file = open(insult_file_name, "r")
    insults = [line for line in insult_file]

    while(True):
        time.sleep(10)
        insult = random.choice(insults)
        os.system("say {}".format(insult))
