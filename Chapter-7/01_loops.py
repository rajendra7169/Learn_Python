"""
Types of Loops in Python:

1. for Loop:  
   Used to iterate over a sequence such as a list, tuple, string, or range. It executes the block of code for each element in the sequence.

2. while Loop:  
   Executes a block of code repeatedly as long as the specified condition is True. The loop stops when the condition becomes False.

3. Nested Loops:  
   A loop inside another loop. The inner loop completes all its iterations for each iteration of the outer loop.

4. else with Loops:  
   An optional else block can be used with for and while loops. It executes when the loop finishes normally (i.e., not interrupted by a break statement).

Control Statements:
- break: Immediately exits the loop, skipping all remaining iterations.  
- continue: Skips the rest of the current iteration and proceeds to the next iteration of the loop.  
- pass: A placeholder that performs no operation, used when a block of code is syntactically required but you don’t want any action.
"""

"""print(1)
print(2)
print(3)
print(4)
print(5)"""

# The same task can be done like this:

for i in range(1, 11):
    print(i)
