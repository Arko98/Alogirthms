#include<stdio.h>

void Greedy_Knapsack(int p[],int w[],int n,int W)
	{float x[n];
	 float load = 0.0,profit = 0.0;
	 for(int i=0;i<n;i++)
	 	x[i] = 0.0;
	 int item = 0;
	 while( item<=n && load<=W)
	 	{if(load+w[item]<=W)
	 		{x[item] = 1;
	 		 load = load + w[item];
	 		 profit = profit + p[item];
			}
		 else
		 	{float remain = W - load;
		 	 load = load + (remain/w[item]);
		 	 profit = profit + p[item]*(remain/w[item]);
		 	 x[item] = remain/w[item];
			}
		 item++;
		}
	 printf("\nMaximized Profit = %f",profit);
	 printf("\nDistribution Array of Items: \n");
	 for(int i=0;i<n;i++)
		printf("%f ",x[i]);
	}
	
int main()
	{int n,W,p[n],w[n];
	 printf("Enter Capacity of Knapsack : ");
	 scanf("%d",&W);
	 printf("Enter Number of Items : ");
	 scanf("%d",&n);
	 printf("Enter Profits: \n");
	 for(int i=0;i<n;i++)
		{printf("Enter Profit of %d th item: ",i+1);
		 scanf("%d",&p[i]);
		}
	 printf("Enter Weights: \n");
	 for(int i=0;i<n;i++)
		{printf("Enter Weight of %d th item: ",i+1);
		 scanf("%d",&w[i]);
		}
	 Greedy_Knapsack(p,w,n,W);
	 return 0;
	}
