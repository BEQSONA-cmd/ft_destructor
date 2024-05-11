
# FT_DESTRUCTOR

A lightweight C library that automates memory cleanup. It ensures all allocated memory is properly freed in case of allocation fail or at program exit.
In short it's simplifying memory management and minimizing memory leaks.


## Installation

Install library on machine
```bash
cd && git clone https://github.com/BEQSONA-cmd/ft_destructor.git && cd ft_destructor && sh install.sh
```

## Getting Started

Run command in terminal and follow steps for implement library 
```bash
fix_leaks
```

## Functions

- Init / Get the list with all allocations
```c
t_allocs *ft_allocs(t_allocs *lst);
````
- Allocations
```c
void *ft_malloc(size_t size);
void *ft_my_calloc(size_t count, size_t size)
```
- Destructors
```c
void ft_free(void *ptr);
void ft_destructor(void);
```

## Demo
```c
#include "ft_alloc.h"

int	main(void)
{
	// init list for allocations
	ft_alloc_init();

	// allocations with ft_malloc
	char *str = ft_malloc(455 * sizeof(char));
	char *str2 = ft_malloc(455 * sizeof(char));
	char *str3 = ft_malloc(455 * sizeof(char));

	// manual free
	ft_free(str);  
	ft_free(str2);
	ft_free(str3);

	int i = 0;
	while (i < 10)
	{
		// allocation without ft_free
		char *str4 = ft_malloc(455 * sizeof(char));
		(void)str4;
		i++;
	}

	// original malloc - won't be freed with destructor
	char *str5 = malloc(455 * sizeof(char)); 
	(void)str5;

	// will free everything that was allocated with ft_malloc or ft_my_calloc
	ft_destructor(); 
	return (0);
}
```
## Feedback

If you have any feedback, please reach out to me at discord: emsa001

