#include <iostream>
#include "engine.hpp"

using namespace std;

string pok[8];
char reg[8][8];
int counter;
int bin = 8;

int main(){

loadPok(pok, "testforprogram.txt");

load(reg, "testforprogram.txt");
printPoke(pok);

}