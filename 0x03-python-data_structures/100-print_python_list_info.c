#include <Python.h>

/**
 * print_python_list_info - prints the information of a python list
 * @p: pointer to the python object
 *
 */
void print_python_list_info(PyObject *p)
{
	Py_ssize_t size, i;
	PyObject *obj;

	size = PyList_Size(p);
	printf("[*] Size of the Python List = %ld\n", size);
	printf("[*] Allocated = %ld\n", ((PyListObject *)p)->allocated);
	for (ai = 0; ai < size; ai++)
	{
		obj = PyList_GetItem(p, ai);
		printf("Element %ld: %s\n", ai, Py_TYPE(obj)->tp_name);
	}
}
