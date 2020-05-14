import sys
from sage.all import *
from sage.interfaces.macaulay2 import Macaulay2

macaulay2 = Macaulay2()

def eulerian_numbers(n):
     r'''
     Computes the Eulerian numbers up to A(n,n).
     OUTPUT:
     An n+1 by n+1 matrix of the Eulerian numbers up to A(n,n).
     '''
     A = zero_matrix(n+1,n+1)
     A[0,0] = 1
     for i in range(1,n+1):
         A[i,0] = 0
         A[i,1] = 1
     for j in range(2,n+1):
         for k in range(2,j+1):
             if j == k:
                 A[j,k] = 1
             else:
                 A[j,k] = (j-k+1)*A[j-1,k-1] +k*A[j-1,k]
     return(A)

def eulerian_polynomial(n):
    r'''
    Computes the nth Eulerian polynomial.
    '''
    R = PolynomialRing(ZZ, 't')
    t = R.gen()
    A = eulerian_numbers(n)
    return(R.sum( A[n,i]*t**i for i in range(n+1)))

def ehr_to_hstar(ehr_poly_coeffs):
    r'''
    Convert the Ehrhart polynomial of a lattice polytope to the h* polynomial.
    The Ehrhart series can be rewritten as follows:
    $$Ehr_P(t) = \sum_{m\geq 0}ehr_P(m)t^m 
               = \sum_{m\geq 0}\sum_{j \geq 0}^{d}c_j m^j t^m.$$ 
    The numerator of the rational expression for the series
    $\sum_{m\geq 0 }m^j t^m $ is an Eulerian polynomial. This function uses
    the Eulerian polynomials to transform from the Ehrhart polynomial to the
    h* polynomial.
    INPUT:
    
    - ``ehr_poly`` - a polynomial in 't' with rational coefficients. The output
      of the ``ehrhart_polynomial`` function. 
    OUTPUT:
    The h* polynomial as a polynomial in 't' with nonnegative integral 
    coefficients.
    
    EXAMPLE:
    The h* polynomial of a unimodular simplex is always one. Here we test the 
    conversion for a 4-dimensional simplex::
        sage: p = polytopes.simplex(4)
        sage: e = p.ehrhart_polynomial()
        sage: ehr_to_hstar(e)
        1
    '''
    # change the polynomial into a vector
    #Ring = PolynomialRing(QQbar, 't')
    #t = Ring.gen()
    ehr_poly = ehr_poly_coeffs
    # get the dimension of the polytope
    d = len(ehr_poly)-1
    # compute the h* polynomial
    factors = zero_vector(d+1)
    factors = factors.change_ring(R)
    for j in range(d+1):
        factors[j] = ehr_poly[j]*(1-t)**(d-j)*eulerian_polynomial(j)
    return sum(factors)

def get_terms(polynomial_as_string):
    R2 = macaulay2('QQ['+','.join(['a'+str(i)+str(j) for i in range(1,5) for j in range(1,5) if not i==j])+', t'+']')
    poly = macaulay2(polynomial_as_string)
    terms = [x.external_string() for x in poly.terms()]
    deg = poly.degree()[0]
    c = [0]*(int(deg)+1)
    for term in terms:
        g = R(term)
        deg_g = g.degree()
        c[deg_g]=c[deg_g]+g
    return c

R = PolynomialRing(QQ,','.join(['a'+str(i)+str(j) for i in range(1,5) for j in range(1,5) if not i==j])+', t')
a12, a13, a14, a21, a23, a24, a31, a32, a34, a41, a42, a43, t = R.gens()

for line in sys.stdin:
    line = line.rstrip()    
    print(ehr_to_hstar(get_terms(line)))