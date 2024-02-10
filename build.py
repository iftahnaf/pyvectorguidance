"""
Adapted from https://github.com/pybind/cmake_example
"""
import os
import platform
import re
import subprocess
import sys
import sysconfig
from distutils.version import LooseVersion
from typing import Any, Dict

import Cython.Build
from numpy import get_include as get_numpy_include
from setuptools.command.build_ext import build_ext
from setuptools.extension import Extension


class CMakeExtension(Extension):
    name: str  # exists, even though IDE doesn't find it

    def __init__(self, name: str, sourcedir: str="") -> None:
        super().__init__(name, sources=[])
        self.sourcedir = os.path.abspath(sourcedir)


class ExtensionBuilder(build_ext):
    def run(self) -> None:
        self.validate_cmake()
        super().run()

    def build_extension(self, ext: Extension) -> None:
        if isinstance(ext, CMakeExtension):
            self.build_cmake_extension(ext)
        else:
            super().build_extension(ext)

    def validate_cmake(self) -> None:
        cmake_extensions = [x for x in self.extensions if isinstance(x, CMakeExtension)]
        if len(cmake_extensions) > 0:
            try:
                out = subprocess.check_output(["cmake", "--version"])
            except OSError:
                raise RuntimeError(
                    "CMake must be installed to build the following extensions: "
                    + ", ".join(e.name for e in cmake_extensions)
                )
            if platform.system() == "Windows":
                cmake_version = LooseVersion(re.search(r"version\s*([\d.]+)", out.decode()).group(1))  # type: ignore
                if cmake_version < "3.1.0":
                    raise RuntimeError("CMake >= 3.1.0 is required on Windows")

    def build_cmake_extension(self, ext: CMakeExtension) -> None:
        extdir = os.path.abspath(os.path.dirname(self.get_ext_fullpath(ext.name)))
        cmake_args = ["-DBUILD_TESTS=ON", "-DBUILD_EXAMPLES=ON", "-DCMAKE_LIBRARY_OUTPUT_DIRECTORY="]

        cfg = "Debug" if self.debug else "Release"
        # cfg = 'Debug'
        build_args = ["--config", cfg]

        if platform.system() == "Windows":
            cmake_args += ["-DCMAKE_LIBRARY_OUTPUT_DIRECTORY_{}={}".format(cfg.upper(), extdir)]
            if sys.maxsize > 2 ** 32:
                cmake_args += ["-A", "x64"]
            build_args += ["--", "/m"]
        else:
            cmake_args += ["-DCMAKE_BUILD_TYPE=" + cfg]
            build_args += ["--", "-j4"]
        cmake_args += ["-DPYTHON_INCLUDE_DIR={}".format(sysconfig.get_path("include"))]

        env = os.environ.copy()
        env["CXXFLAGS"] = '{} -DVERSION_INFO=\\"{}\\"'.format(env.get("CXXFLAGS", ""), self.distribution.get_version())
        if not os.path.exists(self.build_temp):
            os.makedirs(self.build_temp)
        subprocess.check_call(["cmake", ext.sourcedir] + cmake_args, cwd=self.build_temp, env=env)
        subprocess.check_call(["cmake", "--build", "."] + build_args, cwd=self.build_temp)


def build(setup_kwargs: Dict[str, Any]) -> None:
    cython_modules = Cython.Build.cythonize([
        Extension(
            "project.package.cython_extension",
            sources=["project/package/cython_extension.pyx"],
            include_dirs=[get_numpy_include(), "."],
        )
    ])
    cmake_modules = [CMakeExtension("project.package.pybind11_extension", sourcedir="project/package/pybind11_extension")]
    ext_modules = cython_modules + cmake_modules
    setup_kwargs.update(
        {
            "ext_modules": ext_modules,
            "cmdclass": dict(build_ext=ExtensionBuilder),
            "zip_safe": False,
        }
    )