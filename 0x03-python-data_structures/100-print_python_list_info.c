#include <stdio.h>
#include <stdlib.h>

typedef struct object PyObject;

void print_python_list_info(PyObject *p)
{
	void **ptr;
	ssize_t size, allocated;
	ssize_t i;
	PyObject *obj;

	printf("[*] Size of the Python List = %zd\n", *((ssize_t *) p + 1));

	ptr = ((void **) p) + 1;
	size = *((ssize_t *) p + 1);
	allocated = *((ssize_t *) p + 2);
	printf("[*] Allocated = %zd\n", allocated);

	for (i = 0; i < size; i++)
	{
		obj = (PyObject *) ptr[i];
		printf("Element %zd: %s\n", i, ((PyObject *) obj)->ob_type->tp_name);
	}
}
