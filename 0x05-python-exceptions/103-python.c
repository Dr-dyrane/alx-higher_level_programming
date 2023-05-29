#include <Python.h>

void print_python_list(PyObject *p);
void print_python_bytes(PyObject *p);
void print_python_float(PyObject *p);

/**
 * print_python_list - Prints basic info about Python lists.
 * @p: A PyObject list object.
 */
void print_python_list(PyObject *p)
{
	Py_ssize_t a_size, alloc, ai = 0;
	const char *type;
	PyListObject *list = (PyListObject *)p;
	PyVarObject *var = (PyVarObject *)p;

	a_size = var->ob_size;
	alloc = list->allocated;

	fflush(stdout);

	printf("[*] Python list info\n");
	if (strcmp(p->ob_type->tp_name, "list") != 0)
	{
		printf(" [ERROR] Invalid List Object\n");
		return;
	}

	printf("[*] Size of the Python List = %ld\n", a_size);
	printf("[*] Allocated = %ld\n", alloc);

	while (ai < a_size)
	{
		type = list->ob_item[ai]->ob_type->tp_name;
		printf("Element %ld: %s\n", ai, type);
		if (strcmp(type, "bytes") == 0)
			print_python_bytes(list->ob_item[ai]);
		else if (strcmp(type, "float") == 0)
			print_python_float(list->ob_item[ai]);
		ai++;
	}
}

/**
 * print_python_bytes - Prints basic info about Python byte objects.
 * @p: A PyObject byte object.
 */
void print_python_bytes(PyObject *p)
{
	Py_ssize_t a_size, ai = 0;
	PyBytesObject *bytes = (PyBytesObject *)p;

	fflush(stdout);

	printf("[.] bytes object info\n");
	if (strcmp(p->ob_type->tp_name, "bytes") != 0)
	{
		printf(" [ERROR] Invalid Bytes Object\n");
		return;
	}

	printf("  a_size: %ld\n", ((PyVarObject *)p)->ob_size);
	printf("  trying string: %s\n", bytes->ob_sval);

	if (((PyVarObject *)p)->ob_size >= 10)
		a_size = 10;
	else
		a_size = ((PyVarObject *)p)->ob_size + 1;

	printf("  first %ld bytes: ", a_size);
	while (ai < a_size)
	{
		printf("%02hhx", bytes->ob_sval[ai]);
		if (ai == (a_size - 1))
			printf("\n");
		else
			printf(" ");
		ai++;
	}
}

/**
 * print_python_float - Prints basic info about Python float objects.
 * @p: A PyObject float object.
 */
void print_python_float(PyObject *p)
{
	char *b_buffer = NULL;

	PyFloatObject *float_obj = (PyFloatObject *)p;

	fflush(stdout);

	printf("[.] float object info\n");
	if (strcmp(p->ob_type->tp_name, "float") != 0)
	{
		printf(" [ERROR] Invalid Float Object\n");
		return;
	}

	b_buffer = PyOS_double_to_string(float_obj->ob_fval, 'r', 0,
		Py_DTSF_ADD_DOT_0, NULL);
	printf("  value: %s\n", b_buffer);
	PyMem_Free(b_buffer);
}