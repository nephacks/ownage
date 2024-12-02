global lock_active  # inserted
import discord
import os
import ctypes
import asyncio
import pyuac
import subprocess

# this is my token hope nothing happens to it :slight_smile:
TOKEN = 'MTMxMDU5MDIxMDg4NjcyOTczOQ.G7vGrv.u5mdn82Phe9RzJh17nvq-teyr3bPXiAoWttK3c'

def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()!= 0
    except:
        return False
