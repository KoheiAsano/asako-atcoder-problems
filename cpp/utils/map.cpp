#include<iostream>
#include<map>
#include<string>
using namespace std;

void print(map<string,int> T) {
  map<string, int>::iterator it;
  cout << T.size() << endl;
  for( it = T.begin(); it != T.end(); it++) {
    pair<string, int> item = *it;
    cout << item.first << "==>" << item.second << endl;
  }
}

int main() {
  map<string, int> T;
  T["red"] = 32;
  print(T);

  T.insert(make_pair("asako", 1));
  print(T);
  pair<string, int> target = *T.find("asako");
  cout << target.first << "==>" << target.second << endl;
  return 0;
}
