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

x = 38
print(mod_exp(12, x, 31))