#include <stdio.h>
#include<stdlib.h>
int compare(const void*a, const void*b){
    return(*(int *)a - *(int *)b);
    
}
int max_f_value(int N, int A[]){
    qsort(A, N, sizeof(int), compare);
    int max_f = 0,n;
    for(int i=0;i<n-1;i++){
        max_f += A[i] + A[i + 1] - 1;
    }
    return max_f;
}
int main(){
    int T;
scanf("%d", &T);
for(int t =0;t<T;++T){
    int N;
    scanf("%d", &N);
    int A[N];
    for(int i=0;i<N;++i)
    {
        scanf("%d", A[i]);
    }
    printf("%d\n", max_f_value(N, A));
}
return 0;
}

