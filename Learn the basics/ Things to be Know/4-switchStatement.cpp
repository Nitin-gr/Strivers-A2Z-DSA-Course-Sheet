#include <vector>

double areaSwitchCase(int ch, std::vector<double> a) {
	// Write your code here
	switch(ch){
		case 1:
		  return 3.14159265359*a[0]*a[0];
		  break;
		case 2:
		   return a[0]*a[1];
           break;
        default :
           return 0;	
	}
}