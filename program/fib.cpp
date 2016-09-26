#include <iostream>
#define NIL -1
#define MAX 100

using namespace std;

int lookup[100];

/* Function to initialize NIL values in lookup table */
void _initialize() {
    int i;
    for(i = 0; i < MAX; i++) {
        lookup[i] = NIL;
    }
}

/* function for nth Fibonacci number */
int fib(int n) {
    if(lookup[n] == NIL) {
        if(n <= 1)
            lookup[n] = n;
        else
            lookup[n] = fib(n - 1) + fib(n - 2);
    }

    return lookup[n];
}

int fib_bu(int n) {
    int f[n + 1];
    int i;
    f[0] = 0;
    f[1] = 1;
    for(i = 2; i <= n; i++)
        f[i] = f[i - 1] + f[i - 2];

    return f[n];
}

int main() {
    int n = 50;
    _initialize();
    cout << fib_bu(n) << endl;
    return 0;
}
