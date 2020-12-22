#include "monty.h"

/*main*/
int main(int argc, char **argv)
{
	char *opcode = NULL, *token_1 = NULL;
	int value = 0;
	var_t.line_number = 1;
	(void)token_1;
	/*FILE *file_pointer = NULL;
	//char *buffer = NULL;*/

	/*/size_t bytes_qty = 0;
	//stack_t *head_list = NULL;
	//int line_number = 1;*/


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

	/*Abro el archivo*/
	var_t.file_pointer = fopen(*(argv + 1), "r");
	/*Asigno tokens a variables y llamo la funcion que busca funciones*/
	for (; getline(&var_t.buffer, &var_t.bytes_qty, var_t.file_pointer) != EOF; var_t.line_number++)
	{
		/* remove new line */
		var_t.buffer = new_line_remove(var_t.buffer);
		printf("buffer = %s\n", var_t.buffer);
		opcode = strtok(var_t.buffer, " ");
		printf("opcode %s\n", opcode);
		/*token_1 = strtok(NULL, " ");
		if (token_1)
			value = atoi(token_1);
		else
			value = 0;
		printf("value %d\n", value);*/
		printf("line = %d | opcode = %s | value = %d\n", var_t.line_number, opcode, value);
		/* get the opcode, no need to return */
		get_opcode_function(opcode, &var_t.head_list, var_t.line_number);
		/* *data = NULL ??????????? data = strtok(NULL, " , \n");
		printf("%s\n", data); */
	}
	fclose(var_t.file_pointer);

	free_dlistint();
	free(var_t.buffer);
	return (0);
}
