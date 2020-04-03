#include<stdio.h>
/*Adjacency Matrix*/
int G[6][6] = {{0,1,0,1,0,1},
			   {1,0,1,0,0,0},
			   {0,1,0,0,0,0},
			   {1,0,0,0,1,0},
			   {0,0,0,1,0,1},
			   {1,0,0,1,1,0}};

/*Stack*/
int queue[100], start = -1,end = -1;
void enqueue(int val)
	{if(start == -1)
		{start++;
		 end++;
		 queue[end] = val;
		}
	 else
	 	{end++;
		 queue[end] = val;
		}
	}
int dequeue()
	{start++;
	 return queue[start-1]; 
	}
void state()
	{for(int i=start; i<=end; i++)
	 	printf("%d ",queue[i]);
	}
/*DFS Function*/	
void BFS(int n, int source)
	{int BFS_Order[n];
	 int vertex_state[n];
	 for(int i=0;i<n;i++)
	 	vertex_state[i] = 0;      /*0 - not visited, 1 - under process, 2 - processed*/
	 enqueue(source-1);
	 vertex_state[source-1] = 1;
	 int index = 0; 
	 printf("Initial Queue State: ");
	 state();
	 printf("\n");
	 while(start <= end)
	 	{int v = dequeue();
	 	 vertex_state[v] = 2;
	 	 BFS_Order[index] = v+1;
	 	 index++;
	 	 for(int j=0;j<n;j++)
	 	 	{if(G[v][j] !=0 && vertex_state[j] == 0)   /*Vertices adjacent to reently popped vertex v which are not processed*/
	 	 		{enqueue(j);
	 	 		 vertex_state[j] = 1;
				}
			}
		 printf("Queue State at Iteration %d : ",index);
	 	 state();
	 	 printf("\n");
		}
	 printf("\nBreadth First Search Order : ");
	 for(int i=0;i<n;i++)
	 	 printf("%d ",BFS_Order[i]);
	}
	
	
int main()
	{int source;
	 printf("Enter Source Vertex : ");
	 scanf("%d",&source);
	 
	 BFS(6,source);
	 return 0;	
	}
