#include <Python.h>

void print_python_bytes(PyObject *p);
void print_python_float(PyObject *p);

/**
 * print_python_list - is a function to print basic info about Python list;
 * @p: is a Python Object list;
 *
 * Return: nothing.
 */
void print_python_list(PyObject *p)
{
	const char *type_name;
	Py_ssize_t i = 0, size, allocates;
	PyListObject *list = (PyListObject *)p;
	PyVarObject *var = (PyVarObject *)p;

	size = var->ob_size;
	allocates = list->allocated;
	fflush(stdout);

	printf("[*] Python list info\n");
	if (strcmp(p->ob_type->tp_name, "list") != 0)
	{
		printf("  [ERROR] Invalid List Object\n");
		return;
	}
	printf("[*] Size of the Python List = %ld\n", size);
	printf("[*] Allocated = %ld\n", allocates);

	while (i < size)
	{
		type_name = list->ob_item[i]->ob_type->tp_name;
		printf("Element %ld: %s\n", i, type_name);

		if (strcmp(type_name, "bytes") == 0)
			print_python_bytes(list->ob_item[i]);

		else if (strcmp(type_name, "float") == 0)
			print_python_float(list->ob_item[i]);
		i++;
	}
}

/**
 * print_python_bytes - is a function to Print basic info about Python byte obj;
 * @p: is a Python byte object;
 *
 * Return: nothing.
 */
void print_python_bytes(PyObject *p)
{
	PyBytesObject *bytes = (PyBytesObject *)p;
	Py_ssize_t limit, i = 0, size = ((PyVarObject *)p)->ob_size;

	fflush(stdout);
	printf("[.] bytes object info\n");
	if (strcmp(p->ob_type->tp_name, "bytes") != 0)
	{
		printf("  [ERROR] Invalid Bytes Object\n");
		return;
	}
	printf("  size: %ld\n", size);
	printf("  trying string: %s\n", bytes->ob_sval);

	if (size >= 10)
		limit = 10;
	else
		limit = size + 1;

	printf("  first %ld bytes: ", limit);
	while (i < limit)
	{
		printf("%02hhx", bytes->ob_sval[i]);
		if (i == (limit - 1))
			printf("\n");
		else
			printf(" ");
		i++;
	}
}

/**
 * print_python_float - is a function to print basic info about Python float objs;
 * @p: is a Python float object;
 *
 * Return: nothing.
 */
void print_python_float(PyObject *p)
{
	PyFloatObject *floats = (PyFloatObject *)p;
	char *buf = NULL;

	fflush(stdout);
	printf("[.] float object info\n");
	if (strcmp(p->ob_type->tp_name, "float") != 0)
	{
		printf("  [ERROR] Invalid Float Object\n");
		return;
	}

	buf = PyOS_double_to_string(floats->ob_fval,
			'r', 0, Py_DTSF_ADD_DOT_0, NULL);
	printf("  value: %s\n", buf);

	PyMem_Free(buf);
}
