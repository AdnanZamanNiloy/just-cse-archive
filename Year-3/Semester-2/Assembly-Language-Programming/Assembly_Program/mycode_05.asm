.model small
.stack 100h
.data
a db 'Jump Concept $'            ; String 1 - must end with '$' for AH=9
b db 'Assembly programming $'     ; String 2
c db 'end here$'                  ; String 3

.code
main proc
    mov ax, @data      ; Load address of data segment
    mov ds, ax         ; Initialize DS with data segment address
    
    ; ----- Print first string -----
    mov ah, 9          ; DOS print-string function
    lea dx, a          ; Load offset of string a into DX
    int 21h            ; Call DOS interrupt to print string
    
    ; ----- Print newline -----
    mov ah, 2          ; DOS print-character function
    mov dl, 10         ; Line Feed (LF)
    int 21h
    mov dl, 13         ; Carriage Return (CR)
    int 21h
    
level1:
    ; ----- Print second string -----
    mov ah, 9          ; DOS print-string function
    lea dx, b          ; Load offset of string b into DX
    int 21h
    jmp level2         ; Jump to level2 label
    
level2:
    ; ----- Print third string -----
    mov ah, 9          ; DOS print-string function
    lea dx, c          ; Load offset of string c into DX
    int 21h 
    jmp exit           ; Jump to exit label
    
exit:
    mov ah, 4Ch        ; DOS terminate program function
    int 21h            ; Exit to DOS
main endp
end main
