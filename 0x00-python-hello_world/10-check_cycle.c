#include "lists.h"
/**
 * check_cycle - check if list is cycle
 * @list: type listint_t
 * Return: always int
 * case: 1 true, 0 false
 */
int check_cycle(listint_t *list)
{
listint_t *chk = list, *has = list;
while (chk != NULL && has != NULL && has->next != NULL)
{
chk = chk->next;
has = has->next->next;
if (chk == has)
return (1);
}
return (0);
}
