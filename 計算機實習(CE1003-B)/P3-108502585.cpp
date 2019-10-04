/*
* Practice 3
* Name: 林昱求
* Student Number: 108502585
* Course 2019-CE1003-B
*/

#include <bits/stdc++.h>
using namespace std;

#define for0(i, n) for(int i = 0; i < n; ++i)

signed main() {
	int n; cin >> n;
	if(n <= 3) {
		cout << "It’s not a Christmas tree!!!\n";
		return 0;
	}
	
	for0(i, n) { 							
		for0(j, n - i - 1) cout << " ";
		for0(j, (i * 2 +1)) cout << "*";
		cout << endl;
	}
	for0(i, n / 3) {
		for0(j, n - 2) cout << " ";
		cout << "***\n";
	} 
} 
