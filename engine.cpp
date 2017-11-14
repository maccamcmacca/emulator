#include <iostream>
#include "engine.hpp"

using namespace std;

char pok[8];
char reg[8][8];
int counter;
int bin = 8;

int main(){

    for(int i = 0; i<8; i++){
         for(int j = 0; j<8; j++){
            if(reg[i][1] == '0' && reg[i][2] == '0' && reg[i][3] == '0'){
                counter = bin;    
            }

            if(reg[i][1] == '1' && reg[i][2] == '0' && reg[i][3] == '0'){
                counter = bin;    
            }

            if(reg[i][1] == '1' && reg[i][2] == '1' && reg[i][3] == '0'){
                counter = bin;    
            }

            if(reg[i][1] == '0' && reg[i][2] == '0' && reg[i][3] == '1'){
                counter = bin;    
            }

            if(reg[i][1] == '0' && reg[i][2] == '1' && reg[i][3] == '1'){
                counter = bin;    
            }

            if(reg[i][1] == '1' && reg[i][2] == '1' && reg[i][3] == '1'){
                counter = bin;    
            }

            if(reg[i][1] == '1' && reg[i][2] == '0' && reg[i][3] == '1'){
                counter = bin;    
            }

            if(reg[i][1] == '0' && reg[i][2] == '1' && reg[i][3] == '0'){
                counter = bin;    
            }

        }
    }

}

