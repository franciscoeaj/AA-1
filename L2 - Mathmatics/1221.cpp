#include <iostream>
#include <cstring>
 
using namespace std;
 
bool is_prime(unsigned long n)
{
    if (n <= 3)
    {
        return n > 1;
    }
  
    if (n % 2 == 0 || n % 3 == 0)
    {
        return false;
    }
  
    for (unsigned short i = 5; i * i <= n; i += 6)
    {
        if (n % i == 0 || n % (i + 2) == 0)
        {
            return false;
        }
    }
  
    return true;
}
 
int main()
{
    int n, number;
    string result;
     
    cin >> n;
     
    for (int i = 0; i < n; i++)
    {
        cin >> number;
         
        if (is_prime(number))
        {
            result = "Prime\n";
        }
        else
        {
            result = "Not Prime\n";
        }
         
        cout << result;
    }
}