#include<iostream>
#include<set>
using namespace std;

void print(set<int> S) {
  cout << S.size() << ":";
  for(set<int>::iterator it = S.begin(); it != S.end(); it++){
    cout << " "  << *it;
  }
  cout << endl;
}

int main() {
  set<int> S;

  S.insert(8);
  S.insert(1);
  print(S);
  cout << (S.find(2) == S.end()) << endl;//return it
  S.insert(2);
  print(S);
  cout << (S.find(2) == S.end()) << endl;
  return 0;
}
