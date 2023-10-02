#include "lists.h"

/**
 * check_cycle - checks if a linked list has a cycle
 * @list: list to check
 *
 * Return: 1 if list has a cycle, 0 if not
 */
int check_cycle(listint_t *list)
{
	listint_t jumper1 = *list;
	listint_t jumper2 = *list;

	if (!list)
		return (0);

	while (jumper1 && jumper2 && jumper2.next)
	{
		jumper1 = jumper1.next;
		jumper2 = jumper2.next.next;
		if (jumper1 == jumper2)
			return (1);
	}

	return (0);
}
