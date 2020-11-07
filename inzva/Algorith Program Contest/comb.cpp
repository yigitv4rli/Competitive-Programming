long long int combinations(int n,int r) {
    long long int upper = 1, lower = 1;

    for(int i = 0; i < r; i++) {
        upper*= (n-i);
    }
    for(int j = 1; j <= r; j++) {
        lower *=j;
    }

    return upper/lower;

}