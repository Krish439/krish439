import os
import sys


async def reload_LEGENDBOT():
    executable = sys.executable.replace(" ", "\\ ")
    args = [executable, "-m", "userbot"]
    os.execle(executable, *args, os.environ)
    os._exit(143)
