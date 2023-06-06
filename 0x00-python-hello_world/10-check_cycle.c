#include "lists.h"

/**
 * check_cycle - a function to check if a singly linked list has a cycle in it;
 * @list: is a singly linked list to be checked;
 *
 * Return: value 0 if no cycle otherwise return 1.
 */
int check_cycle(listint_t *list)
{
	listint_t *hare = list;
	listint_t *tortoise = list;

	if (list == NULL)
		return (0);

	while (tortoise && hare && hare->next)
	{
		tortoise = tortoise->next;
		hare = hare->next->next;

		if (hare == tortoise)
			return (1);
	}

	return (0);
}
