#include <stdio.h>
#include <stdlib.h>
#include "lists.h"

/**
 *stack_push - pushes a value onto the stack
 *@stack: double pointer to the top of the stack
 *@value: value to be pushed
 *
 *Return: pointer to the updated top of the stack
 */
void stack_push(listint_t **stack, int value)
{
	listint_t *new_node = malloc(sizeof(listint_t));

	if (new_node == NULL)
	{
		fprintf(stderr, "Error: Failed to allocate memory\n");
		exit(EXIT_FAILURE);
	}

	new_node->n = value;
	new_node->next = *stack;
	*stack = new_node;
}

/**
 *stack_pop - pops a value from the stack
 *@stack: double pointer to the top of the stack
 *
 *Return: the popped value
 */
int stack_pop(listint_t **stack)
{
	if (*stack == NULL)
	{
		fprintf(stderr, "Error: Stack is empty\n");
		exit(EXIT_FAILURE);
	}

	int value = (*stack)->n;
	listint_t *temp = *stack;
	*stack = (*stack)->next;
	free(temp);

	return (value);
}

/**
 *is_palindrome - checks if a singly linked list is a palindrome
 *@head: double pointer to the head of the linked list
 *
 *Return: 1 if the list is a palindrome, 0 otherwise
 */
int is_palindrome(listint_t **head)
{
	listint_t *slow = *head;
	listint_t *fast = *head;
	listint_t *stack = NULL;

	if (*head == NULL || (*head)->next == NULL)
		return (1);

	/*Push the first half of the linked list onto the stack */
	while (fast != NULL && fast->next != NULL)
	{
		stack_push(&stack, slow->n);
		slow = slow->next;
		fast = fast->next->next;
	}

	/*If the linked list has odd number of nodes, skip the middle element */
	if (fast != NULL)
		slow = slow->next;

	/*Compare the second half of the linked list with the values in the stack */
	while (slow != NULL)
	{
		int value = stack_pop(&stack);

		if (slow->n != value)
			return (0);
		slow = slow->next;
	}

	return (1);
}
