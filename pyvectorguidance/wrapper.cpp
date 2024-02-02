#include "../third_party/pybind11/include/pybind11/pybind11.h"

#include "vectorguidance/soft_landing.hpp"
#include "vectorguidance/bounded_interception.hpp"

namespace py = pybind11;

PYBIND11_MODULE(libpyvectorguidance, m){
    m.def("soft_landing_tgo_lq", &SoftLanding::soft_landing_tgo_lq, "Soft landing lq tgo");
    m.def("soft_landing_tgo_bounded", &SoftLanding::soft_landing_tgo_bounded, "Soft landing bounded tgo");
    m.def("soft_landing_controller_lq", &SoftLanding::soft_landing_controller_lq, "Soft landing lq controller");
    m.def("soft_landing_controller_bounded", &SoftLanding::soft_landing_controller_bounded, "Soft landing bounded controller");

    py::class_<BoundedInterception>(m, "BoundedInterception")
        .def(py::init<>())
        .def("bounded_interception_controller", &BoundedInterception::bounded_interception_controller)
        .def("bounded_interception_tgo", &BoundedInterception::bounded_interception_tgo);
}