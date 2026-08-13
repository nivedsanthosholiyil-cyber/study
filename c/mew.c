#include <stdio.h>
#include <cs50.h>
#include <stdbool.h>
int main(void)

{
    int n;
    while (true)
    {
        n = get_int("how much cuh u wnat ");
        if (n<0)
        {
            continue;
        
        }
        else
        {
            break;

        }
    }

    for (int i = 0; i < n; i++)
    {
        printf("67\n");
    }
}