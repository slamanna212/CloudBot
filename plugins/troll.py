"""
Troll.py
Plugin with commands for #Trollchromosomes
You need a file in the data directory called troll.txt
Format (new item each line): website url,website password,submit url, 
submit password, rules, pets url, pets password
"""

import codecs
import os

from cloudbot import hook

@hook.on_start()
def load_troll(bot):
    global TROLL_DATA
    with codecs.open(os.path.join(bot.data_dir, "troll.txt"), encoding="utf-8") as f:
        TROLL_DATA = [line.strip() for line in f.readlines() if not line.startswith("//")]

opt_in = ["#trollchromosomes","##trollmods"]

@hook.command()
def trolls(chan):
        if chan not in opt_in:
            return
        response = "Here is our website: {} | The password is {}".format(TROLL_DATA[0], TROLL_DATA[1])
        return response

@hook.command()
def submit(chan):
        if chan not in opt_in:
            return
        response = "Submit your picture here!: {} | The password is {}".format(TROLL_DATA[2]. TROLL_DATA[3])
        return response

@hook.command()
def rules(chan):
        if chan not in opt_in:
            return
        response = "Here are our rules: {} | TL:DR Dont be a dick".format(TROLL_DATA[4])
        return response

@hook.command()
def pets(chan):
        if chan not in opt_in:
            return
        response = "Wolf! Meow! Check out all of our awesome pets! They are purrrrfect! {} | Password: {}".format(TROLL_DATA[5], TROLL_DATA[6])
        return response
