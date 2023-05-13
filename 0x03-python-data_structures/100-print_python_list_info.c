#include <stdio.h>
#include <stdlib.h>
#include <Python.h>

/**
 *print_python_list_info - Print some basic info about Python lists
 *@p: PyObject
 *
 *Return: Nothing
 */
void print_python_list_info(PyObject *p)
{
	PyObject *object;
	int ai, size;

	size = Py_SIZE(p);

	printf("[*] Size of the Python List = %d\n", size);

	printf("[*] Allocated = %ld\n", ((PyListObject *)p)->allocated);

	for (ai = 0; ai < size; ai++)
	{
		object = PyList_GetItem(p, ai);
		printf("Element %d: %s\n", ai, Py_TYPE(object)->tp_name);
	}
}
