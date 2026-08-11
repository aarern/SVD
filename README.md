# SVD
Singular value decomposition walkthrough and a broader linear algebra crash course

# Linear algebra crash course:
Linear algebra is the study of transformations of vectors and matrices. It's the foundation for how computers calculate, and it can be used for optimization and deeper data analysis.

A vector has direction and magnitude. In space, it's an arrow pointing in some x, y, and z direction with some length.

A matrix can be thought of as something that acts on a vector. It can change its direction or magnitude. 

Example:

Consider a vector in 3-D space that takes the form v = [x, y, z], and a 3x3 matrix "A" that takes the form [x y z, x y z, x y z].

Suppose the vector took the form v = [0, 1, 0]; then the vector would point only in the direction of the y-axis. 

A matrix is a grid of numbers, with each column representing a unique vector in space.

We can apply (multiply) vectors and matrices together to change the position of the arrow, so long as the columns of the matrix equal the rows of the vector.

Going back to our example of the vector v = [0, 1, 0], let's suppose we wanted to change its direction and magnitude so that it's rotated 90 degrees clockwise around the z-axis, and is twice as long.

We could multiply the vector v by the matrix A = [0 2 0, 0 0 0, 0 0 0]. The expression Av = [0 2 0, 0 0 0, 0 0 0] [0, 1, 0] simplifies to Av = [0*0 + 1*2 + 0*0, 0*0 + 1*0 + 0*0, 0*0 + 1*0 + 0*0] = [2, 0, 0].

If a matrix is a combination of vectors, and you can use matrixes to change vectors, could you use matrix A times some different vector to get you vector v? If you take for example the matrix A = [4 3 1, 2 7 2, 6 1 9], and imagine it's three vectors (v1 = [4, 2, 6], v2 = [3, 7, 1], v3 = [1, 2, 9]) in space:

Let's construct a parallelepiped from the three vectors (a 3-D parallelogram). The determinant is simply the volume of the parallelepiped. If this matrix were 2-D, i.e., its vector columns exist only on the x- and y-axes (v = [x, y]), then the volume of the parallelepiped would be zero.

We care about the determinant because it tells us if we can construct a vector going in all directions using a matrix. If the matrix is not zero (if volume exists), then we can construct a vector going in all directions.


# Matrixes:
A matrix is special because it can contain any sample and corresponding variables. For example, each column could represent a Fortune 500 company, and each row could contain profitability metrics. This is simply a table, but with linear algebra, you can construct a matrix and then factorize to compare the different companies across many dimensions (metrics). 

First, we need to briefly understand the identity matrix, row-reduced echelon form, inverses, and transposes.


#Identity Matrix:
The identity matrix is a square matrix with a 1 in all "pivot" positions. Pivot positions identify a unique variable. For the 2x2 identity matrix, I, it takes the form I = [1 0, 0 1]. 


#Row Reduced Echelon Form (RREF):
We can construct a matrix out of a system of equations to find a solution. For example, take the line formulas 2x+y=4 and x-y=1; we can create an "augmented matrix" that represents these formulas. The augmented matrix A = [2 1 | 4, 1 -1 | 1], where "|" represents the equals sign.

RREF is a reduction method used to obtain the identity matrix on the left-hand side and a solution on the right-hand side. Here, when we reduce the matrix, we'll find where the two lines intersect. Using the notation "R1" for row one and "R2" for row two, we reduce as follows.  Negative R1 implies A = [2 1 | 4, -1 1 | -1], R1 is calculated as R1-R2 implies A = [3 0 | 5, -1 1 | -1]. R2 scaled by three implies A = [3 0 | 5, -3 3 | -3]. R2 becomes R2+R1 implies A = [3 0 | 5, 0 3 | 2]. R1 and R2 scaled by 1/3 implies A = [1 0 | 5/3, 0 1 | 2/3]. Thus, the lines intersect at x = 5/3, y = 2/3.


# Inverses:
Now that we understand reduction and the identity matrix, we can learn inverses. An inverse is the reverse of a function. With respect to matrices, the inverse is the opposite of a matrix. Inverses can only be found for square matrices. An important identity is that for a square matrix A and its inverse ("A^-1"), A * A^-1 = I, and A^-1 * A = I. The product of a square matrix and its inverse produces the identity matrix.

For a simple 2x2 matrix A with the form A = [a b, c d], the inverse is calculated by the formula A^-1 = 1/(ad-bc) * [d -b, -c a]. It's important to note that the calculation "ad-bc" is the determinant of matrix A.

