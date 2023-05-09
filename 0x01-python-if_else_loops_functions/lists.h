#ifndef LISTS_H
#define LISTS_H

#include <stddef.h> // for size_t

/**
 * struct listint_s - singly linked list
 * @n: integer
 * @next: points to the next node
 *
 * Description: singly linked list node structure
 */
typedef struct listint_s
{
    int n;
    struct listint_s *next;
} listint_t;

/**
 * print_listint - prints all the elements of a listint_t list
 * @h: pointer to the head of the list
 * Return: the number of nodes in the list
 */
size_t print_listint(const listint_t *h);

/**
 * add_nodeint_end - adds a new node at the end of a listint_t list
 * @head: pointer to the head of the list
 * @n: integer to be added to the new node
 * Return: the address of the new element, or NULL if it fails
 */
listint_t *add_nodeint_end(listint_t **head, const int n);

/**
 * free_listint - frees a listint_t list
 * @head: pointer to the head of the list
 */
void free_listint(listint_t *head);

/**
 * insert_node - inserts a new node into a sorted listint_t list
 * @head: pointer to the head of the list
 * @number: integer to be added to the new node
 * Return: the address of the new element, or NULL if it fails
 */
listint_t *insert_node(listint_t **head, int number);

#endif /* LISTS_H */
