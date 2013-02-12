myLast x = x !! (length x - 1)

myButLast x = x !! (length x - 2)

element_at x k= x!!k

myLength [] = 0
myLength (x:xs) = 1+myLength xs

main = print (myReverse [1,2,4,3])
