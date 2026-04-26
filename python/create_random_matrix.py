import numpy as np

def create_random_matrix(shape: tuple) -> np.ndarray:
    rng = np.random.default_rng()
    matrix = np.round(rng.uniform(-100, 100, size=shape), 2)
    
    # Print aligned
    for row in matrix:
        print("  ".join(f"{x:6.2f}" for x in row))
    
    return matrix

def main():
    create_random_matrix((12,9))
    

if __name__=='__main__':
    main()

