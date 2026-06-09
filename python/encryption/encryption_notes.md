# Encryption: Diffie-Hellman & RSA

---

## Session 1: Modular Arithmetic + Diffie-Hellman

---

### Symmetric vs. Asymmetric Encryption

**Symmetric encryption:** Both parties share the same secret key.
- Fast, but requires a secure channel to exchange the key first.
- Examples: AES, DES.

**Asymmetric encryption:** Two different keys — a public key and a private key.
- Anything encrypted with the public key can only be decrypted with the private key.
- Solves the key distribution problem.
- Examples: RSA, ECC.

**The key exchange problem:** How do Alice and Bob agree on a shared secret over a public channel, without ever sending the secret itself?
Diffie-Hellman solves exactly this.

---

### Modular Arithmetic Review

`a mod n` is the remainder when `a` is divided by `n`.

```
17 mod 5 = 2
23 mod 7 = 2
```

**Properties:**
```
(a + b) mod n = ((a mod n) + (b mod n)) mod n
(a * b) mod n = ((a mod n) * (b mod n)) mod n
```

**Modular exponentiation:** `a^b mod n`

Naively computing `a^b` first and then taking mod is infeasible for large `b`.
Instead, use fast exponentiation:

```python
def mod_exp(base, exp, mod):
    result = 1
    base = base % mod
    while exp > 0:
        if exp % 2 == 1:          # if current bit is 1
            result = (result * base) % mod
        exp = exp // 2
        base = (base * base) % mod
    return result

# Example: 3^13 mod 7
print(mod_exp(3, 13, 7))  # => 3
```

This runs in **O(log exp)** multiplications.

---

### The Discrete Logarithm Problem

Given `g`, `p`, and `y = g^x mod p`, find `x`.

- Computing `g^x mod p` is easy (fast exponentiation).
- Finding `x` given `g^x mod p` is believed to be computationally hard for large primes `p`.

This asymmetry is the security foundation of Diffie-Hellman.

---

### Diffie-Hellman Key Exchange

**Setup (public):**
- A large prime `p`
- A generator `g` (a primitive root mod `p`)

**Protocol:**

| Step | Alice | Bob |
|------|-------|-----|
| 1 | Picks private `a` | Picks private `b` |
| 2 | Computes `A = g^a mod p` | Computes `B = g^b mod p` |
| 3 | Sends `A` to Bob | Sends `B` to Alice |
| 4 | Computes `s = B^a mod p` | Computes `s = A^b mod p` |

**Why they get the same secret:**
```
Alice: s = B^a mod p = (g^b)^a mod p = g^(ab) mod p
Bob:   s = A^b mod p = (g^a)^b mod p = g^(ab) mod p
```

An eavesdropper sees `g`, `p`, `A`, `B` — but recovering `a` or `b` requires solving the discrete logarithm problem.

**Python example:**

```python
p = 23   # public prime
g = 5    # public generator

# Alice's side
a = 6                        # Alice's private key
A = mod_exp(g, a, p)         # Alice's public value: 5^6 mod 23 = 8

# Bob's side
b = 15                       # Bob's private key
B = mod_exp(g, b, p)         # Bob's public value: 5^15 mod 23 = 19

# Shared secret
alice_secret = mod_exp(B, a, p)   # 19^6 mod 23
bob_secret   = mod_exp(A, b, p)   # 8^15 mod 23

print(alice_secret)   # 2
print(bob_secret)     # 2  <- same!
```

**Limitation:** DH establishes a *shared secret*, but does not encrypt messages by itself, and does not authenticate who you are talking to (man-in-the-middle attack is possible without authentication).

---

## Session 2: RSA

---

### Background: Euler's Totient Function

`φ(n)` counts how many integers from `1` to `n-1` are coprime to `n`.

For a prime `p`:
```
φ(p) = p - 1
```

For a product of two distinct primes:
```
φ(p * q) = (p - 1) * (q - 1)
```

**Fermat's Little Theorem** (stated without proof):

If `p` is prime and `gcd(a, p) = 1`, then:
```
a^(p-1) ≡ 1 (mod p)
```

**Euler's generalization:**
```
a^φ(n) ≡ 1 (mod n)    when gcd(a, n) = 1
```

This means:
```
a^(k * φ(n) + 1) ≡ a (mod n)    for any integer k ≥ 0
```

RSA is built on this fact.

---

### RSA: Key Generation

1. Choose two large distinct primes `p` and `q`.
2. Compute `n = p * q`.
3. Compute `φ(n) = (p-1) * (q-1)`.
4. Choose `e` such that `1 < e < φ(n)` and `gcd(e, φ(n)) = 1`.
   - Common choice: `e = 65537`.
5. Compute `d` such that `e * d ≡ 1 (mod φ(n))`.
   - `d` is the modular inverse of `e` mod `φ(n)`.
   - Computed using the Extended Euclidean Algorithm.

**Public key:** `(e, n)`  
**Private key:** `(d, n)`

---

### RSA: Encrypt and Decrypt

