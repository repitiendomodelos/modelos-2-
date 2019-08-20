#include <iostream>


using namespace std;
int main(int argc, char** argv) {
	int n;
	int antes = 0;
	int despues = 1 ;
	int aux;
	int c;
	 


	cin>>n;
	
	 
	for (c = 0; c <= n; c++){
	    if (c <= 1)
	      aux = c;
	    else{
	      aux = antes + despues;
	      antes = despues;
	      despues = aux;
	    }
	    	
	  }
	 
 
	cout<<" La serie de Fibonachi  = "<<aux;
	
	
	return 0;
}
