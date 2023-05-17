#include "/usr/include/python3.4/Python.h"
#include <stdio.h>

void print_hexn(const char *str, int n)
{
	int jerry = 0;

	do {
		printf("%02x ", (unsigned char) str[jerry]);
		jerry++;
	} while (jerry < n - 1);

	printf("%02x", str[jerry]);
}

void print_python_bytes(PyObject *p)
{
	PyBytesObject *morty_clone = (PyBytesObject*) p;
	int morty_bytes, clone_size = 0;

	printf("[.] bytes object info\n");
	if (PyBytes_Check(morty_clone))
	{
		clone_size = PyBytes_Size(p);
		morty_bytes = clone_size + 1;

		if (morty_bytes >= 10)
			morty_bytes = 10;

		printf("  size: %d\n", clone_size);
		printf("  trying string: %s\n", morty_clone->ob_sval);
		printf("  first %d bytes: ", morty_bytes);
		print_hexn(morty_clone->ob_sval, morty_bytes);
		printf("\n");
	}
	else
		printf("[ERROR] Invalid Bytes Object\n");
}

void print_python_list(PyObject *p)
{
	int morty = 0, morty_list_len = 0;
	PyObject * item;
	PyListObject *morty_clone = (PyListObject*) p;

	printf("[*] Python list info\n");
	morty_list_len = PyList_GET_SIZE(p);
	printf("[*] Size of the Python List = %d\n", morty_list_len);
	printf("[*] Allocated = %d\n", (int) morty_clone->allocated);

	do {
		item = PyList_GET_ITEM(p, morty);
		printf("Element %d: %s\n", morty, item->ob_type->tp_name);

		if (PyBytes_Check(item))
			print_python_bytes(item);

		morty++;
	} while (morty < morty_list_len);
}
