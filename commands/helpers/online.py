import os

def isOnline() -> bool:
    result = os.system('wget -q --spider http://google.com')
    return result == 0
