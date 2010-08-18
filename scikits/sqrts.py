# -*- coding: utf-8 -*-

import numpy as np

def nmv(z):
    """Nevière-Maystre-Vincent square-root.
    Cf. http://dx.doi.org/10.1088/0150-536X/8/4/002"""
    return np.sqrt(1j)*np.sqrt(-1j*z)

def nmvo(z):
    """Nevière-Maystre-Vincent square-root, opposite branch cut"""
    return -np.sqrt(-1j)*np.sqrt(1j*z)

def posimag(z):
    """Positive imaginary part"""
    return 1j*np.conj(np.sqrt(-np.conj(z)))

class Nearest:
    """nearest square root"""
    def __init__(self, value):
        self.previous = np.complex(value)
    def sqrt(self,z): 
        s = np.sqrt(np.complex(z))
        d1 = np.abs(self.previous - s)
        d2 = np.abs(self.previous + s)
        self.previous = ((d1 <= d2)*2-1)*s
        return self.previous
