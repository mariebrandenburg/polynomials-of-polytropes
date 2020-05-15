# Volume, Ehrhart, and <img src="https://latex.codecogs.com/gif.latex?\dpi{250}h^*">-polynomials of polytropes

### Input files:
data.txt: classical vertices (pseudovertices) of polytropes. Each line contains the vertices of a representative of a maximal tropical type.

### Scripts:
- step1.py: Computes the Kleene star, converts it to a weight vector and computes a minimal prime
- step2.py: Applies [Alg. ] to compute the multivariate volume polynomial
- step3.py: Applies the Todd operator to the volume polynomial to compute the Ehrhart polynomial
- step4.py: Computes the h\*-polynomial from the Ehrhart polynomial using Eulerian polynomials

### Output:
- kleene_stars: Kleene stars and a minimal prime
- vol_pols: Multivatiate volume polynomials
- ehr_pols: Multivariate ehrhart polynomials
- h_star_pols: Multivariate h\*-polynomials

### Tests:
- comparison_vol_pols: Evaluates the multivariate volume polynomial at the weight vector from step 1. Independently computes the euclidean volume of the convex hull of the input points and compares the two.
- comparison_ehr_pols: Evaluates the multivariate Ehrhart polynomial at t\*(weight vector), using the weight vector from step 1. Independently computes the univariate Ehrhart polynomial of the convex hull of the input points and compares the two.
- comparison_h_star_pols: Evaluates the multivariate h\* polynomial at the weight vector from step 1. Independently attempts to compute the univariate h\* polynomial of the convex hull of the input points and compares the two. Kills the computation if this takes longer than `MAX_WAITING_TIME = 7 * 60` seconds.

### Affine Hull:
- polynomials_to_points.py: Converts multivariate polyomials for d=4 to points in the vector space of homogeneous polynomials of degree 4 in 20 variables. 
- affine_hull_of_points.py: Computes the dimension of the affine hull of the above points.
- output_vectors.txt: Multivariate polyomials for d=4 as points in the vector space of homogeneous polynomials of degree 4 in 20 variables. 

### Example run (d=3):
Compute all volume, Ehrhart and h\*-polynomials for d=3 at once:
```
cat in/3d_data.txt | sage 3d_step1.py | tee out/3d/3d_kleene_stars.txt | sage 3d_step2.py | tee out/3d/3d_vol_pols.txt | sage 3d_step3.py | tee out/3d/3d_ehr_pols.txt | sage 3d_step4.py > out/3d/3d_h_star_pols.txt
```

### Dependencies:
All scripts are written for Sage (version ), using an interface to Macaulay2 (version ).
For some of the scripts the normaliz package of sage is needed. To install it, run
	``` sage -i pynormaliz ```

Note that you need Macaulay2 to be installed and the M2 command available under in your `PATH` to use the Sage interface to Macaulay2.
