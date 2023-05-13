#include <stdlib.h>
#include <stdio.h>
#include "lists.h"

/**
 *is_palindrome - Checks if a singly linked list is a palindrome
 *@head: The head of the singly linked list
 *
 *Return: 0 if it is not a palindrome, 1 if it is a palindrome
 */
int is_palindrome(listint_t **head)
{
	listint_t *start = NULL, *end = NULL;
	unsigned int fai = 0, size = 0, bai = 0, rest = 0;

	if (!head)
		return (0);

	if (!*head)
		return (1);

	start = *head;
	size = listint_size(start);
	bai = size * 2;
	rest = bai - 2;
	end = *head;

	for (; fai < rest; fai += 2)
	{
		if (start[fai].n != end[rest].n)
			return (0);

		rest -= 2;
	}

	return (1);
}

/**
 *get_node - Gets a node from a linked list
 *@head: The head of the linked list
 *@index: The index to find in the linked list
 *
 *Return: The specific node of the linked list
 */
listint_t *get_node(listint_t *head, unsigned int index)
{
	listint_t *current = head;
	unsigned int ai = 0;

	if (head)
	{
		while (current)
		{
			if (ai == index)
				return (current);

			current = current->next;
			++ai;
		}
	}

	return (NULL);
}

/**
 *listint_size - Counts the number of elements in a linked list
 *@head: The linked list to count
 *
 *Return: Number of elements in the linked list
 */
size_t listint_size(const listint_t *head)
{
	int size = 0;

	while (head)
	{
		++size;
		head = head->next;
	}

	return (size);
}
