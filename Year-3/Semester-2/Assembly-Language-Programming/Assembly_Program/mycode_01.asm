.model small
.stack 100h
.data
msg  db 5      ; number
msg1 db ?      ; will store a character
.code

main proc
    mov ax, @data
    mov ds, ax
    
    ; Convert number in msg to ASCII
    add byte ptr msg, 48   ; 5 -> '5'
    
    mov ah, 2
    mov dl, msg            ; Load value at msg into DL
    int 21h                ; Print it
    
    ; Read a character
    mov ah, 1
    int 21h
    mov msg1, al           ; Store it in msg1
    
    mov ah, 2     ; DOS function to display a single character
    mov dl, 10    ; LF = move down one line
    int 21h 
    mov dl, 13    ; CR = return to column 1
    int 21h
    
    ; Print stored character
    mov ah, 2
    mov dl, msg1
    int 21h
    
exit:
    mov ah, 4Ch
    int 21h
main endp
end main


