cmake_minimum_required(VERSION 3.12)
project(pyvectorguidance)

set(PYTHON_EXECUTABLE "/usr/bin/python3")
find_package(pybind11 REQUIRED)
find_package(Eigen3 REQUIRED)

add_library(pyvectorguidance MODULE wrapper.cpp)

# Add include directories for Python and Eigen
target_include_directories(pyvectorguidance PRIVATE ${pybind11_INCLUDE_DIRS})
target_include_directories(pyvectorguidance PRIVATE ${PYTHON_INCLUDE_DIRS})
target_include_directories(pyvectorguidance PRIVATE ${EIGEN3_INCLUDE_DIR})

# Link against pybind11 module and your C++ library
target_link_libraries(pyvectorguidance PRIVATE pybind11::module vectorguidance)

# Remove the 'lib' prefix from the output library name
set_target_properties(pyvectorguidance PROPERTIES PREFIX "")