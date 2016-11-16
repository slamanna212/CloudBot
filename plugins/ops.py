#opdb: opdb[nick] = pushbulletApiToken; if pushbulletApiToken = "none", message sent through /msg command
#lastops: lastops[nick] = datetime; Last datetime that user used that command. Used to rate limit sort of. This could be done better
#pingops permission: "users": ["*!*@*"]; I assume there's a way to ignore users who overuse the command, but I'm not 100% sure how.

@asyncio.coroutine
@hook.command("ops", permissions=["pingops"], autohelp=False)
def pingops(text, nick, chan):
    """Alerts the ops that something is amiss. Optional, include a message to be passed along."""

    global opdb, lastops

    parts = text.lower().split()
    now = datetime.now()
    pingwent = False
    sendping = False
    if nick in lastops:
        lastop = lastops[nick]
        if (now - lastop).total_seconds() < 30:
            lastop[nick] = now
            timeleft = 30 - (now - lastop).total_seconds()
            sendmessage(chan, "Chill out " + nick + ", we're getting to it. Wait at least %.0fs to whine more." % timeleft)
        else:
            sendping = True
    else:
        lastops[nick] = now
        sendping = True
    if sendping:
        pushbulleturl = "https://api.pushbullet.com/v2/pushes"
        message = "An OP has been requested in IRC by " + str(nick)
        if len(parts) > 0:
            message += ": " + str(text)
        for op, pushbullet in opdb.items():
            headers = {"Access-Token": pushbullet}
            data = {"type": "note", "title": "OP requested from IRC",
                    "body": message}
            if pushbullet != "none":
                resp = requests.post(pushbulleturl, data=data, headers=headers)
                if resp.status_code == 200:
                    pingwent = True
                else:
                    errorcode = ''.join(
                        random.SystemRandom().choice(string.ascii_uppercase + string.digits) for _ in range(5))
                    print("ERR: " + str(errorcode) + str(resp.text))
            else:
                pingwent = True
            sendmessage(op, message)
        if pingwent:
            sendmessage(nick, "OPs have been paged.")
