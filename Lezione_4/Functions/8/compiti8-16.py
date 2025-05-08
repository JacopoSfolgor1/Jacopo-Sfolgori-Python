'''8-16. Imports: Using a program you wrote that has one function in it, store that function in a separate file. 
Import the function into your main program file, and call the function using each of these approaches:
import module_name
from module_name import function_name
from module_name import function_name as fn
import module_name as mn
from module_name import *'''

import functionfor815
functionfor815.show_messages(["Ciao","funziona","per","favore"]) 

from functionfor815 import show_messages 
show_messages(["Ciao","funziona","per","favore"])

from functionfor815 import show_messages as fn 
fn(["Ciao","funziona","per","favore"])

import functionfor815 as mn
mn.show_messages(["Ciao","funziona","per","favore"])

from functionfor815 import *
show_messages(["Ciao","funziona","per","favore"])







