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
	PyListObject *list = (PyListObject *)p;
	int ai, size, set;

	size = Py_SIZE(p);
	set = list->allocated;
	printf("[*] Size of the Python List = %d\n", size);
	printf("[*] Allocated = %d\n", set);

	for (ai = 0; ai < size; ai++)
	{
		object = PyList_GetItem(p, ai);
		printf("Element %d: %s\n", ai, Py_TYPE(object)->tp_name);
	}
}
