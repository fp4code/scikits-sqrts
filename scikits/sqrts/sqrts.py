# -*- coding: utf-8 -*-

import numpy as np

def nmv(z):
    """Nevière-Maystre-Vincent complex square-root.
    Cf. http://dx.doi.org/10.1088/0150-536X/8/4/002

    >>> sqrts.nmv([-2j-1e-20,-2j,-2j+1e-20])
    array([ 1.+1.j,  1.-1.j, -1.-1.j])
    """
    return np.sqrt(1j)*np.sqrt(-1j*np.asarray(z,np.complex))

def nmvo(z):
    """Nevière-Maystre-Vincent complex square-root, opposite branch cut

    >>> sqrts.nmvo([2j+1e-20,2j,2j-1e-20])
    array([-1.-1.j, -1.-1.j,  1.+1.j])
    """
    return -np.sqrt(-1j)*np.sqrt(1j*np.asarray(z,np.complex))

def posimag(z):
    """Positive imaginary part complex square root

    >>> sqrts.posimag([1+1e-20j,1,1-1e-20j]).real
    array([ 1.,  1., -1.])
    """
    return 1j*np.conj(np.sqrt(-np.conj(z)))

class Nearest:
    """Nearest complex square root
    >>> s = sqrts.Nearest([1,1j,-1,-1j])
    >>> s.sqrt(1).real
    array([ 1.,  1., -1.,  1.])
    >>> s = sqrts.Nearest(1)
    >>> s.sqrt(2j)
    (1+1j)
    >>> s.sqrt(-1)
    1j
    >>> s.sqrt(-2j)
    (-1+1j)
    >>> s.sqrt(1)
    (-1+0j)
    >>> s.sqrt(2j)
    (-1-1j)
    >>> s.sqrt(-1)
    (-0-1j)
    >>> s.sqrt(-2j)
    (1-1j)
    >>> s.sqrt(1)
    (1+0j)
    """
    def __init__(self, value):
        self.previous = np.asarray(value,np.complex)
    def sqrt(self,z): 
        s = np.sqrt(np.complex(z))
        d1 = np.abs(self.previous - s)
        d2 = np.abs(self.previous + s)
        self.previous = ((d1 <= d2)*2-1)*s
        return self.previous
