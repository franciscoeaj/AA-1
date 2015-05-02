#include <cstdio>
 
int gcd(int a, int b)
{
    int t;
 
    while (b > 0)
    {
        t = b;
        b = a % b;
        a = t;
    }
     
    return a;
}
 
int main()
{
    int n, f1, f2;
     
    scanf("%d", &n);
     
    for (int i = 0; i < n; i++)
    {
        scanf("%d %d", &f1, &f2);
         
        int result = gcd(f1, f2);
        printf("%d\n", result);
    }
     
    return 0;
}