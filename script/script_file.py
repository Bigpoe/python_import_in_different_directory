import os
import sys

## Get location of this file ##
script_dir = os.path.dirname( __file__ )
print(f'script directory {script_dir}')

## Get directory from /module1/ folder ##
module1_dir = os.path.join( script_dir, '..', 'module1' )
print(f'look for mmodule {module1_dir}')

## Get directory from /module1/subdir1/ folder ##
mymodule_dir = os.path.join( script_dir, '..', 'module1', 'submodule1' )
print(f'look for mmodule {mymodule_dir}')

## Get directory from /module2/ folder ##
module2_dir = os.path.join( script_dir, '..', 'module2' )
print(f'look for mmodule {module2_dir}')

## Append location of /module1/ to the PATH ##
sys.path.append(module1_dir)

## Append location of /module1/subdir1/ to the PATH ##
sys.path.append(mymodule_dir)

## Append location of /module2/ to the PATH ##
sys.path.append(module2_dir)


## import modules outside the script directory ##
import module1_script1
import module1_script2
import submodule1_script1
from module2_script1 import Module2Script1Class1


## Execute fuctions from imported modules ##
submodule1_script1.submodule1_script1_function()
module1_script1.module1_script1_function()
module1_script2.module1_script2_function()
docule2_class = Module2Script1Class1()
docule2_class.module2_script1_function()

## Print each location in the sys.path where python looks for modules ##
for item in sys.path:
    print( item )
