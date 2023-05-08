#ifndef LISTS_H
#define LISTS_H

#include <stdlib.h>

/**
 * struct listint_s - singly linked list
 * @n: integer
 * @next: points to the next node
 *
 * Description: singly linked list node structure
 * 
 */
typedef struct listint_s
{
    int n;
    struct listint_s *next;
} listint_t;

size_t print_listint(const listint_t *h);
/* This function prints all the elements of a linked list */
/* It takes a pointer to the head of the list as an argument */
/* and returns the number of nodes in the list */

listint_t *add_nodeint(listint_t **head, const int n);
/* This function adds a new node at the beginning of a linked list */
/* It takes a double pointer to the head of the list as its first argument */
/* and the data to be stored in the new node as its second argument */
/* It returns a pointer to the new node on success, or NULL on failure */

void free_listint(listint_t *head);
/* This function frees a linked list */
/* It takes a pointer to the head of the list as an argument */

int check_cycle(listint_t *list);
/* This function checks if a linked list has a cycle in it */
/* It takes a pointer to the head of the list as an argument */
/* It returns 1 if there is a cycle, and 0 otherwise */

#endif /* LISTS_H */
