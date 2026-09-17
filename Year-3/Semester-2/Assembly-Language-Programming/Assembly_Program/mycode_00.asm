.model small
.stack 100h
.code

main proc
    ; Read first character
    mov ah,1
    int 21h
    mov bl,al

    ; Read second character
    mov ah,1
    int 21h
    mov bh,al

    ; Display first character
    mov ah,2
    mov dl,bl
    int 21h

    ; Display second character
    mov ah,2
    mov dl,bh
    int 21h

exit:
    mov ah,4ch
    int 21h
main endp
end main
