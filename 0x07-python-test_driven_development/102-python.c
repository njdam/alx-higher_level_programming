#include <Python.h>

/**
 * print_python_string - is a function to print info about Python strings.
 * @p: is a PyObject of Python strings.
 *
 * Return: nothing.
 */
void print_python_string(PyObject *p)
{
	Py_ssize_t lens;

	fflush(stdout);
	printf("[.] string object info\n");

	if (strcmp((p->ob_type)->tp_name, "str") != 0)
	{
		printf("  [ERROR] Invalid String Object\n");
		return;
	}

	lens = ((PyASCIIObject *)(p))->length;

	if (PyUnicode_IS_COMPACT_ASCII(p))
		printf("  type: compact ascii\n");
	else
		printf("  type: compact unicode object\n");

	printf("  length: %ld\n", lens);
	printf("  value: %ls\n", PyUnicode_AsWideCharString(p, &lens));
}
