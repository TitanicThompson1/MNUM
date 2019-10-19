#include <iostream>
#include <iomanip>
#include <cmath>

using namespace std;

double f(double x ){ return (x-3.6)+(pow(cos(x+1.2),3));};

double df(double x) {return 1-3*pow(cos(x+1.2),2)*sin(x+1.2);};

int main() {
    double x=0.5;
    x= (double) x - f(x)/df(x);
    cout << x;


}