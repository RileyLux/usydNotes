>Each digit is a power of 16
{1, 2, 3, 4, 5, 6, 7, 8, 9, A, B, C, D, E, F}

### Converting from Binary
- Separate bit stream into groups of 4 (right to left)
- Do binary conversion on each group
- Combine digits

### Converting to decimal
eg:
$$
24A8_{16} = 2\times16^3 + 4\times16^2+A\times16^1+8\times16^0
$$
$$
=
2\times4096+4\times256+10\times16+8\times1=9384_{10}
$$
