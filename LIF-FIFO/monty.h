#ifndef __MONTY_H__
#define __MONTY_H__
#include <stdio.h> /* fopen */
#include <string.h> /* strok */
#include <stdlib.h> /* free */

/**
 * struct stack_s - doubly linked list representation of a stack (or queue)
 * @n: integer
 * @prev: points to the previous element of the stack (or queue)
 * @next: points to the next element of the stack (or queue)
 *
 * Description: doubly linked list node structure
 * for stack, queues, LIFO, FIFO Holberton project
 */
typedef struct stack_s
{
	int n;
	struct stack_s *prev;
	struct stack_s *next;
} stack_t;
/**
 * struct instruction_s - opcode and its function
 * @opcode: the opcode
 * @f: function to handle the opcode
 *
 * Description: opcode and its function
 * for stack, queues, LIFO, FIFO Holberton project
 */
typedef struct instruction_s
{
	char *opcode;
	void (*f)(stack_t **stack, unsigned int line_number);
} instruction_t;

/**
* 
* 
* 
*/

typedef struct variables_s
{
	FILE *file_pointer;
	char *buffer;
	unsigned int line_number;
	size_t bytes_qty;
	instruction_t *instru;
	stack_t *head_list;
}var;

var var_t;
extern int value;
char *new_line_remove(char *buffer);
void get_opcode_function(char *opcode_input, stack_t **head_list, unsigned int line_number);
void opcode_push(stack_t **head_list, unsigned int line_number);
void opcode_pall(stack_t **head_list, unsigned int line_number);
void free_dlistint(void);


/*functions test*/
char **divide_line(char *line, char *delim);
char *_strcpy(char *dest, char *src);
char **divide_path(char *str, char **env);
char *concat_path(char *command, char **env);
void free_pointers(char *line, char *path, char **arguments);
int _count_token(char *line, char *delim);

#endif
