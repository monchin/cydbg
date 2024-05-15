#include <cstdint>

/**
 * @brief write_in_wrong_loc
 * @param ptr pointer to the beginning of the array
 * @param size size of the array
*/
void write_in_wrong_loc(float* ptr, int size);

class CppClass {
public:
    CppClass() = default;
    ~CppClass() = default;
    void double_free();
    void use_after_free();
};