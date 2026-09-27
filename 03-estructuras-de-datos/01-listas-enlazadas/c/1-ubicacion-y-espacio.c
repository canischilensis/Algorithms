#include <stdio.h>

int main(){
    
    int myVal = 13;

    printf("Value of integer 'myVal': %d\n", myVal);
    printf("Size of integer 'myVal': %lu bytes\n", (unsigned long) sizeof(myVal));// 4 bytes
    printf("Address to 'myVal': %p\n", (void*)&myVal); //&myVal → 0x7ffca3b8
    // (void*)&myVal: Convierte esa dirección a puntero genérico para imprimirla correctamente.
    printf("Size of the address to 'myVal': %lu bytes\n", (unsigned long) sizeof(&myVal)); // 8 bytes

return 0;
}