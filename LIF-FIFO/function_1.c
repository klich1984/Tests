#include "monty.h"

/*elimina \n*/
char *new_line_remove(char *buffer)
{
	int i = 0;

	for (; *(buffer + i) != '\n'; i++)
		;
	*(buffer + i) = '\0';
	return (buffer);
}

/*Funcion que busca y devuelve un pointer a la funcion*/
void get_opcode_function(char *opcode_input, stack_t **head_list, unsigned int line_number)
{
	instruction_t function[] = {
		{"push", opcode_push},
		{"pall", opcode_pall},
		{NULL, NULL}
	};
	int i = 0;
	char *str = NULL;

	while (function[i].opcode != NULL)
	{
		str = function[i].opcode;
		/*Si es = 0 las palabras son identicas*/
		if (strcmp(opcode_input, str) == 0)
		{
			function[i].f(head_list, line_number);
			return;
		}
		i++;
	}
	if (function[i].opcode == NULL)
	{
		/*liberar y cerrar*/
		fprintf(stderr, "L%d: unknown instruction %s\n", line_number, opcode_input);
		exit(EXIT_FAILURE);
	}
}


/*crea double linked list agregando nodo al principio LIFO*/
void opcode_push(stack_t **head_list, unsigned int line_number)
{
	stack_t *new = NULL;
	stack_t *temp = NULL;
	char *token = NULL;
	int value = 0;

	token = strtok(NULL, " ");
	if (token)
		value = atoi(token);
	else
		value = 0;
/*printf("value %d\n", value);*/
	new = (malloc(sizeof(stack_t)));
	if (new == NULL)
	{
		fprintf(stderr, "Error: malloc failed\n");
		exit(EXIT_FAILURE);
	}
	new->prev = NULL;
	new->next = *head_list;
	new->n = value;
	if (*head_list == NULL)
		*head_list = new;
	else
	{
		temp = *head_list;
		*head_list = new;
		temp->prev = new;
	}
	/*return (new);*/
	printf("line is: %d | date is: %d\n", line_number, new->n);
}

/*imprime la doble lista linkeada creada en push*/
void opcode_pall(stack_t **head_list, __attribute__((unused))unsigned int line_number)
{
	stack_t *temp = *head_list;

	if (temp == NULL)
		return;
	while(temp != NULL)
	{
		printf("%d\n", temp->n);
		temp = temp->next;
	}

	printf("funcion opcode_pall line_pall: %d\n", line_number);
}

/**
* free_dlistint - function that free double link list
* @head: pointer a double linked list
* Return: Nothing
*/

void free_dlistint(void)
{
	stack_t *free_list = var_t.head_list;
	if (free_list == NULL)
		return;

	if (free_list->prev != NULL)
	{
		while (free_list->prev != NULL)
			free_list = free_list->prev;
	}
	else
	{
		while (free_list->next != NULL)
		{
			free_list = free_list->next;
			free(free_list->prev);
		}
	}
	free(free_list);
}
