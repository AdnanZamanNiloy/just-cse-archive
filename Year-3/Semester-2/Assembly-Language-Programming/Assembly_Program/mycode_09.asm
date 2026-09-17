.model small
.stack 100h
.data
    a db 'Enter two numbers: $'
    b db 10,13, 'Largest Number is: $'
.code

main proc
    mov ax, @data      ; Load data segment
    mov ds, ax

    ; Show "Enter two numbers"
    mov ah, 9
    lea dx, a
    int 21h

    ; Read first number
    mov ah, 1
    int 21h
    mov bl, al         ; Store in BL

    ; Read second number
    mov ah, 1
    int 21h
    mov cl, al         ; Store in CL

    ; Compare numbers
    cmp bl, cl
    jg level1          ; If BL > CL ? go to level1
    jmp level2         ; Else ? go to level2



level1:
    mov ah, 9
    lea dx, b
    int 21h  
    
    
    mov ah, 2          ; Print single character
    mov dl, bl
    int 21h
    jmp exit

level2:
    mov ah, 9
    lea dx, b
    int 21h  
    
    
    mov ah, 2          ; Print single character
    mov dl, cl
    int 21h

exit:
    mov ah, 4Ch
    int 21h

main endp
end main
