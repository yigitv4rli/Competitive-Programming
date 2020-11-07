#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>



int main() {
    std::vector<int> a;
    std::vector<int> b;
    int N, maximum, DP[100000];

    scanf("%d", &N);

    for (int i = 0; i < N; i++) {
        int ai, bi;
        scanf("%d %d", &ai, &bi);
        a.push_back(ai);
        b.push_back(bi);
    }

    DP[N-1] = a[N-1];
    
    for(int i = N-2; i>= 0; i--) {
        DP[i] = a[i];
        maximum = 0;
        for(int j = i+1; j < N; j++) {
            if (b[i] >= b[j]) continue;
            if (maximum < DP[j]) maximum = DP[j];
        }
        DP[i]+= maximum;
    }

    maximum = DP[0];
    for(int i = 1; i < N; i++) {
        if (maximum < DP[i]) maximum = DP[i];
    }
    
    std::cout << maximum;
    return 0;

}


