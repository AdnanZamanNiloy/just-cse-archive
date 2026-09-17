.model small
.stack 100h
.data
    num1 db 00000101b   ; 5 in binary
    num2 db 00000011b   ; 3 in binary

    msg1 db 'AND Result: $'
    msg2 db 0Dh,0Ah, 'OR  Result: $'
    msg3 db 0Dh,0Ah, 'XOR Result: $'

.code
main proc
    mov ax, @data
    mov ds, ax

    ; ---------- AND Operation ----------
    mov al, num1
    and al, num2         ; AL = num1 AND num2
    mov bl, al           ; store result
   
    mov ah, 9
    lea dx, msg1
    int 21h
    add bl, '0'          ; convert to ASCII
    
    mov ah, 2
    mov dl, bl
    int 21h

    ; ---------- OR Operation ----------
    mov al, num1
    or  al, num2         ; AL = num1 OR num2
    mov bl, al
    
    mov ah, 9
    lea dx, msg2
    int 21h
    add bl, '0'
   
    mov ah, 2
    mov dl, bl
    int 21h

    ; ---------- XOR Operation ----------
    mov al, num1
    xor al, num2         ; AL = num1 XOR num2
    mov bl, al
    
    mov ah, 9
    lea dx, msg3
    int 21h
    add bl, '0'
   
    mov ah, 2
    mov dl, bl
    int 21h

    ; Exit program
    mov ah, 4Ch
    int 21h
main endp
end main
