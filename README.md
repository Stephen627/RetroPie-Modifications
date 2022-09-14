# RetroPie Modifications

## Dependencies
- [rclone](https://rclone.org/) with a drive setup called "roms"

## Build Dependencies
- [pyinstaller](https://github.com/pyinstaller/pyinstaller)

## Added Functionality
- On emulation station start up, download all roms with "roms" drive
- On game close, upload save data to "roms" drive
- On retropie option "Download cloud ROM saves", download save data from "roms" drive

## How to Install

## Road Map
- Keep a record of all game metadata and store that with the roms on the "roms" drive. This will include the name, description, release date, etc. and the image itself.
- If the device currently doesn't have an internet connection when uploading the saves, it doesn't do anything. I want it to instead mark a flag and check for that flag on a number of different events
- Convert scripts from bash to c
- Make easy install script that walks you through the entire setup process including setting up the "roms" drive
- Create script to change input from lcd screen to external hdmi screen on button hold
