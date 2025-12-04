# Cisc121 Algorithm Visualization Project
## Step 1 - Algorithm Chose: Bubble Sort

I ended up choosing bubble sort because overall it is the easiest and simplest to impliment. It is also much more effective for visual representation then linear. The problem which will be solved is arranging values from smallest to largest, which as is known bubble sort, sorts it that way but comparing neighboring elements until the list is fully sorted. 

Bubble Sort works really well with small datasets which makes it a great leanring tool. 

This is the reason why bubble sort is the best solution for this situation. 


## Step 2 - My Plan using Computational Thinking 

### Decomposition
Smaller steps that are forming my algorithm
1. Comparing neigboring elements in a list
2. If order is correct keep same, if not, swap them. 
3. Move to next pair and repeat, and keep going over the list until it is fully sorted. 

### Pattern Recognition 
How does my Algorithm compare and swap values
1. Every pair of elements is checked
2. The largest unsorted number will "bubble up," to the end of the list after each and every pass
3. This will continue until no more swaps are needed. 

### Abstraction 
Details that will be simplified for the user
What they won't see:
1. Index changes and loop logic
2. Temporary values
What they will see:
3. List becoming more sorted after each individual step
4. Swapping values when out of order

### Algorithim Design
How input -> processing -> output will flow. 
1. Input: Will be an unsorted list of numbers
2. Processing: Comparing and swapping elements if needed. 
3. Output: Sorted list, from smallest to largest


## Step 3 & 4 (Purely code for the app so not in this section)


## Step 5 

### Testing and Verifying 
I did 5 different tests (edge cases and normal tests) just to make sure my app works properly
Test 1: 
Input: 20, 210, 21, 67, 45, 98, 987
Expected outcome: 20, 21, 45, 67, 98, 210, 987
The expected outcome was the exact same as the actual outcome we got as seen in the screenshot below:
![Test 1 output](<Screenshot 2025-12-03 at 9.01.07 PM.png>)

Test 2:
Input: a, b, c 
Expected outcome: Error message (The one I wrote in my code)
The outcome that was expected, was what was shown as well, "This is a error, please enter whole numbers no decimals," as seen in this screenshot below:
![Test 2 Output](<Screenshot 2025-12-03 at 9.04.42 PM.png>)

Test 3:
Input: 4
Expected outcome: 4
Again with this input the expected code was the correct code that was displayed in my app as seen in the screenshot below:
![Test 3 Output](<Screenshot 2025-12-03 at 9.06.05 PM.png>)

Test 4: 
Input: -4, -12, 12, 4 
Expected outcome: -12, -4, 4, 12
Again with this test I expected the code to sort the nunmbers from lowest to highest and that is what happened in the screenshot below:
![Test 4 Output](<Screenshot 2025-12-03 at 9.07.55 PM.png>)

Test 5:
Input: 1, 2, 3, 4, 5
Expected outcome: 1, 2, 3, 4, 5
For this code I expect the list to not change as it is already sorted and that is what I got, as seen in the screenshot below:
![Test 5 Output](<Screenshot 2025-12-03 at 9.09.28 PM.png>)

Note:
Overall I tested some edge cases like using one number or negatives in certain examples, as well as using letters. And my app responded accordingly for all these tests. So overall all my tests worked and it was successful. 
