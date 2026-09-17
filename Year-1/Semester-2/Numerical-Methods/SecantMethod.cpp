#include <bits/stdc++.h>
using namespace std;

#define ld long double

ld f(ld x)
{
    return x * x * x - 3 * x - 5;
}

ld Error(ld a, ld b)
{
    return abs((a - b) / b);
}

int iter = 0;

ld secantMethod(ld x1, ld x2, ld error)
{
    ld c = 0;
    while (Error(x1, x2) > error)
    {
        if (f(x2) - f(x1) == 0)
        {
            cout << "Division by zero error in iteration " << iter << endl;
            return c;
        }
        c = (x1 * f(x2) - x2 * f(x1)) / (f(x2) - f(x1));
        cout << fixed << setprecision(4) << iter << "\t\t" << x1 << "\t\t" << x2 << "\t\t" << c << "\t\t" << Error(x1, x2) << endl;
        if (f(c) == 0.0)
        {
            break;
        }
        else
        {
            x1 = x2;
            x2 = c;
        }
        iter++;
    }
    cout << "The root of the equation is: " << endl;
    return c;
}

int main()
{
    ld x1, x2;
    cin >> x1 >> x2;
    ld error = 0.0001;
    cout << "Secant Method" << endl;
    cout << "Iter"
         << "\t\tx1: "
         << "\t\tx2: "
         << "\t\tc: "
         << "\t\tError: " << endl;
    cout << secantMethod(x1, x2, error) << endl;

    return 0;
}
