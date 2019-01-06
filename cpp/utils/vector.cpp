#include <bits/stdc++.h>
using namespace std;

void print(vector<double> V) {
  for(int i=0;i<V.size();i++){
    cout << V[i] << " ";
  }
  cout << endl;
}

void printByIt(vector<double> V) {
  vector<double>::iterator it;
  for(it = V.begin();it != V.end();it++){
    cout << *it << " ";
  }
  cout << endl;
}


int main() {
  vector<double> S;
  int n = 5;
  for (int i = 0;i < 5; i++) {
    S.push_back(i);
  }
  print(S);
  printByIt(S);
  cout << S.size() << endl;
  S.insert(S.begin() + 4,9);//O(n)
  print(S);
  S.erase(S.begin() + 1);//O(n)
  print(S);
}
