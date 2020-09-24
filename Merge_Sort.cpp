#include<stdio.h>

void merge(int array[],int begin,int mid,int end)
	{int i=0, j=mid+1, index=0,temp[100];
	 while(i<=mid && j<=end)
	 	{if(array[i]<array[j])
	 		{temp[index] = array[i];
	 		 i++;
			}
		 else
		 	{temp[index] = array[j];
	 		 j++;
			}
		 index++;
		}
	 if(i>mid)
	 	{while(j<=end)
	 		{temp[index] = array[j];
	 		 index++;
	 		 j++;
			}
		}
	 else if(j>end)
	 	{while(i<=mid)
	 		{temp[index] = array[i];
	 		 index++;
	 		 i++;
			}
		}
	 for(int a=0;a<index;a++)
	 	 array[a] = temp[a]; 
	} 

void merge_sort(int array[],int begin,int end)
	{if(begin<end)
		{int mid = (begin+end-1)/2;
		 merge_sort(array,begin,mid);
		 merge_sort(array,mid+1,end);
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
