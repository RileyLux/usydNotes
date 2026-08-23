---
tags:
  - Unix
  - Shell
---
### Files/Directories

| **cd**    | Change directory        |
| ----- | ----------------------- |
| **mkdir** | Make directory          |
| **ls**    | List directory contents |
| **rmdir** | Remove directory        |
| **rm**    | Remove                  |
| **mv**    | Move/Rename             |
| **cp**    | Copy                    |
| **pwd**   | Print working directory |


### Name space

| **..** | Parent Directory   | *cd ..*     |
| ------ | ------------------ | ----------- |
| **.**  | Current Directory  | *./program* |
| **-**  | Previous Directory | *cd -*      |
| **~**  | Home Directory     | *cd ~*      |
| **/**  | Root Directory     | *cd /*      |

### Symbols

| $?      | Holds status code of last executed command                                        |                |
| ------- | --------------------------------------------------------------------------------- | -------------- |
| \\      | Treats special symbols as text characters instead of unix commands                | \\\\, \\$, \\' |
| \`...\` | Placing command in back quotes means replace command with output of inner command |                |
| >       | Redirect output of command to new file                                            |                |
| >>      | Redirect output of command to new file (append if file already exists)            |                |
| \|      | sends output of one command as input to another                                   |                |


---

| **cat** | retrieve/display contents of file                                                  | cat ./hello.txt |
| ------- | ---------------------------------------------------------------------------------- | --------------- |
| echo    | prints arguments                                                                   | echo "hello"    |

