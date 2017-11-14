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

int bintoDec(int num){
    int rem;
 
    if (num <= 1){
        cout << num;
        return num;
    }
    rem = num % 2;
    bintoDec(num / 2);
    //num = num;
    cout << rem;
}
/*THIS IS A TEMPORARY PLACEHOLDER FOR THIS WHILE I PISS ABOUT WITH THE MAIN FUNCTION
//THIS ONLY EXISTS TO NOT CLUTTER UP MAIN ATM
void run(){

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
*/