import multiprocessing as mp

import numpy as np
from cydbg.cython import cydbg_cy


def bad_kernel():
    pyclass = cydbg_cy.PyClass()
    # pyclass.double_free()
    pyclass.use_after_free()


if __name__ == "__main__":
    test_arr = np.zeros((5,), dtype=np.float32)
    p = mp.Process(target=bad_kernel, args=())
    p.start()
    cydbg_cy.py_write_in_wrong_loc(test_arr)
    p.join()
