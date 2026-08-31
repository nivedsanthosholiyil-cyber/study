#include <stdio.h>

int main(void)
{
    int scores[3];

    scores[0] = 63;
    scores[1] = 54;
    scores[2] = 33;

    printf("avg %f\n", (scores[0] + scores[1] + scores[2]) / 3.0);
}