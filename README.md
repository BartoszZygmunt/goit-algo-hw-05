# Substring Search Algorithms Efficiency Comparison

## Introduction
This document compares the efficiency of three substring search algorithms: Boyer-Moore, Knuth-Morris-Pratt (KMP), and Rabin-Karp. The comparison is based on two text files (Article 1 and Article 2) with substrings that exist in the text and substrings that do not.

## Methodology
The efficiency of each algorithm was measured using the `timeit` module in Python. The execution time was recorded for each algorithm when searching for an existing substring and a non-existing substring.

## Results

### Article 1

| Algorithm          | Substring              | Time (seconds) |
|--------------------|------------------------|----------------|
| Boyer-Moore        | "алгоритм"             | 0.000436       |
| Knuth-Morris-Pratt | "алгоритм"             | 0.002214       |
| Rabin-Karp         | "алгоритм"             | 0.001879       |
| Boyer-Moore        | "неіснуюча_підрядка"   | 0.000160       |
| Knuth-Morris-Pratt | "неіснуюча_підрядка"   | 0.002838       |
| Rabin-Karp         | "неіснуюча_підрядка"   | 0.003296       |

### Article 2

| Algorithm          | Substring              | Time (seconds) |
|--------------------|------------------------|----------------|
| Boyer-Moore        | "алгоритм"             | 0.000483       |
| Knuth-Morris-Pratt | "алгоритм"             | 0.001599       |
| Rabin-Karp         | "алгоритм"             | 0.003913       |
| Boyer-Moore        | "неіснуюча_підрядка"   | 0.000226       |
| Knuth-Morris-Pratt | "неіснуюча_підрядка"   | 0.003124       |
| Rabin-Karp         | "неіснуюча_підрядка"   | 0.003513       |

## Conclusion
- **Article 1**: The fastest algorithm for existing substrings was Boyer-Moore, and for non-existing substrings was Boyer-Moore.
- **Article 2**: The fastest algorithm for existing substrings was Boyer-Moore, and for non-existing substrings was Boyer-Moore.
- **Overall**: The Boyer-Moore algorithm demonstrated the best performance across both texts for both existing and non-existing substrings.

The choice of the fastest algorithm may vary depending on the specific text and the nature of the substring being searched. However, based on the data obtained, the Boyer-Moore algorithm generally provides the best performance.
