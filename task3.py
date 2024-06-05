import timeit

# Function to read file with error handling for encoding issues
def read_file(filepath):
    with open(filepath, 'rb') as file:
        raw_data = file.read()
    return raw_data.decode('utf-8', errors='ignore')

# Load the articles
article1 = read_file('./article1.txt')
article2 = read_file('./article2.txt')

# Boyer-Moore Algorithm
def boyer_moore(text, pattern):
    m = len(pattern)
    n = len(text)
    if m == 0:
        return 0
    last = {}
    for i in range(m):
        last[pattern[i]] = i
    i = m - 1
    j = m - 1
    iterations = 0
    while i < n:
        iterations += 1
        if text[i] == pattern[j]:
            if j == 0:
                return iterations, i
            else:
                i -= 1
                j -= 1
        else:
            lo = last.get(text[i], -1)
            i += m - min(j, 1 + lo)
            j = m - 1
    return iterations, -1

# Knuth-Morris-Pratt Algorithm
def kmp_search(text, pattern):
    n = len(text)
    m = len(pattern)
    lps = [0] * m
    j = 0
    compute_lps_array(pattern, m, lps)
    i = 0
    iterations = 0
    while i < n:
        iterations += 1
        if pattern[j] == text[i]:
            i += 1
            j += 1
        if j == m:
            return iterations, i - j
        elif i < n and pattern[j] != text[i]:
            if j != 0:
                j = lps[j-1]
            else:
                i += 1
    return iterations, -1

def compute_lps_array(pattern, m, lps):
    length = 0
    i = 1
    while i < m:
        if pattern[i] == pattern[length]:
            length += 1
            lps[i] = length
            i += 1
        else:
            if length != 0:
                length = lps[length-1]
            else:
                lps[i] = 0
                i += 1

# Rabin-Karp Algorithm
def rabin_karp(text, pattern, q=101):
    d = 256
    n = len(text)
    m = len(pattern)
    p = 0
    t = 0
    h = 1
    iterations = 0
    for i in range(m-1):
        h = (h * d) % q
    for i in range(m):
        p = (d * p + ord(pattern[i])) % q
        t = (d * t + ord(text[i])) % q
    for i in range(n - m + 1):
        iterations += 1
        if p == t:
            if text[i:i+m] == pattern:
                return iterations, i
        if i < n - m:
            t = (d * (t - ord(text[i]) * h) + ord(text[i + m])) % q
            if t < 0:
                t = t + q
    return iterations, -1

# Define substrings to search
existing_substring = "алгоритм"  # Exists in both articles
non_existing_substring = "неіснуюча_підрядка"  # Does not exist

# Benchmarking function
def benchmark_search(text, pattern, search_function):
    setup_code = f'''
from __main__ import {search_function}
text = {repr(text)}
pattern = {repr(pattern)}
'''
    test_code = f'{search_function}(text, pattern)'
    times = timeit.repeat(setup=setup_code, stmt=test_code, repeat=5, number=1)
    return min(times)

# Measure execution times
results = []

for article, name in [(article1, "Article 1"), (article2, "Article 2")]:
    for pattern in [existing_substring, non_existing_substring]:
        for search_function in ["boyer_moore", "kmp_search", "rabin_karp"]:
            time_taken = benchmark_search(article, pattern, search_function)
            results.append((name, pattern, search_function, time_taken))

# Print results
for result in results:
    print(f"Text: {result[0]}, Pattern: '{result[1]}', Algorithm: {result[2]}, Time: {result[3]} seconds")


