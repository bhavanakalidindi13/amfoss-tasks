##Problem Faced
In this task the problem that i faced was that the code was working in my computer but when i run it on the website i got EOF error.
I also got a runtime error -'NZEC' which is 'non zero exit code'.

## Solution
I searched in google and found out that the input given in the website was ending with '\eof',therefore it was creating an error.
So, I used sys.stdin.readline for input and the error was resolved.
For NZEC error i found that the input which was given was null. Therefore, adding if statement to verify whether the input was null or not clarified that error.

## What i learned?
I learned how to search in google for errors.
As i encountered errors which i never did before i learned new things through it. 