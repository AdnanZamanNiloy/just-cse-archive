.model small
.stack 100h
.code
main proc
    mov ax,@data
    mov ds,ax        ; Initialize data segment (if needed)

    ; ----- Input first number -----
    mov ah,1
    int 21h
    sub al,48
    mov bl,al        ; Store first number in BL

    ; ----- Input second number -----
    mov ah,1
    int 21h
    sub al,48
    mov bh,al        ; Store second number in BH

    ; ----- Input third number -----
    mov ah,1
    int 21h
    sub al,48
    mov cl,al        ; Store third number in CL

    ; ----- Input fourth number -----
    mov ah,1
    int 21h
    sub al,48
    mov dl,al        ; Store fourth number in DL

    ; ----- Add numbers -----
    mov al, bl
    add al, bh
    add al, cl
    add al, dl       ; AL now has sum

    ; ----- Convert sum to ASCII -----
    add al,48

    ; ----- Print result -----
    mov ah,2
    mov dl,al
    int 21h

    ; ----- Exit program -----
    mov ah,4Ch
    int 21h

main endp
end main
