#include "monty.h"

/**
* divide_line - divides a line
* @line: line to be divided
* @delim: delimitator
* Return: array of arguments
*/

char **divide_line(char *line, char *delim)
{
	char **tokens = NULL;
	int i = 0, j = 0, coun_tokens = 0;

	coun_tokens = _count_token(line, delim);
	if (coun_tokens == 0 || !line)
		return (NULL);
	tokens = malloc(sizeof(char *) * (coun_tokens + 1));
	if (tokens == NULL)
		return (NULL);
	while (line[i] != '\0')
	{
		if (i == 0 && line[i] == ' ')
		{
			while (line[i + 1] == ' ' && j == 0)
				i++;
			i++;
			tokens[j] = line + i;
			j++;
		}
		if (i == 0 && line[i] != ' ')
		{
			tokens[j] = line;
			j++;
		}
		while (line[i + 1] == *delim || line[i + 1] == ' ')
		{
			i++;
			line[i] = '\0';
			while (line[i + 1] == ' ')
			{
				i++;
				line[i] = '\0';
			}
			i++;
			tokens[j++] = line + i;
		}
		i++;
	}
	tokens[coun_tokens] = NULL;
	return (tokens);
}

/**
 *  _count_token - divides a line
 *  @line: line to be divided
 *  @delim: delimitator
 *
 *  Return: array of arguments
 */
int _count_token(char *line, char *delim)
{
	int coun_tokens = 0, i = 0;

	while (line[i] != '\0')
	{
		if (line[i] == ' ')
			i++;
		else
		{
			if (line[i + 1] == ' ' || line[i + 1] == '\0'
			|| line[i + 1] == *delim)
				coun_tokens++;
			i++;
		}
	}
	return (coun_tokens);
}
