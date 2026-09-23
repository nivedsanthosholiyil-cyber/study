#include <cs50.h>
#include <stdio.h>

int main(void)
{
    int numbers[] = {1, 2, 3, 4, 5};

    int n  = get_int("Enter a number: ");
    for (int i = 0; i < 5; i++)
    {
        if (numbers[i] == n)
        {
            printf("found\n");
            return 0;
        }
    }
    printf("not found\n");
    return 1;
}