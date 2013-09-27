#include <stdio.h>
#include <math.h>
 
int VAXrand(unsigned int seed)
{
    unsigned int s = ((69069 * seed + 1) % (unsigned int)pow(2,32));
    return s;
}
 
int main()
{
    unsigned int tempseed = 0; //starting seed
    unsigned int res = 0; //store result
    unsigned int n = 0;
 
    tempseed = 6;
for (n = 0; n < 10; n++)
    {
        res = VAXrand(tempseed);
        printf("Starting seed: %u, seed mod 36: %u, result: %u, result mod 36: %u\n",                  tempseed, tempseed%36, res, res%36);
        tempseed = res;
    }
 
return 0;
}