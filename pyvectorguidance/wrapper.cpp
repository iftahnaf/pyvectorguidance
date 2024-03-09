#include "../third_party/pybind11/include/pybind11/pybind11.h"
#include "../third_party/pybind11/include/pybind11/numpy.h"
#include "../third_party/pybind11/include/pybind11/eigen.h"
#include "vectorguidance/soft_landing.hpp"
#include "vectorguidance/bounded_interception.hpp"
#include <Eigen/Dense>
#include <Eigen/Geometry>
#include <unsupported/Eigen/Polynomials>

namespace py = pybind11;

PYBIND11_MODULE(pyvectorguidance, m){
    py::class_<SoftLanding>(m, "SoftLanding")
        .def(py::init<>())
        .def("soft_landing_controller_bounded", [](SoftLanding &sl, py::array_t<double> r, py::array_t<double> v, double tgo) {
            // Access the underlying data of r and v
            double *r_ptr = static_cast<double *>(r.request().ptr);
            double *v_ptr = static_cast<double *>(v.request().ptr);

            // Create an empty NumPy array for u
            py::array_t<double> u_array = py::array_t<double>({3}); // Assuming u is a 3-element array
            double *u_ptr = static_cast<double *>(u_array.request().ptr);

            // Call your original function with the pointers
            sl.soft_landing_controller_bounded(r_ptr, v_ptr, u_ptr, tgo);

            // Return the populated u_array to Python
            return u_array;
        }, py::arg("r"), py::arg("v"), py::arg("tgo"))
        .def("soft_landing_controller_lq", [](SoftLanding &sl, py::array_t<double> r, py::array_t<double> v, double tgo) {
            // Access the underlying data of r and v
            double *r_ptr = static_cast<double *>(r.request().ptr);
            double *v_ptr = static_cast<double *>(v.request().ptr);

            // Create an empty NumPy array for u
            py::array_t<double> u_array = py::array_t<double>({3}); // Assuming u is a 3-element array
            double *u_ptr = static_cast<double *>(u_array.request().ptr);

            // Call your original function with the pointers
            sl.soft_landing_controller_lq(r_ptr, v_ptr, u_ptr, tgo);

            // Return the populated u_array to Python
            return u_array;
        }, py::arg("r"), py::arg("v"), py::arg("tgo"))
        .def("soft_landing_tgo_bounded", [](SoftLanding &sl, py::array_t<double> r, py::array_t<double> v, double min_tgo) {
            // Access the underlying data of r and v
            double *r_ptr = static_cast<double *>(r.request().ptr);
            double *v_ptr = static_cast<double *>(v.request().ptr);

            // Call your original function with the pointers
            return sl.soft_landing_tgo_bounded(r_ptr, v_ptr, min_tgo);
        }, py::arg("r"), py::arg("v"), py::arg("min_tgo"))
        .def_property("um", [](SoftLanding& obj){return obj.um;}, [](SoftLanding& obj, double um){obj.um = um;})
        .def("soft_landing_tgo_lq", [](SoftLanding &sl, py::array_t<double> r, py::array_t<double> v, double min_tgo) {
            // Access the underlying data of r and v
            double *r_ptr = static_cast<double *>(r.request().ptr);
            double *v_ptr = static_cast<double *>(v.request().ptr);

            // Call your original function with the pointers
            return sl.soft_landing_tgo_lq(r_ptr, v_ptr, min_tgo);
        }, py::arg("r"), py::arg("v"), py::arg("min_tgo"));

    py::class_<BoundedInterception>(m, "BoundedInterception")
        .def(py::init<>())
        .def("bounded_interception_tgo", [](BoundedInterception &bi, py::array_t<double> r, py::array_t<double> v, double min_tgo) {
            // Access the underlying data of r and v
            double *r_ptr = static_cast<double *>(r.request().ptr);
            double *v_ptr = static_cast<double *>(v.request().ptr);
            // Call your original function with the pointers
            return bi.bounded_interception_tgo(r_ptr, v_ptr, min_tgo);
        }, py::arg("r"), py::arg("v"), py::arg("min_tgo"))
        .def_property("rho_u", [](BoundedInterception& obj){return obj.rho_u;}, [](BoundedInterception& obj, double rho_u){obj.rho_u = rho_u;})
        .def_property("rho_w", [](BoundedInterception& obj){return obj.rho_w;}, [](BoundedInterception& obj, double rho_w){obj.rho_w = rho_w;})
        .def("bounded_interception_controller", [](BoundedInterception &bi, py::array_t<double> r, py::array_t<double> v, double tgo) {
            // Access the underlying data of r and v
            double *r_ptr = static_cast<double *>(r.request().ptr);
            double *v_ptr = static_cast<double *>(v.request().ptr);

            // Create an empty NumPy array for u
            py::array_t<double> u_array = py::array_t<double>({3}); // Assuming u is a 3-element array
            double *u_ptr = static_cast<double *>(u_array.request().ptr);

            // Call your original function with the pointers
            bi.bounded_interception_controller(r_ptr, v_ptr, u_ptr, tgo);

            // Return the populated u_array to Python
            return u_array;
        }, py::arg("r"), py::arg("v"), py::arg("tgo"));
}