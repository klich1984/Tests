#ifndef __HASHTABLE_H
#define __HASHTABLE_H


#include <sys/types.h>
#include <sys/stat.h>
#include <sys/time.h>
#include <fcntl.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>

#define TAMHASH 1572869

typedef struct {
	int *datos;
	int num_datos;
}datos;

typedef struct{
	int k[5];
	int v;
}hash_datos_t;

typedef struct
{
	hash_datos_t *datos;
	int num_datos;
	int num_max_datos;
}hash_node;

#endif
