## COUNTING SORT
 - Counting Sort is very time efficient and stable algorithm for sorting. Unlike bubble sort and merge sort, counting sort is not a comparison based algorithm. It        avoids comparisons and exploits the O(1) time insertions and lookup in an array.

### Algorithm for Counting Sort :-
    1. Algo: Counting Sort(A,B,K):
    2. for i <- 1 to k 
    3.    C[i] <- 0
    4. for j <- 1 to length[A]
    5.    C[A[j]] <- C[A[j]] + 1
    6. for i <- 2 to k
    7.    C[i] <- C[i] + C[i-1]
    8. for j <- length[A] down to 1
    9.    B[C[A[j]]] <- A[j]
    10.   C[A[j]] <- C[A[j]] - 1
