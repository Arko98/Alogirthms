#include<stdio.h>
int* merge(int a[],int b[],int n, int* temp)
	{
		int i=0,j=0,k=0,l=0;
		//static int temp[2*n];
		while(i<n & j<n)
			{
				if(a[i]<b[j])
					{
						temp[k] = a[i];
						i++;
					}
				else
					{
						temp[k] = b[j];
						j++;
					}
				k++;
			}
		if (i==n)
			{
				while(j<n)
					{
						temp[k] = b[j];
						j++;
						k++;
					}
			}
		if (j==n)
			{
				while(i<n)
					{
						temp[k] = a[i];
						i++;
						k++;
					}
			}
		return temp;
	}
	
int search_k_smallest(int a[],int b[], int n, int k)
	{
		int i=0;
		int temp[2*n];
		int* sorted_array = merge(a,b,n, temp);
		printf("The combined Sorted Array is: \n"); 
		for (i=0;i<2*n;i++)
			printf("%d ",*(sorted_array+i));
		return *(sorted_array+(k-1));
	}
	
int main()
	{
		int n,k;
		printf("Enter size of the array: ");
		scanf("%d",&n);  
		int a[n],b[n];
		printf("Enter the elements in sorted order for array 1: ");  
		for(int i=0;i<n;i++)    
        	scanf("%d", &a[i]);  
		printf("Enter the elements in sorted order for array 2: ");  
		for(int i=0;i<n;i++)    
        	scanf("%d", &b[i]);  
		printf("Enter the kth smallest element which you want to find (Value of K): ");
		scanf("%d",&k); 		
		int element = search_k_smallest(a,b,n,k);
		printf("\nThe %dth Smallest Element: %d",k,element);
		return 0;
	}
