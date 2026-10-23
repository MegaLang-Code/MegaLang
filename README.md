## Run MegaLang
download the .exe file I recommend the latest version.
Then make a .MEGA file or if on an older version of windows use a .MLS (MegaLang Syntax) Made the name for syntax, but it has a use now.
I got support for Linux to run it after download:
```
chmod +x MegaLang

./MegaLang
```
.

## Syntax
here is some syntax for you to study
I made it so quotes are not needed. Don't ask how or why

``` MegaLang
# 1. VARIABLE MANIPULATION
MakeVar PlayerName, Alex
MakeVar HighScore, 2500
SetExistVar HighScore, 3000
DelVar PlayerName

# 2. INPUT & OUTPUT (I/O)
Speek HighScore
Speek Loading assets...
Ask Press Enter to boot the system...
MakeVar UserResponse, empty
AskInputToVar Enter your team color:, UserResponse

# 3. MATHEMATICAL OPERATIONS
ADD HighScore, 500
SUB 100, 25
MULTI HighScore, 2
DIV 100, 4

# 4. CONDITIONAL LOGIC BLOCKS
MakeVar IsAdmin, TRUE
If IsAdmin
    Speek Access granted.
CheckElse
    Speek Access denied.
EndIf

# 5. NETWORKING & WEB UTILITIES
StartServerDev 8000
StartServerProduct 8080

# 6. ENGINE MEMORY CONFIGURATION
AutoVarClean Off
VarMemClean
```

DON'T DO EVIL (check the bottom of the licence)
and NO malware of course. (I don't think in it's state is possible)
(I lost 1.0) At least we have the 1.0 exe.
If you have suggestions you have to submit a pull request. (Fork it then submit a pull request once you make your changes, and I'll try to get linux support.) I have V1.6 (added REPL)

