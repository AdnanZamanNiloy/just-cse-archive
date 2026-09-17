.model small
.stack 100h
.data
    msg db 'Enter lowercase letter: $' 
    msg2 db 'Enter uppercase letter: $'
    newline db 0Dh,0Ah,'$'  ; newline for formatting
.code
main proc
    mov ax,@data
    mov ds,ax
    
    
    
    ; Print lowercase prompt
    mov ah,9
    lea dx,msg
    int 21h

    ; Read lowercase character
    mov ah,1
    int 21h
    mov bl,al       ; store input in BL

    ; Convert to uppercase
    sub bl,32       

    ; Print newline
    mov ah,9
    lea dx,newline
    int 21h



    ; Print uppercase prompt
    mov ah,9
    lea dx,msg2
    int 21h

    ; Read uppercase character
    mov ah,1
    int 21h
    mov cl,al 

    ; Convert to lowercase
    add cl,32  

    ; Print newline
    mov ah,2
    mov dl,10
    int 21h
    mov dl,13
    int 21h  
     
     
     
     
     
    ; Print uppercase
    mov ah,2
    mov dl,bl
    int 21h    

    ; Print lowercase
    mov ah,2
    mov dl,cl
    int 21h

    ; Exit
    mov ah, 4Ch
    int 21h
main endp
end main
