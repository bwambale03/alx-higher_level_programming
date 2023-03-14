#include<Python.h>
#include<object.h>
#include<listobject.h>
/**
 * print_python_list_info-C function that prints some basic
 * info about Python lists.
 * @p: This is an Argument List
 * Return:Always 0
 */
void print_python_list_info(PyObject *p)
{
	long int size = PyList_Size(p);
	int i;
	PyLitObject *obj = (PyListObject *)p;

	printf("[*] Size of the Python List = %li\n", size);
	printf("[*] Allocated = %li\n", obj->allocated);
	for (i = 0; i < size; i++)
		printf("Element %i: %s\n", i, Py_TYPE(obj->obj_item[i]->tp_name);
}
