#include <stdio.h>
#include <Python.h>

/**
 * print_python_list_info - prints python list info
 * @p: PyObject
 * Return: Nothing.
 */
void print_python_list_info(PyObject *p)
{
	long int size, index = 0;
	PyListObject *list;
	PyObject *item;

	size = Py_SIZE(p);
	printf("[*] Size of the Python List = %ld\n", size);
	list = (PyListObject *)p;
	printf("[*] Allocated = %ld\n", list->allocated);
	for (; index < size; index++)
	{
		item = PyList_GetItem(p, index);
		printf("Element %ld: %s\n", index, Py_TYPE(item)->tp_name);
	}
}
