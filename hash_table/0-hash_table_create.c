#include "hash_tables.h"

inline static int hash_key(int x, int y, int z, int v, int w)
{
	return (x * y * (z + 1) + v + w) / 10;
}

int main(void)
{
	int result = 0;

	result = hash_key(9, 100, 33, 100, 2221);
	printf("el valor de la clave fue %d", result);
	return 0;
}



