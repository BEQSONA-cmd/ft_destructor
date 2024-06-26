/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_destructors.c                                   :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: btvildia <btvildia@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2024/05/04 14:12:49 by escura            #+#    #+#             */
/*   Updated: 2024/05/11 15:37:27 by btvildia         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "ft_alloc.h"

void	ft_free(void *ptr)
{
	t_allocs	*lst;
	t_allocs	*tmp;

	lst = ft_allocs(NULL);
	tmp = NULL;
	if (!ptr)
		return ;
	while (lst != NULL)
	{
		if (lst->ptr == ptr)
		{
			tmp->next = lst->next;
			free(lst->ptr);
			free(lst);
			return ;
		}
		tmp = lst;
		lst = lst->next;
	}
	free(ptr);
}

void	ft_destructor(void)
{
	t_allocs	*lst;
	t_allocs	*temp;

	lst = ft_allocs(NULL);
	if (DEBUG)
		printf("Passing %d allocations to destructor\n", ft_allocsize());
	while (lst != NULL)
	{
		temp = lst;
		lst = lst->next;
		if (temp->ptr != NULL)
		{
			if (DEBUG)
				printf("Freeing using destructor %p\n", temp->ptr);
			free(temp->ptr);
			temp->ptr = NULL;
		}
		free(temp);
	}
	free(lst);
}

void	ft_exit(int status)
{
	ft_destructor();
	exit(status);
}
