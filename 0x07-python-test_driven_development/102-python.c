#include <Python.h>

void print_python_string(PyObject *p) {
    long int length;

    fflush(stdout);

    printf("[.] string object info\n");
    if (!PyUnicode_Check(p)) {
        printf("  [ERROR] Invalid String Object\n");
        return;
    }

    length = PyUnicode_GET_LENGTH(p);

    if (PyUnicode_IS_COMPACT_ASCII(p))
        printf("  type: compact ascii\n");
    else
        printf("  type: compact unicode object\n");

    Py_ssize_t size;
    const wchar_t *wstr = PyUnicode_AsWideCharString(p, &size);
    printf("  length: %ld\n", size);
    printf("  value: %ls\n", wstr);
    PyMem_Free((void *)wstr);
}
