#include "lists.h"
#include <stddef.h>

/**
 * is_palindrome - checks if a singly linked list is a palindrome
 * @head: pointer to head of list
 * Return: 0 if it is not a palindrome, 1 otherwise
 */
int is_palindrome(listint_t **head)
{
	listint_t *node, *newnode, *prev_node;
	listint_t *scanf, *middle;
	int is_pal = 1;

	node = newnode = prev_node = *head;
	middle = NULL;
	if (*head != NULL && (*head)->next != NULL)
	{
		while (newnode != NULL && newnode->next != NULL)
		{
			newnode = newnode->next->next;
			prev_node = node;
			node = node->next;
		}
		if (newnode != NULL)
		{
			middle = node;
			node = node->next;
		}
		scanf = node;
		prev_node->next = NULL;
		reverse(&scanf);
		is_pal = compare(*head, scanf);
		if (middle != NULL)
		{
			prev_node->next = middle;
			middle->next = scanf;
		}
		else
		{
			prev_node->next = scanf;
		}
	}
	return (is_pal);
}

/**
 * reverse - reverses the second half of the list
 * @h_r: head of the second half
 * Return: Nothing.
 */
void reverse(listint_t **h_r)
{
	listint_t *previous;
	listint_t *current;
	listint_t *new;

	previous = NULL;
	current = *h_r;
	while (current != NULL)
	{
		new = current->next;
		current->next = previous;
		previous = current;
		current = new;
	}
	*h_r = previous;
}

/**
 * compare - compares each int of the list
 * @h1: head of the first half
 * @h2: head of the second half
 * Return: 1 if are equals, 0 if not
 */
int compare(listint_t *h1, listint_t *h2)
{
	listint_t *temp_1;
	listint_t *temp_2;

	temp_1 = h1;
	temp_2 = h2;
	while (temp_1 != NULL && temp_2 != NULL)
	{
		if (temp_1->n == temp_2->n)
		{
			temp_1 = temp_1->next;
			temp_2 = temp_2->next;
		}
		else
		{
			return (0);
		}
	}
	if (temp_1 == NULL && temp_2 == NULL)
	{
		return (1);
	}
	return (0);
}
