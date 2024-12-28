#include <Python.h>
#include <time.h>
#include "functions.h"

//mozliwe sygnatury funkcji stanowiącej "interfejs" pomiędzy pythonem i C
//static PyObject *mod_met(PyObject *self){
//static PyObject *mod_met(PyObject *self, PyObject *args, PyObject *kw){
static PyObject *mod_met(PyObject *self, PyObject *args){
	int a = 0;
    int b = 0;
    int c = 0;
	PyObject *d=NULL;
	if(!PyArg_ParseTuple(args, "ii|iO", &a, &b, &c, &d)){ //jezeli do stringa wstawi sie | to po sa parametry opcjonalne; O od Object
		return NULL;	//zwracane w przypadku bledu; interpreter zglasza wyjatek wywolania funkcji
	}
	int s=a+b+c;
	if(d){
		int r=PyList_Size(d);
		for(int i=0; i<r; i++){
            PyObject *item = PyList_GetItem(d, i);
            if (PyLong_Check(item)) {
                s += PyLong_AsLong(item);
            }
		}
	}
	//Py_RETURN_NONE; //jesli nic nie zwraca
	return Py_BuildValue("i", s);
}

static PyObject *mod_sortuj(PyObject *self, PyObject *args){
	PyObject *t=NULL;
	if(!PyArg_ParseTuple(args, "O", &t)){ //jezeli do stringa wstawi sie | to po sa parametry opcjonalne; O od Object
		return NULL;	//zwracane w przypadku bledu; interpreter zglasza wyjatek wywolania funkcji
	}
    int r=PyList_Size(t);
    int *arr = malloc(r * sizeof(int));
    for(int i=0; i<r; i++){
        PyObject *item = PyList_GetItem(t, i);
        if (PyLong_Check(item)) {
            arr[i] = PyLong_AsLong(item);
        }
    }

    sortuj(arr, r);

    PyObject* pyList = PyList_New(r);
    for (int i = 0; i < r; i++) {
        PyList_SetItem(pyList, i, PyLong_FromLong(arr[i]));
    }
    free(arr);

	//Py_RETURN_NONE; //jesli nic nie zwraca
	return Py_BuildValue("O", pyList);
}

static PyObject *mod_mnozenie(PyObject *self, PyObject *args){
	PyObject *t1=NULL;
    PyObject *t2=NULL;
	if(!PyArg_ParseTuple(args, "OO", &t1, &t2)){ //jezeli do stringa wstawi sie | to po sa parametry opcjonalne; O od Object
		return NULL;	//zwracane w przypadku bledu; interpreter zglasza wyjatek wywolania funkcji
	}
    int wierszy1=PyList_Size(t1);
    int kolumn1 = PyList_Size(PyList_GetItem(t1, 0));
    int wierszy2=PyList_Size(t2);
    int kolumn2 = PyList_Size(PyList_GetItem(t2, 0));

    int **a = malloc(wierszy1 * sizeof(int*));
    for (int i = 0; i < wierszy1; i++) {
        a[i] = malloc(kolumn1 * sizeof(int));

        PyObject *item = PyList_GetItem(t1, i);

        for (int j = 0; j < kolumn1; j++) {
            a[i][j] = PyLong_AsLong(PyList_GetItem(item, j));
        }
    }

    int **b = malloc(wierszy2 * sizeof(int*));
    for (int i = 0; i < wierszy2; i++) {
        b[i] = malloc(kolumn2 * sizeof(int));

        PyObject *item = PyList_GetItem(t2, i);

        for (int j = 0; j < kolumn1; j++) {
            b[i][j] = PyLong_AsLong(PyList_GetItem(item, j));
        }
    }

    int **c = malloc(wierszy1 * sizeof(int*));
    for (int i = 0; i < wierszy1; i++) {
        c[i] = calloc(kolumn2, sizeof(int));
    }

    mnoz(a, b, c, wierszy1, kolumn1, kolumn2);

    PyObject* pyList = PyList_New(wierszy1);
    for (int i = 0; i < wierszy1; i++) {

        PyObject* pyListW = PyList_New(kolumn2);
        for (int j = 0; j < kolumn2; j++) {
            PyList_SetItem(pyListW, j, PyLong_FromLong(c[i][j]));
        }
        PyList_SetItem(pyList, i, pyListW);
    }


    for (int i = 0; i < wierszy1; i++) {
        free(a[i]);
    }
    free(a);

    for (int i = 0; i < wierszy2; i++) {
        free(b[i]);
    }
    free(b);

    for (int i = 0; i < wierszy1; i++) {
        free(c[i]);
    }
    free(c);


	//Py_RETURN_NONE; //jesli nic nie zwraca
	return Py_BuildValue("O", pyList);
}

//tablica metod
static PyMethodDef mod_metody[]={
	{"met", (PyCFunction)mod_met, METH_VARARGS, "Funkcja ..."},
    {"sortuj", (PyCFunction)mod_sortuj, METH_VARARGS, "Funkcja ..."}, 
    {"mnozenie", (PyCFunction)mod_mnozenie, METH_VARARGS, "Funkcja ..."}, 
	//nazwa funkcja stosowana w Pythonie, adres funkcji , j.w. lub METH_KEYWORDS lub METH_NOARGS, lancuch dokumentacyjny
	{NULL, NULL, 0, NULL}	//wartownik
};


static struct PyModuleDef modmodule={
        PyModuleDef_HEAD_INIT,
        "mod",
        NULL,
        -1,
        mod_metody
};

//funkcja inicjalizujaca
PyMODINIT_FUNC PyInit_mod(void){
        return PyModule_Create(&modmodule);
}
