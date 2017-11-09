#include <iostream>

void loadMem(int mem[]){

    for(int i = 0; i<=8; i++){
        
        mem[i] = 0;

    }

}

void printMem(int mem[]){
    
        for(int i = 0; i<=8; i++){
            
            std::cout << mem[i];
    
        }
    
    }