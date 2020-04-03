#include<stdio.h>
#include<LIMITS.h>

int Optimal_Matrix_Order(int p[],int n)
	{int M[n][n],i,j,L,k,val;
	 //initialiation of computation table
	 for (i=1;i<n;i++)
	 	M[i][i] = 0;
	 //Computation of Minimum Cost
	 for (L=2;L<=n;L++)
	 	{for(i=1;i<=n-L+1;i++)
	 		{j= i+L-1;
	 		 M[i][j] = INT_MAX;
	 		 for(k=i;k<=j-1;k++)
	 		 	{val = M[i][k] + M[k+1][j] + p[i-1]*p[k]*p[j];
	 		 	 if(val<M[i][j])
	 		 	 	M[i][j] = val;
				}
			}
		}
	 return M[1][n];	
	}

int main()
	{int n;
	 printf("Enter Number of Matrices : ");
	 scanf("%d",&n);
	 int p[n+1];
	 printf("Enter Size: \n");
	 for(int i=0;i<=n;i++)
		{printf("Enter %dth size: ",i);
		 scanf("%d",&p[i]);
		}
	 int min_cost = Optimal_Matrix_Order(p,4);
	 printf("\nMinimum Cost : %d",min_cost);
	 return 0;
	}

