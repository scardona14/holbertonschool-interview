# Find the Loop

## Description

This project involves detecting a loop in a singly linked list. The goal is to write a function that can identify the start of a loop in the list, if one exists.

## Requirements

### General

- Allowed editors: `vi`, `vim`, `emacs`
- All your files will be compiled on Ubuntu 14.04 LTS
- Your programs and functions will be compiled with `gcc 4.8.4` using the flags `-Wall -Werror -Wextra` and `-pedantic`
- All your files should end with a new line
- A `README.md` file at the root of the folder of the project is mandatory
- Your code should use the **Betty style**. It will be checked using `betty-style.pl` and `betty-doc.pl`
- You are not allowed to use global variables
- No more than 5 functions per file
- No standard library functions allowed. Any use of functions like `printf`, `puts`, `calloc`, `realloc`, etc., is forbidden
- The prototypes of all your functions should be included in your header file called `lists.h`
- Don’t forget to push your header file
- All your header files should be **include guarded**

### `lists.h`

The following `lists.h` file should be used:

```c
#ifndef _LISTS_H_
#define _LISTS_H_

#include <stddef.h>

/**
 * struct listint_s - singly linked list
 * @n: integer
 * @next: points to the next node
 *
 * Description: singly linked list node structure
 * for Holberton project
 */
typedef struct listint_s
{
    int n;
    struct listint_s *next;
} listint_t;

listint_t *add_nodeint(listint_t **head, const int n);
size_t print_listint_safe(const listint_t *head);
size_t free_listint_safe(listint_t **h);

listint_t *find_listint_loop(listint_t *head);

#endif
