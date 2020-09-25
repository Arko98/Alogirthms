#include<stdio.h>

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
	{int array[5] = {12,6,34,90,1};
	 merge_sort(array,0,4);
	 for(int i=0;i<5;i++)
	 	 printf("%d ",array[i]);
	 return 0;
	}
