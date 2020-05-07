#include <stdio.h>
#include <stdlib.h>
#include "lists.h"

int is_palindrome(listint_t **head)
{
	listint_t *t = *head;
	int x = 0, i = 0, y = 0, z[4000];
	if (!t || !t->next)
		return (1);
	for (; t; x++, t = t->next)
	{
		z[x] = t->n;
	}
	z[x] = '\0';
	for (y = x - 1; y >= x / 2; y--, i++)
	{
		if (z[y] != z[i])
			return (0);
	}
	return (1);
}
