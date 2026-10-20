## Syntax
here is some syntax for you to study
I made it so quotes are not needed. Don't ask how
``` MegaLang
# Create some initial test variables
MakeVar my_number, 500
MakeVar delete_me_target, Temporary Data

# Print the starting conditions
Speek Running initial value check:
Speek my_number

# Let's perform calculation tests
Speek Adding values together:
ADD my_number, 100

# Test manual variable cleanup via DelVar
Speek Now clearing out the temporary data variable...
DelVar delete_me_target

# Running an operational safety test 
# This should trigger your new error message since the key is gone!
DelVar delete_me_target

# Test that system constants remain fully protected
DelVar TRUE

# Test memory optimizations block syntax
AutoVarClean Off
VarMemClean
AutoVarClean On

Speek Code executed completely and safely!

StartServer 9450
```

DON'T DO EVIL (check the bottom of the licence)
and NO malware of course. (I don't think in it's state is possible)
(I lost 1.0) At least we have the 1.0 exe.
