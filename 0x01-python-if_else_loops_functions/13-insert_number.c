#include "lists.h"

/**
 * insert_node is a function to add a number into a sorted singly linked list;
 * @head: is a pointer to pointed head;
 * @number: is a number to be add it to singly linked list;
 *
 * Return: address of new node otherwise NULL if failed.
 */
listint_t *insert_node(listint_t **head, int number)
{
	int num;
	listint_t *current = *head;
	listint_t *new_node;

	new_node = malloc(sizeof(listint_t));
	if (new_node == NULL)
		return (NULL);
	new_node->n = number;

	if (current == NULL || current->n >= number)
	{
		new_node->next = current;
		*head = new_node;

		return (new_node);
	}

	while (current && current->next)
	{
		num = current->next->n;
		if (number > num)
			current = current->next;
		else
			break;
	}

	new_node->next = current->next;
	current->next = new_node;

	return (new_node);
}
