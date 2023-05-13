#include <stdio.h>
#include <stdlib.h>
#include <Python.h>

/**
 *print_python_list_info - Print some basic info about Python lists
 *@p: PyObject representing the Python list
 *
 *Return: Nothing
 */
void print_python_list_info(PyObject *p)
{
	/*PyObject pointer to store individual list elements */
	PyObject *object;
	/*ai for iteration, size to store the size of the list */
	int ai, size;
	/*Get the size of the Python list */
	size = Py_SIZE(p);

	printf("[*] Size of the Python List = %d\n", size);

	printf("[*] Allocated = %ld\n", ((PyListObject *)p)->allocated);

	/*Iterate through the elements of the list */
	for (ai = 0; ai < size; ai++)
	{
		/*Get the individual list element */
		object = PyList_GetItem(p, ai);
		/*Print the element's type */
		printf("Element %d: %s\n", ai, Py_TYPE(object)->tp_name);
	}
}
