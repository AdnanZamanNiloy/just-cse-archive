.model small
.stack 100h
.code
main proc     

    ; Input 1
    mov ah,1
    int 21h
    sub al,48         ; Convert ASCII to number
    mov bl,al
     
    ; Print newline
    mov ah,2
    mov dl,10
    int 21h
    mov dl,13
    int 21h
    
    ; Input 2
    mov ah,1
    int 21h
    sub al,48
    mov cl,al
    
    ; Print newline
    mov ah,2
    mov dl,10
    int 21h
    mov dl,13
    int 21h
    
    ; Addition
    mov al,bl       ;Transfer bl to al
    add al,cl
    add al,48         ; Convert to ASCII
    mov ah,2
    mov dl,al
    int 21h
    
    ; Print newline
    mov ah,2
    mov dl,10
    int 21h
    mov dl,13
    int 21h
    
    ; Subtraction
    mov al,bl
    sub al,cl
    add al,48
    mov ah,2
    mov dl,al
    int 21h
    
    
    ; Exit
    mov ah,4Ch
    int 21h
main endp
end main
