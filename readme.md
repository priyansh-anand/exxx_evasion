# EXXX EVASION!
**DO NOT UPLOAD TO [VIRUSTOTAL.COM](https://virustotal.com) INSTEAD USE [NODISTRIBUTE.COM](https://nodistribute.com)**
```

 /$$$$$$$$ /$$   /$$ /$$   /$$ /$$   /$$       /$$$$$$$$ /$$    /$$  /$$$$$$   /$$$$$$  /$$$$$$  /$$$$$$  /$$   /$$
| $$_____/| $$  / $$| $$  / $$| $$  / $$      | $$_____/| $$   | $$ /$$__  $$ /$$__  $$|_  $$_/ /$$__  $$| $$$ | $$
| $$      |  $$/ $$/|  $$/ $$/|  $$/ $$/      | $$      | $$   | $$| $$  \ $$| $$  \__/  | $$  | $$  \ $$| $$$$| $$
| $$$$$    \  $$$$/  \  $$$$/  \  $$$$/       | $$$$$   |  $$ / $$/| $$$$$$$$|  $$$$$$   | $$  | $$  | $$| $$ $$ $$
| $$__/     >$$  $$   >$$  $$   >$$  $$       | $$__/    \  $$ $$/ | $$__  $$ \____  $$  | $$  | $$  | $$| $$  $$$$
| $$       /$$/\  $$ /$$/\  $$ /$$/\  $$      | $$        \  $$$/  | $$  | $$ /$$  \ $$  | $$  | $$  | $$| $$\  $$$
| $$$$$$$$| $$  \ $$| $$  \ $$| $$  \ $$      | $$$$$$$$   \  $/   | $$  | $$|  $$$$$$/ /$$$$$$|  $$$$$$/| $$ \  $$
|________/|__/  |__/|__/  |__/|__/  |__/      |________/    \_/    |__/  |__/ \______/ |______/ \______/ |__/  \__/
                                                                                                                   
                                                                                                                   
                                                                                                                   
            ##########################################################################################
            ######## WARNING : DO NOT TEST THIS EXECUTABLE ON ANY COMPUTER THAT YOU DON'T OWN ########
            ##########################################################################################

```
Generating fully undetectable meterpreter custom payloads using msfvenom and custom loader template. It bypasses the latest Windows Defender running on Windows 10 Pro 1903 ( Build 18363.693 ) with all updates available till 16th of March, 2020.

# Requirements
> * Python 3
> * msfvenom
> * x86_64-w64-mingw32-g++ or g++ ( MinGW G++ Compiler for windows )
> * x86_64-w64-mingw32-windres or windres ( Component of with MinGW )
> * pip3 termcolor

# Installation
Execute these commands on your terminal. If installation fails, try using sudo.
```bash
$ git clone https://github.com/priyansh-anand/exxx_evasion.git
$ cd exxx_evasion
$ chmod +x setup
$ ./setup
// Now you can delete this folder
```
# Usage
```bash
$ exxx_evasion
```
It will show required info after every step

# Features
There are 2 modules in this tool:
* Undetectable Reverse Shell
	* Doesn't requires Admin Priviledges to run
	* Bypassess all antiviruses including Windows Defender
	* Just an undetectable meterpreter reverse_shell
	* Migrates automatically to explorer.exe just after running
	* Limitations : Triggers Windows Defender if 'getsystem' is executed using meterpreter, however the meterpreter session is not lost and the payload exe file is not detected
* Persistent Advanced Reverse Shell
	* Requires Admin Priviledges to run
	* Bypassess all antiviruses including Windows Defender
	* Disables Windows Defender permanently using registry ( Can't be turned on without changing registry )
	* Adds all the disk and drives to Defender exclusion list
	* Runs the meterpreter shell as SYSTEM and add it to startup
	* Can execute your custom commands before launching payload ( see main.py )
	* All features and limitataion of the 1st module

# TODO
* Add support for embedding payloads in other exe
* Add support for adding icons and digital certificates ( spoofed ) to payloads
* Make all payloads persistent by default
# License
MIT

**Free Software, Hell Yeah!**

# Warning
This tool is for educational purposes only. I am not responsible if you do any illegal act using this tool. Use it wisely.
# Contribution
If you want to add any new feature or fix any bug, I welcome you to do that. You can also request/suggest for more awesome features to be added in this tool