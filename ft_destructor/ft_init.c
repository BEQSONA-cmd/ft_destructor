/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_init.c                                          :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: btvildia <btvildia@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2024/05/04 14:08:30 by escura            #+#    #+#             */
/*   Updated: 2024/05/11 16:45:56 by btvildia         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "ft_alloc.h"

bool	ft_alloc_init(void)
{
	t_allocs	*lst;

	lst = ft_my_calloc(1, sizeof(t_allocs));
	if (lst == NULL)
		return (false);
	ft_allocs(lst);
	return (true);
}
