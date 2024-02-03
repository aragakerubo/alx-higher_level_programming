#include <stdio.h>
#include <Python.h>

/**
 * print_python_string - prints info about python strings
 * @p: python object
 */
void print_python_string(PyObject *p)
{
	long int length;

	fflush(stdout);
	printf("[.] string object info\n");
	if (!PyUnicode_Check(p))
	{
		printf("  [ERROR] Invalid String Object\n");
		return;
	}
	if (PyUnicode_IS_COMPACT_ASCII(p))
		printf("  type: compact ascii\n");
	else
		printf("  type: compact unicode object\n");
	length = PyUnicode_GET_LENGTH(p);
	printf("  length: %ld\n", length);
	printf("  value: %ls\n", PyUnicode_AS_UNICODE(p));
}