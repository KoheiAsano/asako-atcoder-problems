#include <iostream>
#include <queue>
#include <string>

using namespace std;

int main() {
  queue<string> que;
  que.push("ASAKO");
  cout << "que.front()="<< que.front() << endl;
  que.push("ASAKO1");
  que.pop();
  cout << "que.front()="<< que.front() << endl;
  cout << "que.empty()=" << que.empty() << endl;
  que.pop();
  cout << "que.empty()=" << que.empty() << endl;
}
