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
	int ai;
	/*Iterate over the string bytes */
	for (ai = 0; ai < n - 1; ai++)
		/*Print the hexadecimal representation of each byte */
		printf("%02x ", (unsigned char) str[ai]);
	printf("%02x", str[i]);
	printf("\n");
}
/**
 *print_python_bytes - Print the information of a Python bytes object
 *@p: PyObject representing the Python bytes object
 *
 *Return: Nothing
 */
void print_python_bytes(PyObject *p)
{
	int size, bytes;

	printf("[.] bytes object info\n");

	/*Check if the object is a valid PyBytesObject */
	if (!PyBytes_Check(p))
	{
		printf(" [ERROR] Invalid Bytes Object\n");
		return;
	}

	/*Get the size and string representation of the bytes object */
	size = PyBytes_Size(p);
	bytes = size + 1;

	/*Print the size and string representation */
	printf("  size: %d\n", size);
	printf("  trying string: %s\n", ((PyListObject *)p)->ob_sval);

	/*Print the hexadecimal representation of the first bytes */
	printf("  first %d bytes: ", bytes);
	print_hexn(((PyListObject *)p)->ob_sval, bytes);
}
/**
 *print_python_list - Print some basic info about Python lists
 *@p: PyObject representing the Python list
 *
 *Return: Nothing
 */
void print_python_list(PyObject *p)
{
	PyObject *object;
	int ai, size;

	printf("[*] Python list info\n");
	/*Get the size of the Python list */
	size = PyList_GET_SIZE(p);
	printf("[*] Size of the Python List = %d\n", size);

	/*Print the allocated space for the list */
	printf("[*] Allocated = %ld\n", ((PyListObject *)p)->allocated);

	/*Iterate over the list elements */
	for (ai = 0; ai < size; ai++)
	{
		/*Get the object at the current index */
		object = PyList_GET_ITEM(p, ai);
		printf("Element %d: %s\n", ai, Py_TYPE(object)->tp_name);

		/*Check if the object is of type PyBytesObject */
		if (PyBytes_Check(object))
			print_python_bytes(object);
	}
}
