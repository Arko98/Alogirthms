#include<stdio.h>
int cost[3][3];
int min(int a,int b)
	{if(a<b)
		return a;
	 else
	 	return b;
	}

void Floyd_Warshall(int n)
	{for(int i=0;i<n;i++)
		{for(int j=0;j<n;j++)
			{for(int k=0;k<n;k++)
				cost[i][j] = min(cost[i][j],cost[i][k]+cost[k][j]);
			}
		}
	 //return cost;
	}

int main()
	{int n = 3;
	 printf("Enter Cost Matrix: \n");
	 for(int i=0;i<n;i++)
		{for(int j=0;j<n;j++)	
			{printf("Enter Cost of edge ( %d, %d): ",i,j);
			 scanf("%d",&cost[i][j]);
			}
	    }
	 Floyd_Warshall(n);
	 printf("All Pairs Shortest Distance Matrix:\n");
	 for(int i=0;i<n;i++)
		{for(int j=0;j<n;j++)
			printf("%d ",cost[i][j]);
		 printf("\n");
		}
	 return 0;	
	}
