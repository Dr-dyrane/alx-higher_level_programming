# Project 0x03 - Python - Data Structures: Lists, Tuples

This project consists of a collection of Python functions that operate on different data structures such as lists, tuples, and strings. The functions perform various operations like printing elements, replacing values, removing characters, finding maximum values, and more. The goal of this project is to demonstrate an understanding of Python data structures and their manipulation.

## Functions

1. **print_integers(lst):**

   - Description: This function prints all the integers from a given list.
   - Input: `lst` - A list of elements.
   - Output: Prints the integers present in the list.

2. **get_element(lst, index):**

   - Description: This function retrieves an element from a list using the given index.
   - Input:
     - `lst` - A list of elements.
     - `index` - The index of the element to retrieve.
   - Output: Returns the element at the specified index.

3. **replace_element(lst, index, value):**

   - Description: This function replaces an element in a list at a specific position using the given value.
   - Input:
     - `lst` - A list of elements.
     - `index` - The index of the element to replace.
     - `value` - The value to replace the element with.
   - Output: Modifies the list by replacing the element at the specified index with the given value.

4. **print_integers_reverse(lst):**

   - Description: This function prints all the integers from a given list in reverse order.
   - Input: `lst` - A list of elements.
   - Output: Prints the integers present in the list in reverse order.

5. **replace_element_copy(lst, index, value):**

   - Description: This function replaces an element in a list at a specific position without modifying the original list.
   - Input:
     - `lst` - A list of elements.
     - `index` - The index of the element to replace.
     - `value` - The value to replace the element with.
   - Output: Returns a new list with the element at the specified index replaced with the given value, without modifying the original list.

6. **remove_characters(string, characters):**

   - Description: This function removes all occurrences of specified characters (c and C) from a given string.
   - Input:
     - `string` - The input string.
     - `characters` - A string containing the characters to be removed.
   - Output: Returns a new string with all occurrences of the specified characters removed.

7. **print_matrix(matrix):**

   - Description: This function prints a matrix of integers, where each row is represented by a list.
   - Input: `matrix` - A list of lists representing the matrix.
   - Output: Prints the matrix in a well-formatted manner.

8. **add_tuples(tuple1, tuple2):**

   - Description: This function adds two tuples element-wise and returns a new tuple as the result.
   - Input:
     - `tuple1` - The first input tuple.
     - `tuple2` - The second input tuple.
   - Output: Returns a new tuple where each element is the sum of the corresponding elements from the input tuples.

9. **string_length_and_first_char(string):**

   - Description: This function returns a tuple with the length of a given string and its first character.
   - Input: `string` - The input string.
   - Output: Returns a tuple containing the length of the string (integer) and its first character (string).

10. **find_max_integer(lst):**
    - Description: This function finds the biggest integer in a given list.

- Input: `lst` - A list of integers.
- Output: Returns the maximum integer value present in the list.

11. **find_multiples_of_two(lst):**

    - Description: This function finds all the multiples of 2 in a given list and returns a new list containing only those values.
    - Input: `lst` - A list of integers.
    - Output: Returns a new list that contains only the integers from the input list that are multiples of 2.

12. **delete_element(lst, index):**

    - Description: This function deletes the item at a specific position in a list.
    - Input:
      - `lst` - A list of elements.
      - `index` - The index of the item to delete.
    - Output: Modifies the list by removing the item at the specified index.

13. **switch_values(a, b):**

    - Description: This function switches the values of variables `a` and `b`.
    - Input:
      - `a` - First variable.
      - `b` - Second variable.
    - Output: Modifies the values of `a` and `b` by swapping their contents.

14. **is_palindrome_singly_linked_list(head):**
    - Description: This function checks if a singly linked list is a palindrome.
    - Input: `head` - The head node of the linked list.
    - Output: Returns a boolean value (`True` or `False`) indicating whether the linked list is a palindrome or not.
