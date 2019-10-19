#include <iostream>
#include <iomanip>
#include <cmath>

using namespace std;

double f(double x){return exp(0.7*x)-pow(x,2)-0.5;};

int main() {
    double a=-1,b=0,m=(double)(a+b)/2;
    cout << a << " " << b << " " << m << " " << f(a) << " " << f(b) << " " << f(m) << endl;

    for(int i=0;i<2;i++){

        if (f(a)*f(m)<0)
            b=m;
        else
            a=m;
        m=(double)(a+b)/2;
        cout << a << " " << b << " " << m << " " << f(a) << " " << f(b) << " " << f(m) << endl;

    }

}