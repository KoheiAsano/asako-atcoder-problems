#include <iostream>
#include <string>
#include <cmath>
#include <utility>
using namespace std;
int N;

struct BigInt{
  unsigned int first, second;
  BigInt *next;
};

BigInt addition(BigInt a, BigInt b){
	BigInt res;
	unsigned int carry = 0, under_sum = a.first + b.first;
	if(under_sum > 1000000000){
		carry += under_sum/1000000000;
		under_sum %= 1000000000;
	}
	res.first = under_sum;
	res.second = a.second + b.second + carry;
	return res;
}

int main(){
	unsigned int a = pow(10, 9)-1;
	BigInt A, B;
	A.first = a;
	B.first = a;
	BigInt ans = addition(A, B);
	cout << ans.second << ans.first << endl;
  cout << pow(10, 9)-1 << pow(10, 9)-1 << endl;
}
