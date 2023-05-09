#include "lists.h"

/**
 * insert_node - Inserts a number into a sorted singly linked list
 *
 * @head: Pointer to the head node of the list
 * @number: Number to be inserted into the list
 *
 * Return: Address of the new node, or NULL on failure
 */
listint_t *insert_node(listint_t **head, int number)
{
    listint_t *new_node = malloc(sizeof(*new_node));
    if (!new_node)
        return (NULL);

    new_node->n = number;

    if (!*head || (*head)->n >= number)
    {
        new_node->next = *head;
        *head = new_node;
    }
    else
    {
        listint_t *current = *head;

        while (current->next && current->next->n < number)
            current = current->next;

        new_node->next = current->next;
        current->next = new_node;
    }

    return (new_node);
}
