// #include <bits/stdc++.h>
// using namespace std;
// #define ARRAY_LENGTH(array) (sizeof(array) / sizeof(array[0]))
// #define MAX(arr) *max_element(arr, arr + ARRAY_LENGTH(arr))
// #define MAXID(arr) distance(arr,max_element(arr, arr + ARRAY_LENGTH(arr)))
//
// int N;
// int ev[10006], ov[10006];
// int ob[10006]={0}, eb[10006]={0};
// int ans, omost, emost, otmp, etmp;
// int main(){
// 	cin >> N;
//
// 	for(int i=0;i<N;i++){
// 		if(i%2==0){
// 			cin >> ev[i];
// 			eb[ev[i]]++;
// 		}
// 		else {
// 			cin >> ov[i];
// 			ob[ov[i]]++;
// 		}
// 	}
// 	omost= MAXID(ob);
// 	emost= MAXID(eb);
// 	if (omost!=emost){
// 		ans = N-MAX(ob)-MAX(eb);
// 		cout << N-MAX(ob)-MAX(eb) << endl;
// 	}
// 	else{
// 		otmp = MAX(ob);
// 		etmp = MAX(eb);
// 		ob[omost]=0;eb[emost]=0;
// 		ans = min(N-MAX(ob)-etmp,N-MAX(eb)-otmp);
// 		cout << ans << endl;
// 	}
// 	return 0;
// }
#include <iostream>
#include <algorithm>

#define N_MAX 100000

using namespace std;

int main(){
    int n;
    int odd[N_MAX+1] = {0};
    int even[N_MAX+1] = {0};
    int max_even = 2;
    int max_odd = 1;
    cin >> n;
    for(int i = 0; i < n; i++){
        int v;
        cin >> v;
        if(i%2 == 0)odd[v]++;
        else even[v]++;
    }
    for(int i = 1; i <= N_MAX; i++){
        if(even[i] > even[max_even]) max_even = i;
        if(odd[i] > odd[max_odd]) max_odd = i;
    }
    if(max_even != max_odd){
        cout << n - even[max_even] - odd[max_odd] << endl;
    }else{
        sort(odd, odd+N_MAX+1, greater<int>());
        sort(even, even+N_MAX+1, greater<int>());
        int tmp = max(even[0]+odd[1], even[1]+odd[0]);
        cout << n - tmp << endl;
    }
}
