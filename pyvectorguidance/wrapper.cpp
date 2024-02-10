#include "../third_party/pybind11/include/pybind11/pybind11.h"
#include "../third_party/pybind11/include/pybind11/numpy.h"
#include "../third_party/pybind11/include/pybind11/eigen.h"
#include "vectorguidance/soft_landing.hpp"
#include "vectorguidance/bounded_interception.hpp"
#include <Eigen/Dense>
#include <Eigen/Geometry>
#include <unsupported/Eigen/Polynomials>


namespace py = pybind11;

PYBIND11_MODULE(libpyvectorguidance, m){
    py::class_<SoftLanding>(m, "SoftLanding")
        .def(py::init<>())
        .def("soft_landing_controller_bounded", &SoftLanding::soft_landing_controller_bounded)
        .def("soft_landing_controller_lq", &SoftLanding::soft_landing_controller_lq)
        .def("soft_landing_tgo_bounded", &SoftLanding::soft_landing_tgo_bounded)
        .def("soft_landing_tgo_lq", &SoftLanding::soft_landing_tgo_lq);

    py::class_<BoundedInterception>(m, "BoundedInterception")
        .def(py::init<>())
        .def("bounded_interception_controller", &BoundedInterception::bounded_interception_controller)
        .def("bounded_interception_tgo", &BoundedInterception::bounded_interception_tgo);
}