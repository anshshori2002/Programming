#include<bits/stdc++.h>
using namespace std;
//Function for Counting Sort
void counting_sort(vector<int> a,int k,int n)
{
    vector<int> c(k);
    vector<int> b(n);
    for(int i = 0; i <= k; i++)
    {
        c[i] = 0;
    }
    for(int j = 0; j < n; j++)
    {
        c[a[j]]++;
    }
    for(int i = 1; i <= k; i++)
    {
        c[i] = c[i] + c[i-1];
    }
    for(int j = n-1; j >= 0; j--)
    {
        b[c[a[j]]] = a[j];
        c[a[j]] = c[a[j]] - 1;
    }
    // Print the Output of sorted string 
    cout<<"Sorted elements are: ";
    for(int i = 1; i <=n; i++)
    {
        cout<<b[i]<<" ";
    }
}
int main()
{
    int n;
    cout<<"Enter the size: ";
    cin>>n;
    vector <int> v;
    int max = 0;
    cout<<"Enter the elements: ";
    for(int i = 0; i < n; i++)
    {
        int x;
        cin>>x;
        v.push_back(x); 
        if(x > max) max = x;
    }
    counting_sort(v, max, n);
return 0;
}


OUTPUT:

Enter the size: 8
Enter the elements: 23 11 45 1 45 90 22 12
Sorted elements are: 1 11 12 22 23 45 45 90 

Enter the size: 6
Enter the elements: 232 33 123 56 67 889
Sorted elements are: 33 56 67 123 232 889 
