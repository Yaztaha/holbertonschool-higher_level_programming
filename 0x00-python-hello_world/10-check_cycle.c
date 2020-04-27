#include "lists.h"

/**
 * check_cycle - check if a list has a loop.
 * Return: 0 if there is no cycle, 1 if there is a cycle.
 * @list: list to be checked.
 */

int check_cycle(listint_t *list)
{
	listint_t *x;
	listint_t *y;

	if (!list)
		return (0);
	x = list;
	y = list->next;
	while (x != y)
	{
		x = x->next;
		if (!x)
			return (0);
		y = y->next;
		if (!y)
			return (0);
		y = y->next;
		if (!y)
			return (0);
	}
	return (1);
}
