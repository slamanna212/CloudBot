import os
import time
import platform
from datetime import timedelta

try:
    import psutil
except ImportError:
    psutil = None

from cloudbot import hook
from cloudbot.util.filesize import size as format_bytes
import cloudbot


@hook.command(autohelp=False)
def about(text, conn):
    """-- Gives information about CloudBot. Use .about license for licensing information"""
    if text.lower() in ("license", "gpl", "source"):
        return "CloudBot Refresh is released under the GPL v3 license, get the source code " \
               "at https://github.com/slamanna212/CloudBot/"

    return "{} is powered by CloudBot Refresh! ({}) - " \
           "https://github.com/CloudBotIRC/CloudBot/".format(conn.nick, cloudbot.__version__)
