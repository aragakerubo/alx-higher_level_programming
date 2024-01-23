#include <Python.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <errno.h>

void print_python_float(PyObject *p);
void print_python_bytes(PyObject *p);
void print_python_list(PyObject *p);

/**
 * print_python_list - prints some basic info about Python lists
 * @p: pointer to a Python object
 */
void print_python_list(PyObject *p)
{
	Py_ssize_t i, size;
	PyListObject *list;

	printf("[*] Python list info\n");
	if (!PyList_Check(p))
	{
		printf("  [ERROR] Invalid List Object\n");
		return;
	}

	list = (PyListObject *)p;
	size = Py_SIZE(p);
	printf("[*] Size of the Python List = %ld\n", size);
	printf("[*] Allocated = %ld\n", list->allocated);

	for (i = 0; i < size; i++)
	{
		printf("Element %ld: ", i);
		printf("%s\n", list->ob_item[i]->ob_type->tp_name);
		if (strcmp(list->ob_item[i]->ob_type->tp_name, "bytes") == 0)
			print_python_bytes(list->ob_item[i]);
		else if (strcmp(list->ob_item[i]->ob_type->tp_name, "float") == 0)
			print_python_float(list->ob_item[i]);
	}
}

/**
 * print_python_bytes - prints some basic info about Python bytes
 * @p: pointer to a Python object
 */
void print_python_bytes(PyObject *p)
{
	Py_ssize_t i, size;
	char *str;

	printf("[.] bytes object info\n");
	if (!PyBytes_Check(p))
	{
		printf("  [ERROR] Invalid Bytes Object\n");
		return;
	}

	str = ((PyBytesObject *)p)->ob_sval;
	size = PyBytes_Size(p);
	printf("  size: %ld\n", size);
	printf("  trying string: %s\n", str);
	if (size < 10)
		printf("  first %ld bytes: ", size + 1);
	else
		printf("  first 10 bytes: ");
	for (i = 0; i <= size && i < 10; i++)
	{
		printf("%02hhx", str[i]);
		if (i < 9 && i < size)
			printf(" ");
	}
	printf("\n");
}

/**
 * print_python_float - prints some basic info about Python float
 * @p: pointer to a Python object
 */
void print_python_float(PyObject *p)
{
	char *str;
	double d;

	printf("[.] float object info\n");
	if (!PyFloat_Check(p))
	{
		printf("  [ERROR] Invalid Float Object\n");
		return;
	}

	d = (((PyFloatObject *)p)->ob_fval);
	str = PyOS_double_to_string(d, 'r', 0, Py_DTSF_ADD_DOT_0, NULL);
	printf("  value: %s\n", str);
}
