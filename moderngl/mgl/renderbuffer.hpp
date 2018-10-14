#pragma once
#include "mgl.hpp"
#include "context.hpp"

struct MGLDataType;

struct MGLRenderbuffer {
    PyObject_HEAD
    PyObject * wrapper;
    MGLContext * context;
    MGLDataType * data_type;
    int renderbuffer_obj;
    int width;
    int height;
    int depth;
    int components;
    int levels;
    int samples;
};