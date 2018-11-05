# snake
The classic game of snake coded in steps using python.

The folder "manual" contains the following files

1. blocks
2. cherry_and_small_snake
3. cherry_snake
4. average_wins

These represent the three broad steps I took to *manually* code the system to play a game of snake (as in cherry_snake). What this means is that the system is **not** intelligent and will just follow the commands given to it to get to the cherry. How to get to the cherry etc has been "hard-coded".

Now, of course, no system is truly intelligent, but this one does not learn from its mistakes or anything like that either. Think of a calculator giving you "4" every time you ask it "2 + 2". If you change the meaning of "+" to mean "%" and try to teach the calculator that by saying "no, 2 + 2 = 0", it is useless. So is this program.

Additionally, the code is very basic - it just calculates the distance to the cherry and then moves the snake in that direction. Which means it dies easily, and often. At some point I will get around to programming a better manual version.

The file average_wins will give you the average wins of this snake over any number of iterations.

The second folder "automated" will contain an artifically intelligent version of this snake. Let us see how many iterations it takes before its intelligence surpasses hard coding.

Anyway, that's the idea, folks.
