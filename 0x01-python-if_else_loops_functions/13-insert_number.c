#include "lists.h"

/**
 * *insert_node - inserts a number into a sorted singly linked list
 * @head: first node of the list
 * @number: number to be inserted
 *
 * Return: address of the new node, or NULL if it failed
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *newnode, *num1 = *head, *num2 = *head, *num3 = *head;
	unsigned int index = 0, len = 0;

	newnode = malloc(sizeof(listint_t));
	if (newnode == NULL)
		return (NULL);
	newnode->n = number;
	newnode->next = NULL;
	if (*head == NULL)
	{
		newnode->next = *head;
		*head = newnode;
		return (newnode);
	}
	while (num1->next)
	{
		len++;
		num3 = num3->next;
		if (num1->n > number)
		{
			len--;
			break;
		}
		else if (num1->next->next == NULL && num3->n < number)
		{
			len++;
			break;
		}
		num1 = num1->next;
	}
	if (len == 0)
	{
		newnode->next = *head;
		*head = newnode;
		return (newnode);	}
	while (num2 != NULL && index < len - 1)
	{
		num2 = num2->next;
		index++;
	}
	if (index == len - 1)
	{	newnode->next = num2->next;
		num2->next = newnode;
		return (newnode);
	}
	return (NULL);
}
