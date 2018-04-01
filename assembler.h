#include <stdio.h>
#include <stdlib.h>

typedef struct memory{

    int memory[31][31];
    int current[31];
    int acc, opcode, operand;


}memory;


//prints the memory
void debug(memory* mem){

    /* for(int i = 0; i < 32; i++){
        printf("%d", mem->current[i]);
    } */
    printf("\n\n");
    for(int j = 0; j<=31; j++){
        for(int i = 0; i<=31; i++){
            printf("%d", mem->memory[j][i]);
        }
        printf("\n");
    }
    printf("\n");
}

char* loadToArray(char *fileName, memory* mem){

 FILE *file = fopen(fileName, "r");
    char *code;
    size_t n = 0;
    int c;

    if (file == NULL)
        return NULL; //could not open file

    code = malloc(10000);

    while ((c = fgetc(file)) != EOF)
    {
        code[n++] = (char) c;
    }
    
    int d = 0;

    for(int j = 0; j<=32; j++){
        for(int i = 0; i<=32; i++){
            
            if(code[d] == '1'){
                mem->memory[j][i] = 1;
            }
            else if(code[d] == '0'){
                mem->memory[j][i] = 0;
            }
            d++;
        }
         for(int n = 0; n<32; n++){
        mem->current[n] = mem->memory[j][n]  ; 
        } 
    }

    for(int i = 0; i<1000; i++){
        printf("%c", code[i]);
    }
    printf("\n");
    // don't forget to terminate with the null character
    code[n] = '\0';        

    return code;

}

void fetch(memory* mem){



}

void decode(memory* mem){



}

void execute(memory* mem){



}