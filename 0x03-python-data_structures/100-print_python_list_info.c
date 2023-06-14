#include <Python.h>

/**
 * print_python_list_info - a function to print basic info about Python lists.
 *
 * @p: is a Python object list.
 *
 * Return: type is void nothing to be returned.
 */
void print_python_list_info(PyObject *p)
{
	PyObject *item;
	const char *type;
	Py_ssize_t size, i, allocates;

	size = Py_SIZE(p);
	allocates = ((PyListObject *)p)->allocated;

	printf("[*] Size of the Python List = %ld\n", size);
	printf("[*] Allocated = %ld\n", allocates);

	for (i = 0; i < size; i++)
	{
		item = PyList_GetItem(p, i);
		type = Py_TYPE(item)->tp_name;

		printf("Element %ld: %s\n", i, type);
	}
}
