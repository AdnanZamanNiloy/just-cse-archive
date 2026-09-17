.model small
.stack 100h
.data
msg db 'i love coding $'
.code

main proc
    mov ax, @data
    mov ds, ax

    mov ah, 9
    lea dx, msg
    int 21h  
     
     
    ;print newline(LF+CR) 
    mov ah,2
    mov dl,10
    int 21h
    mov dl,13
    int 21h

    ; Read a character
    mov ah, 1
    int 21h
    mov bl, al

    ; Print newline (LF + CR)
    mov ah, 2
    mov dl, 10     ; LF
    int 21h
    mov dl, 13     ; CR
    int 21h

    ; Print stored character
    mov ah, 2
    mov dl, bl
    int 21h 
    
     
    ; beep sound  
    mov ah,2
    mov dl,07
    int 21h

exit:
    mov ah, 4Ch
    int 21h
main endp
end main
