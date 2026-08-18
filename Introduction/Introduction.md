---
Week: "1"
Date: 2026-08-03
Slides Link: "[Week 1 Lecture](https://canvas.sydney.edu.au/courses/73745/files/51861267?module_item_id=3245897)"
tags:
  - Binary
  - Hexadecimal
  - Decimal
  - Data_representation
  - Data
  - Unicode
  - Machine_Instructions
---

---
## [[Decimal Number System]]
- 10 Available symbols
	- {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
- Each position is a power of 10

## [[Binary Number System]]
- 2 Symbols
	- {0, 1}
- Each position is a power of 2

## [[Hexadecimal Number System]]
- 16 symbols
	- {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, A, B, C, D, E, F}
- Represents much bigger numbers using less characters
---
## Data Representation
- ASCII Character codes use 7 bots (128 different possible characters)
	- Cant represent other languages (e.g French, Chinese)
- in 1991 a new character code was released, **Unicode**
	- Uses 32 bits, so it can represent over 4 billion characters
	- Includes almost every language, as well as other older symbols an emojis

---
## Machine Instructions
- Operates at cpu level
- Data (characters and numbers) and **program instructions** are stored in the [[RAM|Memory]] of the computer
- Computer programs are translated into machine instructions, that are then loaded into memory and executed by the CPU

---
## Operating Systems
- Simple system consists of Memory + CPU + Input/Output devices
- Program instructions stored in memory, then executed by the CPU
- However more advanced [[OS Systems]] provide more features
- CPU has two modes of operation, **System** and **User**
	- To switch too system mode (program/process needing a system level service), a special CPU instruction is  executed called a **System call**

#### Unix
- Invented by D. Ritchie and K. Thompson at Bell Lab, USA in 1969
- Hundreds of different types/clones of UNIX systems, e.g [[Linux]]

---
## [[File system]]
- Stores **Persistent** data, that doesn't disappear when computer is turned off
	- Can be a connected disk drive or a network storage location
	- Disk drives can use different technologies (magnetic, solid state, electricity)
- Raw storage isn't convenient/easy to use, so a file system with directories is used to structure files.
- Names and structure of file system are called the **Name space**
- Each specific file will have its own path name
	- Path to follow through directories in name space to find the file
- 