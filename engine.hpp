#include <iostream>

void loadMem(char mem[]){

    for(int i = 0; i<=8; i++){
        
        mem[i] = '0';

    }

}

void printMem(char mem[]){
    
        for(int i = 0; i<=8; i++){
            
            std::cout << mem[i];
    
        }
    
    }

    void printmem(char l[][8]){

	for(int x = 0; x<32; x++){
	for(int i = 0; i<32; i++){

		cout << l[x][i];

	}
	cout << endl;
}

}

char poke(char l[], char x[][8]){

	int line;

	cout << "Enter the line which you would like to poke data into, from 1 to 32: ";
	cin >> line;
	cin.ignore();
	cout << endl << "Enter a 8 bit string: ";
	cin.getline(l, 8);

	//for(int i = 0; i<32;i++){
		for(int p = 0; p<8; p++){
			x[line-1][p] = l[p];
		}
	//}



}