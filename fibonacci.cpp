#include<bits/stdc++.h>
#define ll long long int
#define endl "\n"
using namespace std;
int main()
{
	int n;
	cin>>n;
	int a=0,b=1,c=1;
	for(int i=1;i<=n;i++){
		c=a+b;
		a=b;
		b=c;
	}
	cout<<c<<endl;
}
