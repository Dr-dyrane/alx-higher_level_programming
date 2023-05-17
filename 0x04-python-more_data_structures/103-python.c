#include <stdio.h>
#include <stdlib.h>
#include "/usr/include/python3.4/Python.h"
/**
 *print_hexn - Print the hexadecimal representation of a string up to n bytes
 *@str: The input string
 *@n: Number of bytes to print
 *
 *Return: Nothing
 */
void print_hexn(const char *str, int n)
{
	int ai = 0;

	for (; ai < n - 1; ++ai)
		printf("%02x ", (unsigned char) str[ai]);

	printf("%02x", str[ai]);
}
/**
 *print_python_bytes - Print the information of a Python bytes object
 *@p: PyObject representing the Python bytes object
 *
 *Return: Nothing
 */
void print_python_bytes(PyObject *p)
{
	PyBytesObject *clone = (PyBytesObject *) p;
	int calc_bytes, clone_size = 0;

	printf("[.] bytes object info\n");
	if (PyBytes_Check(clone))
	{
		clone_size = PyBytes_Size(p);
		calc_bytes = clone_size + 1;

		if (calc_bytes >= 10)
			calc_bytes = 10;

		printf("  size: %d\n", clone_size);
		printf("  trying string: %s\n", clone->ob_sval);
		printf("  first %d bytes: ", calc_bytes);
		print_hexn(clone->ob_sval, calc_bytes);
		printf("\n");
	}
	else
	{
		printf("  [ERROR] Invalid Bytes Object\n");
	}
}
/**
 *print_python_list - Print some basic info about Python lists
 *@p: PyObject representing the Python list
 *
 *Return: Nothing
 */
void print_python_list(PyObject *p)
{
	int ai = 0, list_len = 0;
	PyObject *item;
	PyListObject *clone = (PyListObject *) p;

	printf("[*] Python list info\n");
	list_len = PyList_GET_SIZE(p);
	printf("[*] Size of the Python List = %d\n", list_len);
	printf("[*] Allocated = %d\n", (int) clone->allocated);

	for (; ai < list_len; ++ai)
	{
		item = PyList_GET_ITEM(p, ai);
		printf("Element %d: %s\n", ai, item->ob_type->tp_name);

		if (PyBytes_Check(item))
			print_python_bytes(item);
	}
}
