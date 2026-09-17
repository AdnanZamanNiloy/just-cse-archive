.model small
.stack 100h
.data
    num1 dw 5
    num2 dw 3
    num3 dw 1
    sum  dw ?           ; to store result

.code
main proc
    mov ax, @data
    mov ds, ax

    ; add three numbers
    mov ax, num1
    add ax, num2
    add ax, num3
    mov sum, ax

    ; convert result to ASCII (only works for single-digit)
    mov ax, sum
    add al, 48
    mov dl, al

    ; display result
    mov ah, 2
    int 21h

    ; exit program
    mov ah, 4Ch
    int 21h
main endp
end main
