/*
* Practice 2
* Name: 林昱求
* Student Number: 108502585
* Course 2019-CE1003-B
*/
#include <bits/stdc++.h>
using namespace std;

int l = 0, r = 101;		// 輸出範圍
bool valid(int num) {
	if(num <= l || num >= r) {
		cout << "Invalid input\n";
		return false;
	}
	return true;
}

signed main() {
	int in;                 // input
	int ans;
	while(cin >> ans && (valid(ans) == false));
	
	while(cin >> in) if(valid(in)) {
		if(ans == in) {
			cout << "You got it!\n";
			break;
		} 

		if(ans > in) l = in;
		else r = in;
		cout << max(1, l) << '~' << min(100, r) << endl;
	}
}

