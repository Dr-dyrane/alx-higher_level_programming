#include "lists.h"

/**
 * check_cycle - checks if a singly linked list has a cycle in it
 * @list: pointer to the head of the list
 * Return: 1 if there is a cycle, 0 otherwise
 */
int check_cycle(listint_t *list)
{
    listint_t *slow, *fast;

    if (list == NULL || list->next == NULL)
        return (0);

    slow = list;
    fast = list->next;

    while (fast != NULL && fast->next != NULL && fast->next->next != NULL)
    {
        if (fast == slow || fast->next == slow)
            return (1);
        fast = fast->next->next;
        slow = slow->next;
    }

    return (0);
}
