int count = 0;

void merge(long long array[], long begin, long mid, long end)
	{   
		int i = begin,j = mid+1,index = begin, k = 0, temp[100];
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

void mergesort(long long array[], long long begin, long long end)
	{    
		if (begin<end)
			{
				int mid = (begin+end)/2;
				mergesort(array,begin,mid);
			        mergesort(array,mid+1,end);
				merge(array,begin,mid,end);
			}
	}

long long int inversionCount(long long arr[], long long N)
    {
        mergesort(arr,0,N-1);
        return count;
    }