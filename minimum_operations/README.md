# Minimum Operations

## Requirements

### General
- Allowed editors: `vi`, `vim`, `emacs`
- All your files will be interpreted/compiled on Ubuntu 14.04 LTS using `python3` (version 3.4.3)
- All your files should end with a new line
- The first line of all your files should be exactly `#!/usr/bin/python3`
- A `README.md` file, at the root of the folder of the project, is mandatory
- Your code should be documented
- Your code should use the **PEP 8** style (version 1.7.x)
- All your files must be executable

## Tasks

### 0. Minimum Operations

**Mandatory**

In a text file, there is a single character `H`. Your text editor can execute only two operations in this file: **Copy All** and **Paste**. Given a number `n`, write a method that calculates the fewest number of operations needed to result in exactly `n` `H` characters in the file. Be smart about how you utilize the memory!

- **Prototype:** `def minOperations(n)`
- **Returns:** An integer
- If `n` is impossible to achieve, return `0`

#### Example:

For `n = 9`: