#include<stdio.h>
#include<conio.h>

int count = 0;

void merge(int array[], int begin,int mid,int end)
	{   
		int i=begin,j=mid+1,index=begin,k=0,temp[100];
		while (i<=mid && j<=end)
			{
				if (array[i]<=array[j])
					{
						temp[index]=array[i];
						i++;
					}
				else
					{
					    count += (mid-i+1); 
				            temp[index]=array[j];
					    j++;
					}
				index++;
			}

			while(j<=end)
				{
					temp[index]=array[j];
					j++;
					index++;
				}
			while(i<=mid)
				{
					temp[index]=array[i];
					i++;
					index++;
			    }
		for (k=begin;k<=end;k++)
			{
				array[k]=temp[k];
			}
	}

void mergesort(int array[], int begin, int end)
	{    
		if (begin<end)
			{
				int mid = (begin+end)/2;
				mergesort(array,begin,mid);
			        mergesort(array,mid+1,end);
				merge(array,begin,mid,end);
			}
	}
	
int main()
	{
		int i,n;
		scanf("%d",&n);
		int a[n];
		for (i=0;i<n;i++)
			scanf("%d",&a[i]);
		mergesort(a,0,n-1);
		for (i=0;i<n;i++)
			printf("%d ",a[i]);
		printf("\nInversions: %d",count);
		return 0;
	}	
