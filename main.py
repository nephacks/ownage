global lock_active  # inserted
import discord
import os
import ctypes
import asyncio
import pyuac
import subprocess

# this is my token hope nothing happens to it :slight_smile:
TOKEN = 'MTMxMDU5MDIxMDg4NjcyOTczOQ.GAAmxz.mZpqwx-HunPs4bQglTonlAMvZXNIVkLzaNrkg8'

def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()!= 0
    except:
        return False
