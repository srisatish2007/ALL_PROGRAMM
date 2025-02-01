#include <iostream>
#include <math.h>
using namespace std;
int main()
{
    int n, sum1, i, sum2 = 0;
    cout << "Enter the n term";
    cin >> n;
    sum1 = 0;
    for (i = 0; i < n; i++)
    {
        sum1 += 2 * (pow(10, i));
        sum2 += sum1;
    }
    cout << "The sum to the       series is =" << sum2;
    return 0;
}