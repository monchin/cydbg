cdef extern from "cpp.h":
    cdef void write_in_wrong_loc(float* ptr, int size)
    cdef cppclass CppClass:
        CppClass() except +
        void double_free()
        void use_after_free()