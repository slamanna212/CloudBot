from cloudbot import hook


supsonface = u'(\u00AF\u005C\u005F\u0028\u30C4\u0029\u005F\u002F\u00AF)'


@hook.command(autohelp=False)
def supson(message, conn):
    """the sup son face"""
    message(supsonface)
	
# 0x30C4 is the face
# ¯\_(ツ)_/¯