---
marp: true
theme: default
paginate: true
class: lead
math: katex
---

# 🧮 Math Refresher for Algorithms

---

## 📘 Motivation

Before diving into algorithms, we need to recall some key **mathematical tools** used to analyze them:
- Powers and exponents  
- Logarithms  
- Growth rates and asymptotic intuition  

---

## ⚡ Powers and Exponents

---

### Exponent Basics

For any real numbers $a, b$:

$$
a^b = \underbrace{a \times a \times \dots \times a}_{b \text{ times}}
$$

Examples:
- $2^3 = 8$
- $5^0 = 1$
- $a^{-n} = \frac{1}{a^n}$

---

### ⚙️ Why $a^{-n} = \frac{1}{a^n}$

We want exponent rules to stay **consistent** for all exponents, including negatives.

Recall:

$$
a^m \cdot a^n = a^{m+n}
$$

Let’s set $m = n$ and $n = -n$:

$$
a^n \cdot a^{-n} = a^{n + (-n)} = a^0
$$

We know $a^0 = 1$.  
Therefore:

$$
a^{-n} = \frac{1}{a^n}
$$

✅ This definition keeps all exponent rules valid for **negative exponents**.

---

### Power Rules Recap

$$
\begin{align*}
a^m \cdot a^n &= a^{m+n} \\
\frac{a^m}{a^n} &= a^{m-n} \\
(a^m)^n &= a^{m \cdot n} \\
(ab)^n &= a^n \cdot b^n \\
\left(\frac{a}{b}\right)^n &= \frac{a^n}{b^n}
\end{align*}
$$

---

### Common Powers

| Expression | Value | Comment |
|-------------|--------|----------|
|$2^{10}$| 1024 | ≈$10^3$|
|$10^6$| 1,000,000 | “a million” |
|$n^2$, $n^3$| quadratic, cubic | appear in algorithm complexity |

---

## 🔢 Logarithms

---

### Definition

The logarithm is the **inverse of exponentiation**:

$$
\log_b(a) = c \quad \Leftrightarrow \quad b^c = a
$$

Examples:
- $\log_2(8) = 3$
- $\log_{10}(100) = 2$

---

### Logarithm Rules

$$
\begin{align*}
\log_b(xy) &= \log_b(x) + \log_b(y) \\
\log_b\left(\frac{x}{y}\right) &= \log_b(x) - \log_b(y) \\
\log_b(x^k) &= k \cdot \log_b(x) \\
\log_b(a) &= \frac{\log_k(a)}{\log_k(b)} \quad \text{(Change of base)}
\end{align*}
$$

---

### 📐 Proof: Change of Base Formula

We want to show:
$$
\log_b(a) = \frac{\log_k(a)}{\log_k(b)}
$$

**Proof:**

Let: $x = \log_b(a)$
By definition, this means: $b^x = a$

Now take $\log_k$ (any other base) of both sides:
$$
\log_k(b^x) = \log_k(a)
$$

---

### 📐 Proof: Change of Base Formula (2)

Using the power rule:
$$
x \cdot \log_k(b) = \log_k(a)
$$

Solve for $x$:
$$
x = \frac{\log_k(a)}{\log_k(b)}
$$

Since $x = \log_b(a)$, we have proven:
$$
\boxed{\log_b(a) = \frac{\log_k(a)}{\log_k(b)}}
$$

---

### Common Bases

| Base | Name | Usage |
|-------|-------|--------|
| 2 | binary logarithm | used in CS (trees, sorting, binary search) |
| e ≈ 2.718 | natural log | used in calculus, continuous growth |
| 10 | common log | used in decimal systems |

---

### Relationship Between Logs and Powers

$$
b^{\log_b(a)} = a, \quad \log_b(b^x) = x
$$

---

### Important Values

| Expression | Approximation |
|-------------|---------------|
|$\log_2(1{,}024)$| 10 |
|$\log_2(1{,}000{,}000)$| ≈ 20 |
|$\log_{10}(2)$| 0.301 |
|$\log_2(10)$| 3.322 |

---

## 📈 Growth Intuition

---

### Comparing Growth Rates

| Function | Growth Type | Example Use |
|-----------|--------------|--------------|
| $\log n$| very slow | binary search |
| $n$| linear | simple loops |
| $n \log n$| sub-quadratic | merge sort |
| $n^2$| quadratic | nested loops |
| $2^n$| exponential | brute force |

---

### Logarithms Shrink Big Numbers

Example:
$$
n = 1{,}000{,}000 \quad \Rightarrow \quad \log_2(n) \approx 20
$$
So a binary algorithm cuts down work **from a million steps to 20!**

---

### Exponential Growth is Explosive

$$
2^{10} = 1{,}024, \quad 2^{20} \approx 10^6, \quad 2^{30} \approx 10^9
$$

Even a small increase in exponent has a **huge impact**.

---

## 🧩 Exercises

---

### 🔹 Exercise 1 — Exponent Logic

Explain *why* the following must be true using the rule $a^m \cdot a^n = a^{m+n}$:

1. $a^0 = 1$ 
2. $a^{-3} = 1 / a^3$

---

### 🔹 Exercise 2 — Logarithm Identities

Simplify using logarithm rules:

1. $\log_2(8) + \log_2(4)$ 
2. $\log_3(81) - \log_3(9)$ 
3. $\log_2(2^k)$

---

### 🔹 Exercise 3 — Change of Base Practice

Compute each value using $\log_{10}$ and the change of base formula:

1. $\log_2(32)$ 
2. $\log_5(125)$

---

### 🔹 Exercise 4 — Growth Comparison

Order the following functions by growth rate (slowest → fastest):

$n$, $2^n$, $\log n$, $n \log n$, $n^2$

Explain your reasoning.

---

## 🧩 Summary

- Powers grow quickly; logs grow slowly.  
- Negative exponents make sense once we demand consistent rules.  
- Logs and powers are inverses.  
- The log base-change formula comes directly from exponent definitions.  
- Understanding their behavior helps estimate algorithm performance.
