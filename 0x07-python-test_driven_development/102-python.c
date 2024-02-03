#include <stdio.h>
#include <Python.h>

/**
 * print_python_string - prints info about python strings
 * @p: python object
 */
void print_python_string(PyObject *p)
{
	printf("[.] string object info\n");
	if (p == NULL || !PyUnicode_Check(p))
	{
		printf("  [ERROR] Invalid String Object\n");
		return;
	}
	printf("  type: %s\n", p->ob_type->tp_name);
	printf("  length: %ld\n", PyUnicode_GET_LENGTH(p));
	printf("  value: %ls\n", PyUnicode_AS_UNICODE(p));
}