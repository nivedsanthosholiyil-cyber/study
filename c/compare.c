#include <stdio.h>
#include <cs50.h>
int main(void)
{
    int x = get_int("whats is x");
    int y = get_int("what is y");

    if (x > y)
    {
        printf("x grt than y");
    }
    else if (x<y)
    {
        printf("y grt than x");

    }
    else 
    {
        printf("x = to y");
    }
}