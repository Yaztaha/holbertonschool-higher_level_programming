#include <stdlib.h>
#include <string.h>
#include <stdio.h>
#include "lists.h"

/**
 * insert_node - inserts node in a sorted linked list
 * @head: double pointer to the beginning of the linked list
 * @number: number to be placed in new node
 * Return: Address of the new node or NULL if failed
 */

listint_t *insert_node(listint_t **head, int number)
{
	listint_t *compare;
	listint_t *newnode;

	if (head == NULL)
		return (NULL);
	newnode = malloc(sizeof(listint_t));
	if (newnode == NULL)
		return (NULL);
	newnode->n = number;
	if (*head == NULL || newnode->n < (*head)->n)
	{
		newnode->next = *head;
		*head = newnode;
	}
	else
	{
		compare = *head;
		while (compare->next != NULL)
		{
			if (compare->next->n > newnode->n)
				break;
			compare = compare->next;
		}
		newnode->next = compare->next;
		compare->next = newnode;
	}
	return (newnode);
}
