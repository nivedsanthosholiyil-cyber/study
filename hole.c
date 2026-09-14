#include <stdio.h>
#include <stdlib.h>
int mad(int g1, int g2 ){
    int result;
    if (g1 > g2) {
        result = g1;
    }
    else {
        result = g2;
    }
    return result;
}
int main () {
    printf("%d", mad(4, 10));

    return 0;
}