from sympy import Matrix

#define matrix
A = Matrix([[17,22,27],[22,29,36],[27,36,45],])

#print Eigenvalues and Eigenvectors
print(A.eigenvals())

print(A.eigenvects())