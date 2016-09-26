#include <iostream>
#include <ctime>
#define MAX 100
#define NIL -1

using namespace std;

/* Recursive. */
int lookup[100];

void _initialize() {
    int i;
    for(i = 0; i < MAX; i++)
        lookup[i] = NIL;
}


int _lis(int arr[], int n, int *max_ref) {
    /* Base Case. */

    if(n == 1)
        return 1;

    // 'max_ending_here' is length of LIS ending with arr[n-1]
    int res, max_ending_here = 1;
    
    /* Recursively get all LIS ending with arr[0], arr[1] ...
       arr[n-2]. If   arr[i-1] is smaller than arr[n-1], and
       max ending with arr[n-1] needs to be updated, then
       update it 
    */
    for(int i = 1; i < n; i++) {
        if(lookup[i] == NIL)
            res = _lis(arr, i, max_ref);
        else
            res = lookup[i];
        
        if(arr[i - 1] < arr[n - 1] && res + 1 > max_ending_here)
            max_ending_here = res + 1;
    }

    // Compare max_ending_here with the overall max. And
    // update the overall max if needed
    if(*max_ref < max_ending_here)
        *max_ref = max_ending_here;

    return max_ending_here;
}


/* Bottom Up */
int LIS(int arr[], int n) {
    int lis[n];
    int i, j, Max = 0;

    for(i = 0; i < n; i++)
        lis[i] = 1;

    for(i = 1; i < n; i++) {
        for(j = 0; j < i; j++) {
            if(arr[i] > arr[j] && lis[i] < 1 + lis[j])
                lis[i] = 1 + lis[j];
        }
        Max = max(Max, lis[i]);
    }

    return Max;

}

/* Top Down */
int LIS_TD(int arr[], int n) {
    int max = 1;
    _lis(arr, n, &max);
    return max;
}

int main() {
    clock_t t1 = clock();
    int arr[] = { 10, 22, 9, 33, 21, 50, 41, 60 };
    int n = sizeof(arr)/sizeof(arr[0]);
    _initialize();
    cout << LIS_TD(arr, n) << endl;
    clock_t t2 = clock();
    cout << double(t2 - t1) / CLOCKS_PER_SEC << endl;
    return 0;
}
