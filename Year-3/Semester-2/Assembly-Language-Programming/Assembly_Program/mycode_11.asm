.model small
.stack 100h
s
.code

main proc
   
   
    ; Input first digit
    mov ah, 1
    int 21h
    sub al, 48      ; Convert ASCII to number
    mov bl, al      ; Store in BL
    
    ; Input second digit
    mov ah, 1
    int 21h
    sub al, 48      ; Convert ASCII to number
    mov cl, al      ; Store in CL
    
    ; Multiply BL * CL
    mov al, bl      ; Move first number to AL
    mul cl          ; Multiply with CL (result in AX)
    
    
    ; Convert result to ASCII
    add al, 48      ; Convert back to ASCII
    
    ; Display result
    mov dl, al      ; Move result to DL
    mov ah, 2       ; Display character function
    int 21h
    
    exit:
    mov ah, 4Ch
    int 21h
    
main endp
end main    

     
     
     
;if we want to multipy 10*10 or above

.model small
.stack 100h 
.data
    a dw ?
    b dw ?  
.code

main proc
    mov ax,@data
    mov ds,ax
    
    ; Input first number
    mov ah,1
    int 21h
    sub al,48     ; Convert ASCII to number
    mov bl,al     ; Store in BL
    
    ; Input second number
    mov ah,1
    int 21h
    sub al,48     ; Convert ASCII to number
    mov cl,al     ; Store in CL
    
    ; Multiplication (BL * CL)
    mov al,bl     ; Move first number to AL
    mul cl        ; Multiply with CL (result in AX)
     
     
     
    ; Handle result (now properly displaying product)
    aam           ; Split into digits (AH=tens, AL=units)
    add ax,48  ; Convert both digits to ASCII
    
    ; Display tens digit if needed
    mov dl,ah
    cmp dl,'0'
    je show_units
    mov ah,2
    int 21h
    
show_units:
    ; Display units digit
    mov dl,al
    mov ah,2
    int 21h
    
exit:
    mov ah,4Ch
    int 21h
    
main endp
end main