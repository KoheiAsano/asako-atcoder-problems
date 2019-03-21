#include <bits/stdc++.h>
using namespace std;

struct C {char s, value;};

void swap(C& a, C& b){
	C tmp = a;
	a = b;
	b = tmp;
}

int main(){
	int N;cin >> N;
	C a[N],b[N];
	for(int i=0;i<N;i++){
		cin >> a[i].s >> a[i].value;
    b[i] = a[i];
	}
	for(int i=0;i<N;i++){
		for(int j=N-1;j>i;j--){
			if(a[j-1].value>a[j].value){
				swap(a[j-1],a[j]);
			}
		}
	}
	for(int i=0;i<N;i++){
		if(i == N-1) {
			cout << a[i].s << a[i].value << endl;
		}else {
			cout << a[i].s << a[i].value << " ";
		}
	}
	cout << "Stable" << endl;
	for(int i=0;i<N;i++){
    int minid = i;
		for(int j=i;j<N;j++){
			if(b[minid].value>b[j].value){
        minid = j;
			}
		}
    if(minid != i){
      swap(b[i],b[minid]);
    }
	}
	int stable = true;
	for(int i=0;i<N;i++){
		if(a[i].s != b[i].s) stable = false;
		if(i == N-1) {
			cout << b[i].s << b[i].value << endl;
		}else {
			cout << b[i].s << b[i].value << " ";
		}
	}
	if(stable) cout << "Stable" << endl;
	else cout << "Not stable" << endl;
	return 0;
}
