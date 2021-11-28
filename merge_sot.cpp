#include <iostream>
using namespace std;

int merge_sort(int * A, int p, int q, int r) {

  int n1 = q - p + 1; 
  int n2 = r - q;
  int L1[n1] = {};
  int L2[n2] = {};
  cout << n1 << endl;
  cout << n2 << endl;

  for (int i=0; i < n1; i++) {
      L1[i] = A[p+i-1];
  }

  for (int j = 0; j < n2; j++) {
    L2[j] = A[q+j];
  }

  cout << endl;
  for (int i=0; i < n1; i++) {
      cout << L1[i] << endl;
  }

  cout << endl;
  for (int j=0; j < n2; j++) {
      cout << L2[j] << endl;
  }


  return 1;
}

int main() {
  int A[] = {6, 5, 4, 3, 2, 1};
  merge_sort(A,0,2,5);
  return 0;
}