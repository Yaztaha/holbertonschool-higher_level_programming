#include "lists.h"

/**
 * insert_node - Inserts a number into a sorted singly linked list.
 *
 * @head: head of linked list..
 * @number: number for the new node.
 * Return: address of the new node, or NULL if it failed.
 */

listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new, *step, *temp;

	if (!head)
		return (NULL);

	new = malloc(sizeof(listint_t));
	if (!new)
		return (NULL);

	new->n = number;
	step = *head;
	temp = *head;

	if (*head == NULL)
	{
		*head = new;
		new->next = NULL;
		return (new);
	}
	if (new->n < step->n)
	{
		*head = new;
		new->next = step;
		return (new);
	}
	while (step->next)
	{
		step = step->next;
		if (new->n < step->n)
		{
			temp->next = new;
			new->next = step;
			return (new);
		}
		temp = temp->next;
	}
	step->next = new;
	new->next = NULL;
	return (new);
}
