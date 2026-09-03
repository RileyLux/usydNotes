The **SHAttered** attack in February 2017 was the first real-world **collision attack** against SHA-1, proving that the algorithm was no longer secure.

It was executed by researchers from **CWI Amsterdam** and **Google**, who successfully generated two entirely different PDF files that produced the exact same SHA-1 hash.

---
## 📂 The Practical Proof
To prove the vulnerability, the researchers created **two distinct PDF documents**:

1. Document A had a **blue background**.
2. Document B had a **green background** and entirely different internal content.

When run through the SHA-1 algorithm, both files generated the exact same hash: `38762cf7f55934b34d179ae6a4c80cadccbb7f0a`.

If a system relied solely on SHA-1 to verify files, it would treat these two completely different documents as identical. In a real-world scam, an attacker could use this trick to get someone to digitally sign a harmless contract, then swap it out for a fraudulent one with the same hash.

## ⚙️ How the Attack Worked
The attack relied on a technique called an **identical-prefix collision**:

- **The Setup:** The researchers started with a shared piece of data (the prefix) that was identical in both files.
- **The Manipulation:** They calculated specific, subtle variations in the next chunks of data (the collision blocks). These variations were designed to trick the SHA-1 mathematical formula.
- **The Equalizer:** The math was engineered so that the internal differences introduced in the files would perfectly cancel each other out by the end of the calculation, resulting in the same final output.

## 💻 The Massive Computing Power Required
While a collision is mathematically possible by pure luck (the [[Birthday Paradox]]), doing it by brute force would take lifetimes. The SHAttered attack used clever mathematics to reduce the required effort by **100,000 times**, though it still required immense computing power:

- The computation took **9 quintillion** (9,000,000,000,000,000,000) SHA-1 calculations.
- It required processing power equivalent to **6,500 years** of a single CPU working non-stop.
- It required processing power equivalent to **110 years** of a single graphics card (GPU) working non-stop.

While that sounds like a lot, a well-funded criminal organization or a nation-state cloud infrastructure could easily pull it off. This real-world proof forced major tech companies to immediately drop SHA-1 support for digital signatures, web certificates, and file verification.