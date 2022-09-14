import os
import helpers.online

def printHelp() -> None:
    print('[usage]')
    print('    copyRomsFromCloud  - copies your ROMs from your cloud storage')
    print('    copySavesFromCloud - copies your saves from your cloud storage')
    print('    copySavesToCloud   - copies your saves to your cloud storage')

def copyRomsFromCloud() -> None:
    if not helpers.online.isOnline():
        return

    os.system('rclone sync roms:"/ROMS" /home/pi/RetroPie/roms/')

def copySavesFromCloud() -> None:
    if not helpers.online.isOnline():
        return

    os.system('rclone sync roms:"/ROM Saves" /home/pi/saves')

def copySavesToCloud() -> None:
    if not helpers.online.isOnline():
        return

    os.system('rclone sync /home/pi/saves roms:"/ROM Saves"')

