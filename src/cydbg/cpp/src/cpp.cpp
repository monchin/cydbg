#include "cpp.h"

void write_in_wrong_loc(float* ptr, int size) {
    ptr[size + 5] = 5.0f;
}

void CppClass::double_free() {
    double* ptr = new double[10];
    delete[] ptr;
    delete[] ptr; // double free
}

void CppClass::use_after_free() {
    double* ptr = new double[10];
    delete[] ptr;
    // use after free
    ptr[0] = 5.0;
}
