#include <iostream>
using namespace std;

int main() {
  int cards [] = {5, 2, 4, 6, 1, 3};
  int key = 0;
  int i = 0;

  for (int j=1; j <= 5; j++) {
    key = cards[j];
    i = j-1;

    while(i > -1 && cards[i] > key) {
      cards[i+1] = cards[i];
      i = i -1;
    }
    cards[i+1] = key;
   }

   for (int k = 0; k <= 5; k++) {
     cout << cards[k] << "\n";
   }

  return 0;
}