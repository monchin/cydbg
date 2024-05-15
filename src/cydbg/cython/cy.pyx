# distutils: language = c++
from cy cimport write_in_wrong_loc, CppClass

def py_write_in_wrong_loc(float[:] arr):
    write_in_wrong_loc(&arr[0], arr.shape[0])

cdef class PyClass:
    cdef CppClass _cppclass
    def __cinit__(self):
        self._cppclass = CppClass()
    
    def double_free(self):
        self._cppclass.double_free()
    
    def use_after_free(self):
        self._cppclass.use_after_free()
