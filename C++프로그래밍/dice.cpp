#include <iostream>
#include <cstdlib>
using namespace std;

int main(int argc, char *argv[]){
// 배열의 크기, 배열
  if (argc != 2){
    cout << "usage: ./dice n\n";
    return -1;
  }
  int n = atoi(argv[argc-1]);
  srand(n);
  for(int i=0; i<10; i++){
    int dice = rand()%6 + 1;
    cout << dice << " ";
  }
  cout << endl;
}
