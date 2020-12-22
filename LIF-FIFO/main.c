#include "monty.h"

void opcode_push(__attribute__((unused))stack_t **head_list, unsigned int line_number)
{
	printf("funcion opcode_push line: %d\n", line_number);
}

void opcode_pall(__attribute__((unused))stack_t **head_list, unsigned int line_number)
{
	printf("funcion opcode_pall  line_pall: %d\n", line_number);
}

/*Funcion que busca y devuelve un pointer a la funcion*/
void get_opcode_function(char *opcode_input, stack_t **head_list, unsigned int line_number)
{
	instruction_t function[] = {
		{"push", opcode_push},
		{"pall", opcode_pall},
		{NULL, NULL}
	};
	int i = 0, len_str = 0;
	char *str = NULL;

	while (function[i].opcode != NULL)
	{
		str = function[i].opcode;
		if (strcmp(opcode_input, str) == 0)
		{
			printf("Las palabras son identicas\n");
			function[i].f(head_list, line_number);
		}
		i++;
	}

	/*len_str = strlen(opcode_input);
	printf("len_str = %d\n", len_str);
	for (i = 0; opcode_input[i] == function->opcode[i] && opcode_input[i] != '\0'; i++)
	{
		printf("%c", opcode_input[i]);
	}
	printf("\n");
	printf("i = %d\n", i);
	if (i == len_str)
		function[1].f(head_list, line_number);
		//printf("son iguales\n");
	else
		printf("No son iguales\n");




	/* find the input function in our opcode function */
	/*for (; function[i].opcode != NULL; i++)
		;
	if (function[i].opcode == NULL)
		return;
	function[i].f(head_list, line_number);*/
}

/*elimina \n*/
char *new_line_remove(char *buffer)
{
	int i = 0;

	for (; *(buffer + i) != '\n'; i++)
		;
	*(buffer + i) = '\0';
	return (buffer);
}

/*main*/
int main(int argc, char **argv)
{
	if (argc > 2 || argc == 0)
	{
		printf("USAGE: monty file");
		return (EXIT_FAILURE);
	}
	if (argv[0] == NULL)
	{
		printf("Error: Can't open file <file>\n");
		return (EXIT_FAILURE);
	}

	FILE *file_pointer = NULL;
	char *buffer = NULL, *opcode = NULL, *str = "push";
	size_t bytes_qty = 0;
	stack_t *head_list = NULL;
	int line_number = 1, value = 0, i = 0;
	char **tokens = NULL;

	file_pointer = fopen(*(argv + 1), "r");
	for (; getline(&buffer, &bytes_qty, file_pointer) != EOF; line_number++)
	{
		/* remove new line */
		buffer = new_line_remove(buffer);
		printf("buffer = %s\n", buffer);
		tokens = divide_line(buffer, " ");
		opcode = tokens[0];
		if(tokens[1])
			value = atoi(tokens[1]);
		else
			value = 0;

		printf("tokens[0] = %s | opcode = %s\n", tokens[0], opcode);
		printf("tokens[1] = %s | value = %d\n", tokens[1], value);

		printf("line = %d | opcode = %s | value = %d\n", line_number, opcode, value);
		/* get the opcode, no need to return */
		get_opcode_function(opcode, &head_list, line_number);
		/* *data = NULL ??????????? data = strtok(NULL, " , \n");
		printf("%s\n", data); */
	}
	fclose(file_pointer);
	free(buffer);
	return (0);
}
