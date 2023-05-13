#include <stdlib.h>
#include "lists.h"

/**
 *reverse_list - reverses a linked list
 *@head: double pointer to the head of the linked list
 *
 *Return: pointer to the new head of the reversed list
 */
listint_t *reverse_list(listint_t **head)
{
	if (*head == NULL || (*head)->next == NULL)
		return (*head);

	listint_t *prev = NULL;
	listint_t *current = *head;
	listint_t *next;

	while (current != NULL)
	{
		next = current->next;
		current->next = prev;
		prev = current;
		current = next;
	}

	*head = prev;

	return (prev);
}

/**
 *is_palindrome - checks if a singly linked list is a palindrome
 *@head: double pointer to the head of the linked list
 *
 *Return: 1 if the list is a palindrome, 0 otherwise
 */
int is_palindrome(listint_t **head)
{
	if (*head == NULL || (*head)->next == NULL)
		return (1);

	listint_t *slow = *head;
	listint_t *fast = *head;

	/*Find the middle of the list */
	while (fast != NULL && fast->next != NULL)
	{
		fast = fast->next->next;
		slow = slow->next;
	}

	/*Reverse the second half of the list */
	listint_t *reversed = reverse_list(&slow);

	/*Compare the first half and reversed second half */
	listint_t *temp1 = *head;
	listint_t *temp2 = reversed;

	while (temp1 != NULL && temp2 != NULL)
	{
		if (temp1->n != temp2->n)
			return (0);
		temp1 = temp1->next;
		temp2 = temp2->next;
	}

	/*Restore the original list by reversing the second half again */
	reverse_list(&reversed);

	return (1);
}
