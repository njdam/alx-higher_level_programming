#include <stdio.h>
#include <Python.h>

void print_python_bytes(PyObject *p);

/**
 * print_python_list - is a function to print some basic info about python list;
 * @p: is a python object which contain required basic info;
 *
 * Return: type is void.
 */
void print_python_list(PyObject *p)
{
	PyListObject *list;
	Py_ssize_t i = 0, allocates, size = PyList_Size(p);
	PyObject *object;

	list = (PyListObject *)p;
	printf("[*] Python list info\n");
	printf("[*] Size of the Python List = %ld\n", size);

	allocates = list->allocated;
	printf("[*] Allocated = %ld\n", allocates);

	while (i < size)
	{
		object = list->ob_item[i];
		printf("Element %ld: %s\n", i, (object->ob_type)->tp_name);

		if (PyBytes_Check(object))
			print_python_bytes(object);
		i++;
	}
}

/**
 * print_python_bytes - is a function to print python bytes objects;
 * @p: is a python object which contain required basic info for object bytes;
 *
 * Return: type is void.
 */
void print_python_bytes(PyObject *p)
{
	Py_ssize_t size, i = 0, max;
	char *str;
	
	printf("[.] bytes object info\n");
	if (!PyBytes_Check(p))
	{
		printf("  [ERROR] Invalid Bytes Object\n");

		return;
	}
	
	str = ((PyBytesObject *)p)-> ob_sval;
	size = ((PyVarObject *)p)-> ob_size;

	printf(" size: %ld\n", size);
	printf(" trying string: %s\n", str);
	
	if (size < 10)
		max = size + 1;
	else
		max = 10;

	printf(" first %ld bytes:", max);

	while (i < max)
	{
		if (str[i] < 0)
			printf(" %02x", 256 + str[i]);
		else
			printf(" %02x", str[i]);
		i++;
	}
	
	printf("\n");
}
