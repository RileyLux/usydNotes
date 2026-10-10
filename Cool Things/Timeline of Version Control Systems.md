## The Evolution of Version Control Systems
The history of Version Control Systems (VCS) is divided into **three distinct generations**. Over time, the technology shifted from tracking single local files to managing global, decentralized codebases.

## 🛠️ 1st Generation: Local & File-Centric (1972 – 1980s)
Systems in this era operated locally on a single machine. Collaboration was managed through strict **file locking**, meaning if one person was editing a file, no one else could access it.

- **1972 – SCCS (Source Code Control System):**
    - Developed at Bell Labs.
    - The first widely used version control system.
    - Tracked modifications to individual text files line-by-line.
- **1982 – RCS (Revision Control System):**
    - An open-source alternative to SCCS.
    - Pioneered "reverse deltas" (storing only the newest version and a history of past edits).
    - Significantly improved system speed and saved disk space.

## 🌐 2nd Generation: Centralized & Client-Server (1986 – 2000s)
These systems introduced networks and central servers. Instead of locking files entirely, multiple developers could edit files simultaneously and **merge** their changes together later.

- **1986 – CVS (Concurrent Versions System):**
    - Built on top of RCS mechanics.
    - Allowed multiple developers to collaborate over a network connection.
    - Lacked "atomic commits," meaning network failures mid-upload corrupted the codebase.
- **2000 – SVN (Apache Subversion):**
    - Created to fix the prominent structural bugs of CVS.
    - Introduced atomic commits (all file changes succeed or fail as a single unit).
    - Tracked entire directory trees rather than isolated files, becoming the industry standard for a decade.

## 💻 3rd Generation: Distributed (2005 – Present)
Distributed systems eliminated the reliance on a single central server. Every developer clones a **full copy of the entire repository**, including its complete historical timeline, directly onto their local machine.

- **2005 – Git:**
    - Created by Linus Torvalds for Linux kernel development.
    - Designed out of necessity after proprietary tool BitKeeper revoked the team's free license.
    - Made branching, history tracking, and merging incredibly fast and lightweight.
- **2005 – Mercurial:**
    - Launched almost simultaneously with Git to solve the same distributed collaboration problem.
    - Offered comparable features with a flatter, arguably easier learning curve.
    - Ultimately lost the adoption race to Git, a shift heavily accelerated by the launch of GitHub in 2008.