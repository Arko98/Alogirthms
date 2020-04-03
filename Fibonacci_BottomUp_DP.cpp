#include<stdio.h>

int fib(int n)
	{int current,first = 0,second = 1;
	 if(n==0 | n==1)
		return n;
	 else
	 	{for (int i=1;i<=n-1;i++)
	 		{current = first + second;
	 		 first = second;
	 		 second = current;
			}
		}
	return(current);	
    }
    
int main()
	{int n;
	 printf("Enter Number: ");
	 scanf("%d",&n);
	 printf("Fibonacci Number = %d",fib(n));
	 return 0;	
	}    
