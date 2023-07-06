#!/usr/bin/python3
"""A file defines a function for multiplying 2 matrices by NumPy module."""

import numpy as mul


def lazy_matrix_mul(m_a, m_b):
    """A function that multiplies 2 metrices by using module NumPy

    Args:
        m_a (matrix): is a list of list must contain int(s)/float(s).
        m_b (matrix): is a list of list must contain int(s)/float(s).
    """

    return (mul.matmul(m_a, m_b))
