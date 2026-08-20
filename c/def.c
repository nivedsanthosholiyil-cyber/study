#include <cs50.h>
#include <stdio.h>
void def(int t);
int get_n(void); 
int main(void)
{
    int n = get_int("how much 67 u want yo");
    def(n);
}
int get_n(void)
{
    int n;
    do
    {
        n = get_int("how much 67 u wnat yo");
    }
    while (n<0);
    return n;

    
}
void def(int t)
{
    for(int i=0 ;i < t; i++)
    {
        printf("67 cocomelon stairway to heaven \n");
    }
}