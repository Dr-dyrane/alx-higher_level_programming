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

	/*Check for invalid input */
	if (!head)
		return (0);

	/*Empty list is considered a palindrome */
	if (!*head)
		return (1);

	/*Assign the value of head to start pointer */
	start = *head;
	/*Calculate the number of elements in the linked list and assign it to size */
	size = listint_size(start);
	/*Multiply the size by 2 and assign it to bai (used for backward iteration) */
	bai = size * 2;
	/*Subtract 2 from bai and assign it to rest (used for forward iteration) */
	rest = bai - 2;
	/*Assign the value of head to end pointer */
	end = *head;

	/*Compare elements from both ends of the list */
	for (; fai < rest; fai += 2)
	{
		/*If values don't match, it's not a palindrome */
		if (start[fai].n != end[rest].n)
			return (0);

		rest -= 2;
	}

	/*All elements compared, it's a palindrome */
	return (1);
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

	/*Traverse the linked list and count the elements */
	while (head)
	{
		/*Increase the size counter */
		++size;

		/*Move to the next node */
		head = head->next;
	}

	return (size);
}
