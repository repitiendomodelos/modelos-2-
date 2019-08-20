//Juan pablo parra 20172020029
//santiago roa 20172020099
//christian isaac 20172020076




int fibo (int n){
	
	if (n==0) return 0;
	if (n==1) return 1;
	if (n>1) return fibo(n-1) + fibo(n-2);
	

}



#include<iostream>
using namespace std;
 
int main(){
	
	
	int n;
	cin>>n;
	cout<<"fibonnaci recursivo";	
	
	cout<<fibo(n);	
	

	
	
	
	
    return 0;
}
