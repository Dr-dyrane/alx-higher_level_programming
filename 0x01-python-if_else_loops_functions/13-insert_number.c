#include "lists.h"

/**
 * insert_node - Insert a number into a sorted singly-linked list.
 * @head: A pointer to the head of the linked list.
 *
 * @number: The number to insert.
 * Return: 0 if the function fails or a pointer to the new node.
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *current = *head, new_node;

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

	while (current && current->next && current->next->n < number)
		current = current->next;
	new_node->next = current->next;
	node->next = new;

	return (new);
}
