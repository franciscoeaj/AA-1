#include<stdio.h>
 
main()
{
    int m, n, c, result;
    while (true)
    {
        scanf("%d %d %d", &n, &m, &c);

        if (n == 0 && m == 0 && c == 0) break;
         
        if (n == m && c == 1)
        {
            if ((n - 7) % 2 == 0)
            {
                result = ((n - 7) * (m - 7)) / 2;
            }
            else
            {
                result = (((n - 7) * (m - 7)) / 2) + 1;
            }
        }
        else
        {
            if (((n - 7) * (m - 7)) % 2 != 0  && c == 1)
            {
                result = (((n - 7) * (m - 7)) / 2) + 1;
            }
            else
            {
                result = ((n - 7) * (m - 7)) / 2;
            }
        }

        printf("%d\n", result); 
    }   
    return 0;  
}