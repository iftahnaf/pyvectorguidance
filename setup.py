from setuptools import setup, Extension
from setuptools.command.build_ext import build_ext
from pybind11.setup_helpers import Pybind11Extension
import sys
import setuptools

# Read version from pyproject.toml
version = "0.0.1"

# Define the extension module
extension_mod = Pybind11Extension("pyvectorguidance",
                           sources=["pyvectorguidance/wrapper.cpp"],
                           include_dirs=["/usr/include/eigen3"],  # Adjust the path to Eigen3 as necessary
                           extra_compile_args=["-std=c++11"])    # Add compiler flag for C++11 support

# Subclass build_ext
class BuildExt(build_ext):
    def build_extensions(self):
        # Adjust compiler flags if needed
        for ext in self.extensions:
            ext.extra_compile_args.append("-Wno-deprecated-declarations")  # Example: suppress deprecated warnings
        super().build_extensions()

# Setup
setup(
    name="pyvectorguidance",
    version=version,  # Set the version from pyproject.toml
    description="Vector guidance for Python",
    author="Iftach Naftaly",
    author_email="iftahnaf@proton.me",
    license="Apache-2.0",
    keywords=["guidance", "control", "autonomous-systems"],
    url="https://github.com/iftahnaf/pyvectorguidance",
    packages=setuptools.find_packages(),
    ext_modules=[extension_mod],
    cmdclass={"build_ext": BuildExt},
)
