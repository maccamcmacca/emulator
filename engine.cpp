#include <iostream>
#include "engine.hpp"

using namespace std;

char poke[8];
char reg[8][8];

int main(){

    loadMem(poke);
    printMem(poke);

}