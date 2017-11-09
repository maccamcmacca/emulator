#include <iostream>
#include "engine.hpp"

using namespace std;

char pok[8];
char reg[8][8];

int main(){

    fillReg(reg);
    loadMem(pok);
    printPoke(pok);
    poke(pok, reg);
    printMem(reg);

}