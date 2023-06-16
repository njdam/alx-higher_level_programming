#include <stdio.h>
#include <Python.h>

/**
 * print_python_bytes - is a function to print python bytes objects;
 * @p: is a python object which contain required basic info for object bytes;
 *
 * Return: type is void.
 */
void print_python_bytes(PyObject *p)
{
	Py_ssize_t max, size, i = 0; /* Py_ssize_t or long int */
	char *str;
	
	printf("[.] bytes object info\n");
	if (!PyBytes_Check(p)) /* to check if it is Bytes object */
	{
		printf("  [ERROR] Invalid Bytes Object\n");
		return;
	}
	
	/* `((PyVarObject *)(p))->ob_size` to replace `PyBytes_Size(p)` */
	size = ((PyVarObject *)(p))->ob_size;
	/* `((PyBytesObject *)p)->ob_sval` to replace `PyBytes_AsString(p)` */
	str = ((PyBytesObject *)p)->ob_sval;

	printf("  size: %ld\n", size);
	printf("  trying string: %s\n", str);
	
	if (size >= 10)
		max = 10;
	else
		max = size + 1;

	printf("  first %ld bytes:", max);

	while (i < max)
	{
		if (str[i] >= 0)
			printf(" %02x", str[i]);
		else
			printf(" %02x", 256 + str[i]);
		i++;
	}
	
	printf("\n");
}

/**
 * print_python_list - is a function to print some basic info about python list;
 * @p: is a python object which contain required basic info;
 *
 * Return: type is void.
 */
void print_python_list(PyObject *p)
{
	PyListObject *list = (PyListObject *)p;
	Py_ssize_t i = 0, allocates, size = ((PyVarObject *)(p))->ob_size;
	PyObject *object;

	printf("[*] Python list info\n");
	printf("[*] Size of the Python List = %ld\n", size);

	allocates = list->allocated;
	printf("[*] Allocated = %ld\n", allocates);

	while (i < size)
	{
		/* `((PyListObject *)p)->ob_item[i]` to replace `PyList_GetItem(p, i);` */
		object = list->ob_item[i];
		/* (object)->ob_type)->tp_name to replace Py_TYPE(object)->tp_name */
		printf("Element %ld: %s\n", i, ((object)->ob_type)->tp_name);

		if (PyBytes_Check(object))
			print_python_bytes(object);
		i++;
	}
}