For larger matrices, the inverse is not calculated as easily. A method used to find the inverse of a matrix is the Gauss-Jordan elimination method. If we follow the rule that a matrix times its inverse produces the identity matrix, written as [A | I], then if we take the inverse of A on the left-hand side, we can simplify A^-1 * A to I, and the right-hand side becomes A^-1 * I. The right-hand side simplifies because anything applied to the identity matrix returns itself, like how anything times one is itself. Thus, we have [I | A^-1], and we found the inverse.

A quick example is as follows:
If A = [5 8 1, 2 5 1, 1 4 5], we can construct the augmented matrix [5 8 1 | 1 0 0, 2 5 1 | 0 1 0, 1 4 5 | 0 0 1], and applying the same row reduction techniques used above, the left hand side turns into the identity matrix, and the right hand side is the inverse of matrix A, [I | A^-1] = [1 0 0 | 3/5 -1 0, 0 1 0 | -1/4 2/3 0, 0 0 1 | 0 -1/3 1/4].


# Transpose:
Transposes are much more straightforward. It's simply taking the columns of a matrix and making them the rows. For matrix A, its transpose is represented by A^T. Note: any matrix times its transpose creates a square matrix, even if the original matrix A is not a square. 

Eigenvectors, Eigenvalues, Diagonalization:
Starting with Eigenvectors, an Eigenvector is a special vector that does not change direction when transformed by a matrix. For example, consider matrix A = [2 1, 1 2]. If we transform the vector v = [1, 1] by matrix A, we get the new vector A*v = [3, 3]. Notice how the direction of the arrow has not changed (on a 2-D graph, the arrow drawn starts at the origin (0, 0) and goes to (1, 1). If the arrow did change directions, suppose the transformed vector became v = [2, 1]. Since this vector is not parallel to the original vector v = [1, 1], v = [2, 1] is not an eigenvector of matrix A. Since our original transformation produced A*v = [3, 3], and A*v is parallel to v = [1, 1], vector v = [1, 1] is an Eigenvector of the specific Matrix A.

So to summarize, Eigenvectors are "stubborn" vectors that do not change direction when transformed by a specific matrix A; they can only change in magnitude and can reverse if multiplied by a negative number.

Next, to understand eigenvalues, we first must know what a scalar is. Scalars are simply values multiplied to a vector or matrix to increase its scale. Take, for example, the 3-D vector v = [1, 1, 1], and the scalar s = 5. We can scale the vector up with the formula s*v = [5, 5, 5]. If we imagine vector v as an arrow, s*v is an arrow with five times the magnitude.

Similarly, Eigenvalues are scalars that describe how the corresponding Eigenvector is scaled when transformed by a matrix A.

To show that, we'll use the formula A = P*D*P^-1, where matrix A is equal to the product of its Eigenvector matrix (P), its diagonal matrix (D), and the inverse of the Eigenvector matrix (P^-1). It's important to keep Eigenvalues attached to respective Eigenvectors. In other words, where ev is an eigenvector, and matrix P = [ev_1, ev_2]. Matrix D's only numbers will be its eigenvalues in each pivot position, i.e., D = [λ_1 0, 0 λ_2]. 

Take, for example, matrix A = [3 5, 0 -6]. Its eigenvectors are ev_1 = [-5, 9], and ev_2 = [1, 0]. Thus, we construct the matrix P = [-5 1, 9 0]. To see if it has an inverse, we calculate the determinant as det(P) = -5*0 - 1*9 = 0-9 = -9. Since the determinant is not zero, our matrix P has an inverse. 

Recall: 
For a simple 2x2 matrix A with the form A = [a b, c d], the inverse is calculated by the formula A^-1 = 1/(ad-bc) * [d -b, -c a]. It's important to note that the calculation "ad-bc" is the determinant of matrix A.

Thus, P^-1 = -1/9 * [0 -1, -9 -5] = [0 -1/9, 1 5/9].

Our eigenvalues are λ_1 = -6 and λ_2 = 3, and our diagonal matrix D = [-6 0, 0 3].

We can check our formula A = P*D*P^-1 now by performing the first matrix multiplication P*D. P*D = [-5 1, 9 0]*[-6 0, 0 3]. We'll use the dot product rule to perform the matrix multiplication. Recall matrices are just collections of vectors. If that's the case, then we'll start taking vector v = [-6, 0] from matrix D, and multiplying that by matrix P. Taking the first row of our first vector v (-6) and multiplying that by the first vector of matrix P ([-5, 9]), our product is P_1*D_1 = [30, -54]. 

Applying this same process of multiplying the second eigenvalue by the second eigenvector produces λ_2*ev_2 = 3*[1, 0] = [3, 0]. Thus, our matrix P*D = [30 -6, -54 0]. If we now follow the same steps and multiply the matrix P^-1, our expression P*D*P^-1 returns the matrix A = [3 5, 0 -6].


# Diagonalization:
Now that we understand Eigenvalues, Eigenvectors, and the formula for deriving them, Let's walk through the full example of diagonalization, which is the process that isolates the Eigenvalues and Eigenvectors from a given matrix. Note: the matrix must be square and invertible to be diagonalized.

The process of diagonalization looks like solving for the Eigenvalues, solving for the Eigenvectors, then taking the inverse of the eigenvector matrix to check if it produces A.

To solve for the eigenvalues, use the formula det(A-λI) = 0. For our matrix A = [3 5, 0 -6], our setup is |3-λ 5, 0 -6-λ| = 0; the determinant of this matrix is (3-λ)(-6-λ) - 5*(0) = 0, which simplifies to λ^2+3λ-18 = 0. Factoring the quadratic gives the Eigenvalues λ = -6, λ = 3.

Now we have to find the Eigenvector that corresponds to each Eigenvalue. 

For λ = -6, we set up (A-λI)v=0, which expands to ([3 5, 0 -6]-[-6 0, 0 -6])v = 0, which simplifies to [9 5, 0 0]v = 0. We have to find a non-trivial vector that produces the null vector ([0, 0]). We'll use x1 and x2 to denote the columns of matrix [9 5, 0 0]. Our equation is 9*x1+5*x2 = 0. Additionally, x2 is a free variable because there is no value in the pivot position; thus, x2 = t. This implies our formula is 9*x1 + 5*t = 0, and x1 = -5/9*t. Extracting t, our Eigenvector  ev_1 = t*[-5/9, 1], for simplicity, we'll use t = 9, and our expression is ev_1 = [-5, 9]. 

For λ = 3, we set up (A- λI)v = 0, which expands to ([3 5, 0 -6] - [3 0, 0 3])v = 0, which simplifies to [0 5, 0 -9]v = 0. We have to find a non-trivial vector that produces the null vector ([0, 0]). We'll use x1 and x2 to denote the columns of matrix [0 5, 0 -9]. the first formula is 0*x1 + 5*x2 = 0, and 0*x1-9*x2=0. Since both values in the first column are zero, x1 = t. Additionally, zero times our second column is a requirement to produce the 0. Therefore, the linear combination needed to produce the null vector is ev_2 = t*[1, 0], which, using t = 1, produces ev_2 = [1, 0]. Note: we could use any number other than zero for 1, but 1 is the simplest option, because if we used 5, our Eigenvector would be v = [5, 0], and our transformation (A-λI)v still produces the null vector.

Our Eigenvector matrix is P = [-5 1, 9 0], and its inverse is P^-1 = [0 -1/9, 1 5/9].

Checking to see if it all works, A = ([-5 9, 1 0]*[-6 0, 0 3])*[0 -1/9, 1 5/9] = [3 5, 0 -6].


# Singular Value Decomposition:

Singular Value Decomposition (SVD) is used to factorize any matrix, not just square matrices like for diagonalization. Our formula is A = UΣV^T, where U is the unit Eigenvectors of A*A^T, V^T is the transposed matrix of A*A^T, and sigma is the singular values of A (the square roots of the Eigenvalues). It's important to note the singular values represent the strength of each component.

SVD has many applications, but in recent times it's been used for "taming the factor zoo". There are many factors with predictive power when modeling a stock's returns, but SVD is used to break all of these factors into principal components. Principal components are simplified factors that combine many factors used at different weights. Principal components keep only the factors that explain the most variance in the independent predictor dataset, and drop "noisy" predictors.

Another interesting point about SVD is that you can select how much variability you want to explain from your independent dataset. People can select to explain 90% variability, or more, but know the more variability you want to explain, the more principal components you'll use in any regressions. You measure the variability you chose to explain by squaring singular values and finding the cumulative variation of each as you descend the singular value matrix.

SVD Process:

Take a matrix A, transpose it => A^T, then multiply A^T*A. Then diagonalize and find Eigenvalues and Eigenvectors of A. Filter any negative or zero eigenvalues, and take the square root of those Eigenvalues to obtain the singular values. Create a singular value matrix in order of greatest to least (Sigma), then take the Eigenvector matrix and multiply by 1 over the magnitude of each vector to get the unit Eigenvector matrix (U). Transpose V => V^T, and A = U*Sigma*V^T, and back solve to get U1, U2, ..., Un columns.

Example of Isolating the Unit Eigenvector Matrix:
First take A*V (since V^T*V = I), then AV = U*sigma. AV1*(1/sigmaV1) = U1, AV2*(1/sigmaV2) = U2. U = [U1 U2].

Basically, A was broken into its most important components; the steps are flipping/rotating with V^T, then stretching by the singular values matrix (sigma), then flipping/rotating again by matrix U. The principal components are obtained by multiplying matrix U by matrix Sigma.
