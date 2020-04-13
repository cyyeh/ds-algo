# python3
import random

def read_input():
    return (input().rstrip(), input().rstrip())

def print_occurrences(output):
    print(' '.join(map(str, output)))

def get_occurrences(pattern, text):
    def poly_hash(pattern, prime, x):
        ans = 0
        for c in reversed(pattern):
            ans = (ans * x + ord(c)) % prime
        return ans

    def precompute_hashes(text, pattern_length, prime, x):
        H = [None] * (len(text) - pattern_length + 1)
        S = text[len(text)-pattern_length : len(text)]
        H[len(text)-pattern_length] = poly_hash(S, prime, x)
        y = 1
        for _ in range(1, pattern_length + 1):
            y = (y * x) % prime
        for i in range(len(text)-pattern_length-1, -1, -1):
            H[i] = (x * H[i + 1] + ord(text[i]) - y * ord(text[i + pattern_length])) % prime
        return H

    prime = 1000000007
    x = random.randint(1, prime - 1)
    result = []
    p_hash = poly_hash(pattern, prime, x)
    H = precompute_hashes(text, len(pattern), prime, x)
    for i in range(len(text) - len(pattern) + 1):
        if p_hash != H[i]:
            continue
        if text[i:i+len(pattern)] == pattern:
            result.append(i)
    
    return result

if __name__ == '__main__':
    print_occurrences(get_occurrences(*read_input()))

