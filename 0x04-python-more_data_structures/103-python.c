#include <Python.h>

void print_python_list(PyObject *p);
void print_python_bytes(PyObject *p);

/**
 * print_python_list - Prints basic information about python lists
 * @p: PyObject list object
 *
 * Return: Nothing.
 */
void print_python_list(PyObject *p)
{
	int byte, alloc, index;
	const char *type;
	PyListObject *list = (PyListObject *)p;
	PyVarObject *var = (PyVarObject *)p;

	byte = var->ob_size;
	alloc = list->allocated;

	printf("[*] Python list info\n");
	printf("[*] Size of the Python List = %d\n", byte);
	printf("[*] Allocated = %d\n", alloc);

	for (index = 0; index < byte; index++)
	{
		type = list->ob_item[index]->ob_type->tp_name;
		printf("Element %d: %s\n", index, type);
		if (strcmp(type, "bytes") == 0)
			print_python_bytes(list->ob_item[index]);
	}
}

/**
 * print_python_bytes - prints basic information about python byte objects
 * @p: PyObject byte object
 *
 * Return: Nothing.
 */
void print_python_bytes(PyObject *p)
{
	unsigned char index, byte;
	PyBytesObject *bytes = (PyBytesObject *)p;

	printf("[.] bytes object info\n");
	if (strcmp(p->ob_type->tp_name, "bytes") != 0)
	{
		printf("  [ERROR] Invalid Bytes Object\n");
		return;
	}

	printf("  size: %ld\n", ((PyVarObject *)p)->ob_size);
	printf("  trying string: %s\n", bytes->ob_sval);

	if (((PyVarObject *)p)->ob_size > 10)
		byte = 10;
	else
		byte = ((PyVarObject *)p)->ob_size + 1;

	printf("  first %d bytes: ", byte);
	for (index = 0; index < byte; index++)
	{
		printf("%02hhx", bytes->ob_sval[index]);
		if (index == (byte - 1))
			printf("\n");
		else
			printf(" ");
	}
}
