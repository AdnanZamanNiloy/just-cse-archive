.model small
.stack 100h
.data
.code

main proc
    mov ax, @data
    mov ds, ax
    
    ;Input first digit
    mov ah, 1
    int 21h
    sub al, 48      ; Convert ASCII to number
    mov bl, al      ; Store in BL
    
    ; Input second digit
    mov ah, 1
    int 21h
    sub al, 48      ; Convert ASCII to number
    mov cl, al      ; Store in CL
    
    ; Division BL / CL 
    mov al, bl      ; First number into AL
    mov ah, 0       ; Clear AH for 8-bit division
    div cl          ; AL ÷ CL ? AL=quotient, AH=remainder
    
    ;Convert quotient to ASCII 
    add al, 48      ; Convert number to ASCII
    
    ; Display quotient
    mov dl, al
    mov ah, 2
    int 21h
    
    ; Exit program
    mov ah, 4Ch
    int 21h
    
main endp
end main
