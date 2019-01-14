#include<iostream>
#include<queue>
using namespace std;

int main(){
	priority_queue<int> PQ;
	PQ.push(2);
	PQ.push(8);
	PQ.push(8);
	cout << PQ.top() << " ";PQ.pop();
	cout << PQ.top() << " ";PQ.pop();
	cout << PQ.top() << " ";PQ.pop();
	return 0;
}
