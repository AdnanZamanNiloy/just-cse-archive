#include <bits/stdc++.h>
using namespace std;

double trueError(double realValue, double calculatedValue)
{
    return abs(realValue - calculatedValue);
}

double trueRelativeError(double realValue, double calculatedValue)
{
    return trueError(realValue, calculatedValue) / realValue;
}

double trueRelativeErrorPercentile(double realValue, double calculatedValue)
{
    return trueRelativeError(realValue, calculatedValue) * 100;
}

double absoluteError(double currentValue, double pastValue)
{
    return abs(currentValue - pastValue);
}

double absoluteRelativeError(double currentValue, double pastValue)
{
    return absoluteError(currentValue, pastValue) / currentValue;
}

double absoluteRelativeErrorPercentile(double currentValue, double pastValue)
{
    return absoluteRelativeError(currentValue, pastValue) * 100;
}

int main()
{
    double a, b;
    cin >> a >> b;
    cout << "The True Error is: " << trueError(a, b) << endl;
    cout << "The True Relative Error is: " << trueRelativeError(a, b) << endl;
    cout << "The True Relative Error Percentile is: " << trueRelativeErrorPercentile(a, b) << endl;
    cout << "The Absolute Error is: " << absoluteError(a, b) << endl;
    cout << "The Absolute Relative Error is: " << absoluteRelativeError(a, b) << endl;
    cout << "The Absolute Relative Error Percentile is: " << absoluteRelativeErrorPercentile(a, b) << endl;
    return 0;
}