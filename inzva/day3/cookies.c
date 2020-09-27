#include <stdio.h>
#include <string.h>
#include <math.h>
#include <stdlib.h>

int main(){
    int n,V,maximum, arr[100000],bl[100000]={0},summation =0,total,i,j;
    
    scanf("%d %d",&n,&V);

    for(i=0;i<n;i++){
        scanf("%d",&arr[i]);
        summation+=arr[i];
    }
    if(n==1){
        if(V>=arr[0])printf("1");
        else printf("0");
        return 0;
    }
    if(summation<=V){ 
        printf("%d",n);
        return 0;
    }
    
    for(i=0;i<n;i++){
        total=0;
        summation=0;
        for(j = i; j < n; j++){
            if(summation + arr[j] <= V){
                summation+=arr[j];
                total++;
            }
            else break;
        }
     bl[i] = total;
     if(j == n)break;    
    }
    maximum = bl[0];
    
    for(i=1;i<n;i++){
        if(bl[i]>maximum) maximum = bl[i];
    }
    printf("%d",maximum);

    return 0;
}
