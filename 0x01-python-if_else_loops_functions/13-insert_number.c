#include "lists.h"

/**
 * insert_node - inserts number into a sorted singly linked list
 *
 * @head: linked list
 * @number: value to be assigned to new node
 * Return: address of new node or NULL if fail
 */

listint_t *insert_node(listint_t **head, int number)
{
	listint_t *slowpoke = NULL; /* pointer to current node */
	listint_t *speedygonzales = NULL; /* pointer to new node */

	slowpoke = *head;

	speedygonzales = malloc(sizeof(listint_t)); /* allocate memory for new node */
	if (speedygonzales == NULL) /* check if allocation fails */
		return (NULL);

	speedygonzales->n = number; /* assign value to new node */
	speedygonzales->next = NULL;

	/* check if head is null or if new node is less than head */
	if (*head == NULL || speedygonzales->n < slowpoke->n)
	{
		speedygonzales->next = *head; /* make new node point to head */
		*head = speedygonzales; /* update head to new node */
		return (speedygonzales); /* return address of new node */
	}

	/* loop through list to find the correct position for new node */

	while (slowpoke->next != NULL && (slowpoke->n < speedygonzales->n)
	       && ((slowpoke->next)->n < speedygonzales->n))
		slowpoke = slowpoke->next;

	/* make new node point to the next node after current node */
	speedygonzales->next = slowpoke->next;
	slowpoke->next = speedygonzales; /* make current node point to new node */
	return (speedygonzales); /* return address of new node */
}
