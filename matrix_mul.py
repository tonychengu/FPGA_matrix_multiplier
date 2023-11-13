import numpy as np

def matrix_mul(A, B, Col1, Row1, Row2):
    C = Col1*Row2 * [0]
    for i in range(Col1):
        for j in range(Row1):
            for k in range(Row2):
                C[i*Row2+k] += A[i*Row1+j] * B[j*Row2+k]
    return C

def main():
    MINSIZE = 2
    MAXSIZE = 10
    for i in range(3):
        c1 = np.random.randint(MINSIZE, MAXSIZE)
        r1 = np.random.randint(MINSIZE, MAXSIZE)
        r2 = np.random.randint(MINSIZE, MAXSIZE)
        A = np.random.randint(1,200, size =(c1,r1))
        B = np.random.randint(1,200, size =(r1,r2))
        C = matrix_mul(A.flatten(), B.flatten(), c1, r1, r2)
        C = np.array(C)
        test_C = C.reshape(c1, r2)
        real_C = np.matmul(A, B)
        status = "Failed"
        if(np.array_equal(real_C, test_C)):
            status = "Passed"
        print("Test %d %s" % (i+1, status) )
        print("C: ", C)
        print("real_C: ", real_C)

if __name__ == "__main__":
    main()