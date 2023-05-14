#include <stdlib.h>
#include "lists.h"

/**
 *is_palindrome - Checks if a singly linked list is a palindrome
 *@head: The head of the singly linked list
 *
 *Return: 0 if it is not a palindrome, 1 if it is a palindrome
 */
int is_palindrome(listint_t **head)
{
	/*Declare variables */
	listint_t *jagger = NULL; /*Forward pointer */
	listint_t *hendrix = NULL; /*Backward pointer */
	listint_t *plant = NULL; /*Previous pointer */
	listint_t *page = NULL; /*Temporary pointer */
	listint_t *bono = NULL; /*Middle pointer */
	/*Check for invalid input */
	if (!head)
		return (0);
	/*Check for an empty list (considered a palindrome) */
	if (!*head)
		return (1);
	/*Initialize the forward and backward pointers */
	jagger = hendrix = *head;
	/*Iterate forward and backward simultaneously */
	while (jagger && jagger->next)
	{
		/*Move the pointers forward and backward */
		jagger = jagger->next->next;
		page = hendrix;
		hendrix = hendrix->next;
		page->next = plant;
		plant = page;
	}
	/*Adjust the pointers if the list has an odd number of elements */
	bono = jagger ? hendrix->next : hendrix;
	/*Compare the elements of the two halves */
	while (plant && bono)
	{
		if (plant->n != bono->n)
			return (0); /*Not a palindrome */

		plant = plant->next;
		bono = bono->next;
	}

	/*All elements compared, it is a palindrome */
	return (1);
}
