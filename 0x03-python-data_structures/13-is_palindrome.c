#include "lists.h"

/**
 * strlength - returns length of a string
 * @str: string to be assessed
 * Return: length of string
 */

int strlength(char *str)
{
	if (*str == '\0')
		return (0);
	return (strlength(str + 1) + 1);
}

/**
 * check_palindrome - check if string is a palindrome
 * @str: string to be assessed
 * @start: first index
 * @end: end index
 * Return: 1 if palindrome, 0 if not palindrome
 */

int check_palindrome(char *str, int start, int end)
{
	if (str[start] != str[end])
		return (0);
	if (start >= end)
		return (1);
	return (check_palindrome(str, start + 1, end - 1));
}

/**
 * is_palin_str - determine if string is a palindrome
 * @str: string to be assessed
 * Return: 1 if string is palindrome and 0 if not
 */

int is_palin_str(char *str)
{
	int end;

	if (*str == '\0')
		return (1);
	end = strlength(str) - 1;
	return (check_palindome(str, 0, end));
}

/**
 * is_palindrome - check if a singly linked list is a palindrome
 *
 * @head: start of linked list
 * Return: 0 if it is not a palindrome, 1 if it is a palindrome
 */

int is_palindrome(listint_t **head)
{
	listint_t *temp = NULL;
	listint_t *current = NULL;
	char *str;
	int size = 0;
	int ai = 0;

	if (*head == NULL || head == NULL)
		return (1);

	current = *head;
	while (current != NULL)
	{
		current = current->next;
		size++;
	}

	str = malloc(sizeof(int) * size);
	if (str == NULL)
		return (-1);

	temp = *head;

	while (temp != NULL)
	{
		str[ai] = temp->n;
		temp = temp->next;
		ai++;
	}

	if (is_palin_str(str) == 1)
	{
		free(str);
		return (1);
	}
	free(str);
	return (0);
}
