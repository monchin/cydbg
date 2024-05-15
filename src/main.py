import numpy as np
from cydbg.cython import cydbg_cy

if __name__ == '__main__':
    test_arr = np.zeros((5, ), dtype=np.float32)
    print("a")
    cydbg_cy.py_write_in_wrong_loc(test_arr)
    print("b")
    pyclass = cydbg_cy.PyClass()
    # pyclass.double_free()
    print("c")
    pyclass.use_after_free()
    print("d")
