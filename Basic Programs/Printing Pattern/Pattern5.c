Pattern 5:    *
             ***
            *****
           *******
           
Code:

#include <stdio.h>
int main()
{
    int n,rows,star,spaces;
    printf("Enter no. :");
    scanf("%d",&n);
    for(rows=1;rows<=n;rows++)
    {
        for(spaces = 1;spaces<=n-rows;spaces++)
        {
            printf(" ");
        }
        for(star = 1;star<=2*rows-1;star++)
        {
            printf("*");
        }
        printf("\n");
    }
    return 0;
}

