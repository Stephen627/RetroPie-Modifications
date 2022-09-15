import os
import helpers.online
from pathlib import Path

flagLocation: str = str(Path.home()) + '/cloud-save-flag'

def add_args(subparsers) -> None:
    namespace_parser = subparsers.add_parser(
        'cloud',
        help='Interact with your ROMs and Saves on your cloud account'
    )

    command_subparser = namespace_parser.add_subparsers(
        title='Commands'
    )

    command_subparser.add_parser(
        'copy-roms-from-cloud',
        help='copies your ROMs from your cloud storage',
    ).set_defaults(func=copy_roms_from_cloud)

    command_subparser.add_parser(
        'copy-saves-from-cloud',
        help='copies your saves from your cloud storage',
    ).set_defaults(func=copy_saves_from_cloud)

    copy_to_cloud_parser = command_subparser.add_parser(
        'copy-saves-to-cloud',
        help='copies your saves to your cloud storage',
    )
    copy_to_cloud_parser.set_defaults(func=copy_saves_to_cloud)
    copy_to_cloud_parser.add_argument('-f', '--flag', help='Flag required to upload the saves', action='store_true')


def copy_roms_from_cloud(args) -> None:
    if not helpers.online.isOnline():
        return

    os.system('rclone sync roms:"/ROMS" /home/pi/RetroPie/roms/')

def copy_saves_from_cloud(args) -> None:
    if not helpers.online.isOnline():
        return

    os.system('rclone sync roms:"/ROM Saves" /home/pi/saves')

def copy_saves_to_cloud(args) -> None:
    if not helpers.online.isOnline():
        Path(flagLocation).touch()
        return

    send_data = 0
    if args.flag:
        if Path(flagLocation).is_file():
            send_data = 1
    else:
        send_data = 1
    
    if send_data:
        os.system('rclone sync /home/pi/saves roms:"/ROM Saves"')
        if Path(flagLocation).is_file():
            Path(flagLocation).unlink()

