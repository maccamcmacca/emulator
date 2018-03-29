#include <stdio.h>
#include <stdlib.h>
#include "assembler.h"

int main(){

memory* mem = (memory*) calloc(2, sizeof(memory));

loadToArray("assem.txt", mem);
debug(mem);

return 0;
}