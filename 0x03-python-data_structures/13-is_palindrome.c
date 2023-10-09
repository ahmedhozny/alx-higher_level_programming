#include "lists.h"

/**
 * is_palindrome - checks if a linked list is palindrome
 * @head: head of the list
 *
 * Return: 1 if list is palindrome, 0 if it is not.
 */
int is_palindrome(listint_t **head)
{
	listint_t *cur, *cur2, *prev, *next;

	if (*head == NULL || (*head)->next == NULL)
		return (1);
	cur = *head, cur2 = *head;

	while (cur->next != NULL && cur2->next != NULL && cur2->next->next != NULL)
	{
		cur = cur->next;
		cur2 = cur2->next->next;
	}
	cur2 = cur;
	cur = cur->next;
	prev = NULL, next = NULL;
	while (cur != NULL)
	{
		next = cur->next;
		cur->next = prev;
		prev = cur;
		cur = next;
	}

	cur2->next = prev;
	cur = *head, cur2 = cur2->next;
	while (cur != NULL && cur2 != NULL)
	{
		if (cur->n != cur2->n)
			return (0);
		cur = cur->next;
		cur2 = cur2->next;
	}

	return (1);
}
