#include "Python.h"

/**
 * print_python_string - Prints information about Python strings.
 * @p: A PyObject string object.
 */
void print_python_string(PyObject *p)
{
    Py_ssize_t len;
    const wchar_t *value;

    printf("[.] string object info\n");

    if (strcmp(p->ob_type->tp_name, "str") != 0)
    {
        printf("  [ERROR] Invalid String Object\n");
        return;
    }

    len = ((PyASCIIObject *)p)->length;
    value = PyUnicode_AsWideCharString(p, &len);

    if (PyUnicode_IS_COMPACT_ASCII(p))
        printf("  type: compact ascii\n");
    else
        printf("  type: compact unicode object\n");

    printf("  length: %zd\n", len);
    printf("  value: %ls\n", value);

    PyMem_Free((void *)value);
}
