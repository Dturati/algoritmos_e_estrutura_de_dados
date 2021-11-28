#include <iostream>
using namespace std;

int main() {
  int A [] = {10, 14, 3, 9, 1};
  int menor = 0;
  int aux = 0;
  for (int j = 0; j < 5; j++ ) {
      menor = j;
      for (int k = j; k < 5; k++) {
          if (A[k] < A[menor]) {
            menor = k;
          }
      }
      aux = A[menor];
      A[menor] = A[j];
      A[j] = aux;
  }
  for (int r = 0; r < 5; r++) {
    cout << A[r] << "\n";
  }
  return 0;
}