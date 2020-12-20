#include "monty.h"

int main(int argc, char **argv)
{
	FILE *fp = NULL;
	char str1[10], str2[10], str3[10], str4[10];
	int idx = 0, i = 0;
	char *line = NULL, *token;
	size_t size = 0;

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

	fp = fopen(argv[1], "r");

	for (i = 1; getline(&line, &size, fp) != EOF; i++)
	{
		printf("line %d = %s", i, line);
		token = strtok(line, " ");
		while (token != NULL)
		{
			printf("token %d %s\n", i, token);
			token = strtok(NULL, " ");
		}
	}

	//printf("argc = %d || argv = %s || argv = %s \n", argc, argv[0], argv[1]);
	/*while(1)
	{
		idx = fgetc(fp);
		if (idx == '\n')
			printf("\nHay un salto de linea\n");
		if(feof(fp))
			break;
		printf("%c", idx);
	}*/
	//fprintf(fp, "%s %s %s %d", "We", "are", "in", 2012);
	printf("afuera\n");
	fclose(fp);
	return (0);
}