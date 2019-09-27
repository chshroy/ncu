/*
* Assignment 2
* Name: 林昱求
* Student Number: 108502585
* Course 2019-CE1003-B
*/
#include <iostream>
#include <iomanip>
using namespace std;

signed main() {
	double n, sum {}, cnt {};
	while(cnt < 10) {
		cin >> n;
		if(n == -1) break;
		if(n < 0 || n > 100) continue;
		sum += n;
		cnt++;
	}
	
	sum /= cnt;
	
	cout << cnt << endl;
	cout << fixed << setprecision(3) << sum << endl;

	if(sum >= 90) cout << "A\n";
	else if(sum >= 80) cout << "B\n";
	else if(sum >= 70) cout << "C\n";
	else if(sum >= 60) cout << "D\n";
	else cout << "F\n";
}
