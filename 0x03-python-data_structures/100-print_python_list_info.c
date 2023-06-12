#include <Python.h>

/**
 * print_python_list_info - a function to print some basic info about Python lists.
 *
 * @p: is a Python object list.
 *
 * Return: nothing.
 */
void print_python_list_info(PyObject *p)
{
	PyObject *item;
	const char *type;
	Py_ssize_t size, i, allocated;

	size = Py_SIZE(p);
	allocated = ((PyListObject *)p)->allocated;

	printf("[*] Size of the Python List = %ld\n", size);
	printf("[*] Allocated = %ld\n", allocated);

	for (i = 0; i < size; i++)
	{
		item = PyList_GetItem(p, i);
		type = Py_TYPE(item)->tp_name;

		printf("Element %ld: %s\n", i, type);
	}
}