**Encryption** (using public key):
```
c = m^e mod n
```

**Decryption** (using private key):
```
m = c^d mod n
```

**Why it works:**
```
c^d = (m^e)^d = m^(e*d) mod n
```
Since `e * d ≡ 1 (mod φ(n))`, we have `e * d = k * φ(n) + 1` for some `k`, so:
```
m^(e*d) = m^(k*φ(n)+1) = (m^φ(n))^k * m ≡ 1^k * m ≡ m (mod n)
```

---

### RSA: Small Example by Hand

Let `p = 61`, `q = 53`.

```
n = 61 * 53 = 3233
φ(n) = 60 * 52 = 3120
e = 17       (gcd(17, 3120) = 1)
d = 2753     (17 * 2753 = 46801 = 15 * 3120 + 1)
```

Public key: `(17, 3233)`  
Private key: `(2753, 3233)`

Encrypt message `m = 65`:
```
c = 65^17 mod 3233 = 2790
```

Decrypt:
```
m = 2790^2753 mod 3233 = 65  ✓
```

---

### RSA: Python Implementation

```python
import math

def mod_exp(base, exp, mod):
    result = 1
    base = base % mod
    while exp > 0:
        if exp % 2 == 1:
            result = (result * base) % mod
        exp //= 2
        base = (base * base) % mod
    return result

def mod_inverse(e, phi):
    # Extended Euclidean Algorithm
    old_r, r = e, phi
    old_s, s = 1, 0
    while r != 0:
        q = old_r // r
        old_r, r = r, old_r - q * r
        old_s, s = s, old_s - q * s
    return old_s % phi

# Key generation
p, q = 61, 53
n = p * q
phi_n = (p - 1) * (q - 1)
e = 17
d = mod_inverse(e, phi_n)

print(f"Public key:  (e={e}, n={n})")
print(f"Private key: (d={d}, n={n})")

# Encrypt
m = 65
c = mod_exp(m, e, n)
print(f"Ciphertext: {c}")

# Decrypt
decrypted = mod_exp(c, d, n)
print(f"Decrypted:  {decrypted}")
```

---

### Extended Euclidean Algorithm

Used to find `d = e^(-1) mod φ(n)`.

**gcd via Euclidean algorithm:**
```
gcd(a, b) = gcd(b, a mod b)
gcd(a, 0) = a
```

**Extended version** also finds `x, y` such that `a*x + b*y = gcd(a, b)`.

```python
def extended_gcd(a, b):
    if b == 0:
        return a, 1, 0
    g, x, y = extended_gcd(b, a % b)
    return g, y, x - (a // b) * y

# Example: find d such that 17*d ≡ 1 (mod 3120)
g, x, _ = extended_gcd(17, 3120)
d = x % 3120
print(d)   # 2753
```

---

### Generating Large Primes

In practice, `p` and `q` are 1024-bit numbers or larger.
Python's `sympy` library can generate primes:

```python
from sympy import randprime, isprime

p = randprime(2**511, 2**512)
q = randprime(2**511, 2**512)
print(isprime(p))   # True
```

Or using Python's built-in `secrets` + Miller-Rabin primality testing.

---

## Session 3: Exercises & Practical Considerations

---

### Exercise 1 — DH by hand

Use `p = 23`, `g = 5`.  
Alice picks `a = 4`, Bob picks `b = 3`.

1. Compute Alice's public value `A`.
2. Compute Bob's public value `B`.
3. Compute the shared secret from each side.
4. Verify they match.

---

### Exercise 2 — RSA by hand

Use `p = 5`, `q = 11`.

1. Compute `n` and `φ(n)`.
2. Choose a valid `e`.
3. Find `d`.
4. Encrypt `m = 9`.
5. Decrypt the ciphertext.

---

### Exercise 3 — Code

Implement a function `rsa_encrypt_string(message, e, n)` that:
- Converts each character to its ASCII value.
- Encrypts each value using RSA.
- Returns a list of ciphertexts.

Implement the corresponding `rsa_decrypt_string(ciphertexts, d, n)`.

---

### Security Considerations

**Why RSA is hard to break:**
- Recovering `d` from `(e, n)` requires factoring `n = p * q`.
- Factoring large semiprimes is believed to be computationally hard (no polynomial algorithm known).
- Key sizes today: 2048 or 4096 bits.

**Why small examples are insecure:**
```python
# For n = 3233, an attacker can just try:
for p in range(2, 3233):
    if 3233 % p == 0:
        q = 3233 // p
        print(p, q)   # Found immediately
```

**Man-in-the-middle on DH:**
- DH alone does not authenticate Alice or Bob.
- In practice, DH is combined with certificates (TLS) or signatures (RSA/ECDSA) to verify identity.

**RSA in practice:**
- Raw RSA as described here is textbook RSA — not used directly.
- Real implementations add padding (OAEP) to prevent attacks.
- RSA is slow; in practice it is used only to encrypt a symmetric key (e.g., AES), and AES does the bulk encryption.
