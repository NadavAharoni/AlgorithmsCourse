import sys
import numpy as np

def matrix_multiply_naive(A, B):
    # check A.shape and B.shape and make sure that the matrices
    # are compatible for multiplication
    if False: # Replace with a condition that checks compatibility
        raise ValueError("Matrix dimensions are not compatible for multiplication")

    result_dtype = np.result_type(A.dtype, B.dtype)
    result_shape = (A.shape[0], B.shape[1])
    result = np.zeros(result_shape, dtype=result_dtype)

    number_of_multiplications = 0
    # write here python loops that calculate
    # each entry i,j in result,
    # and also updates number_of_multiplications
                
    return result, number_of_multiplications

def read_matrix(filepath: str) -> np.ndarray:
    try:
        return np.loadtxt(filepath, dtype=float)
    except Exception as e:
        raise ValueError(f"Failed to read matrix from '{filepath}': {e}") from e

def main():
    if len(sys.argv) != 3:
        print(f"Usage: {sys.argv[0]} <matrix_a_file> <matrix_b_file>")
        sys.exit(1)

    A = read_matrix(sys.argv[1])
    print(F"A.shape={A.shape}")
    B = read_matrix(sys.argv[2])
    print(F"B.shape={B.shape}")

    # result_np = A @ B
    # print(F"result_np=\n{result_np}")

    result_naive, number_of_multiplications = matrix_multiply_naive(A, B)
    # print(F"result_naive=\n{result_naive}")
    print(F"number_of_multiplications={number_of_multiplications}")

if __name__=='__main__':
    main()
