#include <iostream>
#include <stack>
using namespace std;

int main() {
  stack<int> S;//<>内に型を指定。
  S.push(7);
  cout << S.size() << endl;
  S.push(1);
  cout << "S.size()" << S.size() << endl;
  cout << "S.top()" << S.top() << endl;
  S.push(2);
  cout << "S.top()" << S.top() << endl;
  S.pop();
  cout << "S.top()" << S.top() << endl;
  S.pop();
  cout << "S.top()" << S.top() << endl;
  cout << "S.isEmpty()" << S.empty() << endl;
  S.pop();
  cout << "S.isEmpty()" << S.empty() << endl;
  return 0;
}
