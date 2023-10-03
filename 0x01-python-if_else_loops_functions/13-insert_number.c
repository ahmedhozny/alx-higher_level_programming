#include "lists.h"

/**
 * insert_node - inserts new number in a sorted linked list
 * @head: pointer the head of the linked list
 * @number: number to insert
 *
 * Return: pointer to the inserted node. Null on failure
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new_node;
	listint_t *c_node = *head;

	new_node = malloc(sizeof(listint_t));
	if (new_node == NULL)
		return (NULL);
	new_node->n = number;

	if (c_node == NULL || c_node->n >= number)
	{
		new_node->next = c_node;
		*head = new_node;
		return (new_node);
	}

	while (c_node->next)
	{
		if (c_node->next->n >= number)
			break;
		c_node = c_node->next;
	}

	new_node->next = c_node->next;
	c_node->next = new_node;
	return (new_node);
}
