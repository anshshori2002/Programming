#include<iostream>
using namespace std;
int main()
{
    int n;
    cout<<"Enter n: ";
    cin>>n;
    for(int rows=1;rows<=n;rows++)
    {
        for(int col=1;col<=rows;col++)
        {
            cout<<col;
        }       
        printf("\n"); 
    }
}
