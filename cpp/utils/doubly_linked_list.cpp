#include <iostream>
#include <list>
using namespace std;

int main() {
  list<string> L;

  L.push_front("ASAKO");//O(1)
  cout << L.size() << endl;
  cout << L.front() << endl;
  cout << L.back() << endl;
  L.push_front("ASAKO1");//O(1)
  L.push_back("ASAKO2");//O(1)
  cout << L.size() << endl;
  cout << L.front() << endl;
  cout << L.back() << endl;
}
