.model small
.stack 100h
.code

main proc
    
    ; Input three characters
    mov ah,1
    int 21h
    mov bl,al    ; first in bl
    int 21h
    mov cl,al    ; second in cl
    int 21h
    mov dh,al    ; third in dh        
    
    
    
    ; Compare bl and cl (biggest check)
    cmp bl,cl
    jge a        ; if bl >= cl, check bl vs dh
    
    ; bl < cl case
    cmp cl,dh    ; now compare cl vs dh (biggest)
    jge c        ; if cl >= dh, cl is biggest
    
    ; dh is biggest (since cl < dh)
    mov ah,2
    mov dl,dh
    int 21h   
    jmp exit
    
    c:  ; cl is bigger than dh
    mov ah,2
    mov dl,cl
    int 21h
    jmp exit 
    
    a:  ; bl >= cl
    cmp bl,dh    ; compare bl vs dh (biggest)
    jge d        ; if bl >= dh, bl is biggest
    
    ; dh is biggest (since bl < dh)
    mov ah,2
    mov dl,dh
    int 21h
    jmp exit
    
    d:  ; bl is biggest
    mov ah,2
    mov dl,bl
    int 21h
    jmp exit
    
    exit:
    mov ah,4Ch
    int 21h
    
main endp
end main