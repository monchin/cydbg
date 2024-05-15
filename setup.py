import platform
import shutil
from pathlib import Path

from Cython.Build import cythonize
from setuptools import Extension, setup

PRJ_PATH = Path(__file__).absolute().parent / "src" / "cydbg"
PROJ_NAME = "cydbg_cy"

DEBUG_DICT = {"y": True, "n": False, "": False}

srcs = [
    str(PRJ_PATH / "cython" / "cy.pyx"),
    str(PRJ_PATH / "cpp" / "src" / "cpp.cpp"),
]


include_dirs = [str(PRJ_PATH / "cpp" / "include")]
library_dirs = []
libraries = []

PFSYS = platform.system()
if PFSYS == "Windows":
    extra_compile_args = ["/std:c++17"]
    extra_link_args = []
elif PFSYS == "Linux":
    extra_compile_args = ["-std=c++17",]
    extra_link_args = []
else:
    raise NotImplementedError("Only support Windows and Linux")


if __name__ == "__main__":
    define_macros = []

    # 是否debug模式
    if_debug = input("compile by DEBUG? y/(n):").lower()
    while if_debug not in DEBUG_DICT.keys():
        if_debug = input("wrong input, please type again: y/(n):").lower()
    need_debug = DEBUG_DICT[if_debug]
    if need_debug is True:
        if PFSYS == "Windows":
            extra_compile_args += ["/Zi", "/Od"]
            extra_link_args += ["/DEBUG"]
        else:
            extra_compile_args += ["-g", "-O0"]
        
    extension = Extension(
        PROJ_NAME,
        sources=srcs,
        include_dirs=include_dirs,
        library_dirs=library_dirs,
        libraries=libraries,
        language="C++",
        define_macros=define_macros,
        undef_macros=[],
        extra_compile_args=extra_compile_args,
        extra_link_args=extra_link_args,
    )
    extensions = [extension]
    setup(ext_modules=cythonize(extensions, language_level=3))

    if PFSYS == "Windows":
        ext = ".pyd"
    else:
        ext = ".so"
    save_dir = PRJ_PATH / "cython"
    for each_lib_dir in Path("build").glob("lib.*"):
        if each_lib_dir.is_dir():
            for each in each_lib_dir.glob(f"*{ext}"):
                shutil.move(each, save_dir / f"{each.name}")
            if need_debug:
                for each in each_lib_dir.glob(f"*.pdb"):
                    shutil.move(each, save_dir / f"{each.name}")