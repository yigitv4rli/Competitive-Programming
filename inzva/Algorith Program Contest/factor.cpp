#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>


int main() {
    long long int p, q;
    long long int howMany2 = 0, howMany5 = 0;
    long long int temp;

    std::cin >> p >> q;
    temp = q;

    if (40 % q == 0) {
        std::cout << 1;
        return 0;
    }

    while (temp % 5 == 0) {
        temp/=5;
        howMany5++;
    }

    while (temp % 2 == 0) {
        temp/=2;
        howMany2++;
    }


    if (howMany2 % 3 != 0) {
        howMany2 = (howMany2 / 3) + 1;
    } else {
        howMany2 = howMany2 / 3;
    }

    if (temp != 1) {
        std::cout << -1;
    } else {
        std::cout << std::max(howMany2, howMany5);
    }

    return 0;
}

