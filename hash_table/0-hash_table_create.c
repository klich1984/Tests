#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define CAPACITY 5000

unsigned long hash_function(char *str)
{
	unsigned long i = 0;
	int j;

	for (j = 0; str[j]; j++)
		i += str[j];
	return i % CAPACITY;
}
/*Cracion de los items*/
typedef struct Ht_item
{
	char *key;
	char *value;
} Ht_item;

/*Diseño de los nodos de la linked_list*/
typedef struct LinkedList
{
	Ht_item *item;
	struct LinkedList *next;
} LinkedList;

/*Diseño para la tabla*/
typedef struct HashTable
{
	Ht_item **items;
	LinkedList **overflow_buckets; //overflow cuando ocurre una colision
	int size;
	int count;
} HashTable;

static LinkedList **create_overflow_buckets(HashTable *table)
{
	LinkedList **buckets = calloc(table->size, sizeof(LinkedList*));
	return buckets;
}

static void free_overflow_buckets(HashTable *table)
{
	LinkedList **buckets = table->overflow_buckets;
	for (int i = 0; i < table->size; i++)
		free_linkedlist(buckets);
	free(buckets);
}

HashTable *create_table(int size)
{
	HashTable *table = malloc(sizeof(HashTable));  //reservar memoria para nuestra tabla
	table->size = size;
	table->count = 0;
	table->items = calloc(table->size, sizeof(Ht_item*));
	table->overflow_buckets = create_overflow_buckets(table);
}

void print_hastable(HashTable *table)
{
	printf("------------start----------");
	for (int i = 0; i < table->size; i++)
	{
		if (table->items[i]) //table->items[i] != "\0"
		{
			printf("Index-> %d\n Key-> %s\n Value-> %s\n", i, table->items[i]->key,
				table->items[i]->value);
		}
		if (table->overflow_buckets[i])
		{
			printf("-----> \nIt was a collision, this is the overflow bucket\n <-----");
			LinkedList *head = table->overflow_buckets[i];
			while (head)
			{
				printf("Key-> %s\n Value-> %s\n", head->item->key, head->item->value);
				head = head->next;
			}
		}
	}
	printf("\n-------> End <--------\n");
}
/*funcion que crea un item*/

Ht_item *create_item(char *key, char *value)
{
	Ht_item *item = malloc(sizeof(Ht_item));
	item->key = calloc(strlen(key) + 1, sizeof(char));
	item->value = calloc(strlen(value), sizeof(char));
	strcpy(item->key, key);
	strcpy(item->value, value);
	return item;
}

void free_item(Ht_item *item)
{
	free(item->key);
	free(item->value);
	free(item);
}
/*funcion que genera colision*/
void handle_collision(HashTable *table, unsigned long index, Ht_item *item)
{
	LinkedList *head = table->overflow_buckets[index];
	if (head == NULL)
	{
		head = allocate_list();
		head->item = item;
		table->overflow_buckets[index] = head;
		return;
	}
	else
	{
		table->overflow_buckets[index] = LinkedList_insert(head, item);
		return;
	}
}


/*Creacion de funcion insert*/
void ht_insert(HashTable *table, char *key, char *value)
{
	Ht_item *item = create_item(item, value);
	int index = hash_function(key); //has function nos retorna el index donde la guardaremos
	Ht_item *current_item = table->items[index];
	if (current_item == NULL)
	{
		if (table->count == table->size)
		{
			printf("Tables is full");
			free_item(item);
			return;
		}
		table->items[index] = item;
		table->count++;
	}
	else
	{
		if (strncmp(current_item->key, key) == 0)
		{
			free(table->items[index]->value);
			table->items[index]->value = calloc(strlen(value) + 1, sizeof(char));
			strcpy(table->items[index]->value, value);
			free_item(item);
			return;
		}
		else
		{
			handle_collision(table, index, item);
			return;
		}
	}
}

int main(void)
{
	//primero crear la tabla
	HashTable *ht = create_table(CAPACITY);
	print_hastable(ht);
	ht_insert(ht, "Betty", "Holberton");
	ht_insert(ht, "Medellin", "Antioquia");
	ht_insert(ht, "Bogota", "Cundinamarca");
	ht_insert(ht, "2(", "something 1");
	ht_insert(ht, "Z", "something 2");
	print_hastable(ht);

	return 0;
}

