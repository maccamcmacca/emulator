#include <iostream>
#include <fstream>

using namespace std;

void loadMem(char mem[]){

    for(int i = 0; i<=8; i++){
        
        mem[i] = '0';

    }

}

void printPoke(char mem[]){
    
        for(int i = 0; i<=8; i++){
            
            cout << mem[i];
    
        }
        cout << endl;
    }

    void printMem(char l[][8]){

	for(int x = 0; x<8; x++){
	for(int i = 0; i<8; i++){

		cout << l[x][i];

	}
	cout << endl;
}

}

char poke(char l[], char x[][8]){

	int line;

	cout << "Enter the line which you would like to poke data into, from 1 to 8: ";
	cin >> line;
	cin.ignore();
	cout << endl << "Enter a 8 bit string: ";
	cin.getline(l, 9);

		for(int p = 0; p<8; p++){
			x[line][p] = l[p];
		}
        
}

char load(char memory[8][8]){
  ifstream inputfile("test.txt");
  for(int i = 0; i < 8; i++){
    for(int j = 0; j < 8; j++){
      inputfile >> memory[i][j];
    }
  }
  inputfile.close();
  cout << "File Loaded" << endl;
  return 1;
}

char fillReg(char memory[8][8]){
  for(int i = 0; i < 8; i++){
    for(int j = 0; j < 8; j++){
      memory[i][j] = '0';
    }
  }
}