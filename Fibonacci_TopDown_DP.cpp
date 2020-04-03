#include<stdio.h>

int fib_array[1000];

int fib(int n)
	{if(n==0 | n==1)
		fib_array[n] = n;
	 else
	 	{if(fib_array[n] == -1)
	 		fib_array[n] = fib(n-1) + fib(n-2); 
		}
	return(fib_array[n]);	
    }
    
int main()
	{for (int i=0;i<1000;i++)
		 fib_array[i] = -1;
	 int n;
	 printf("Enter Number: ");
	 scanf("%d",&n);
	 printf("Fibonacci Number = %d",fib(n));
	 return 0;	
	}    
