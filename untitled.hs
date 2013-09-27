pythagTriple [] = []
pythagTriple (x:xs) =   [(x,b,c) | b<-xs,c<-xs, x < b, b < c, (findPos xs b) < (findPos xs c)] : pythagTriple xs

removeDupe [] = []
removeDupe (x:xs)
	| elem x xs = removeDupe xs
	| otherwise = x:removeDupe xs
 
findPos list elt = map fst $ filter ((elt==).snd) $ zip [0..] list

flatten [] = []
flatten (x:xs) = x++ flatten xs

--main = print (pythagTriple [1, 1, 2, 2, 3, 4])
main = print  (length (removeDupe (flatten (pythagTriple [1, 1, 5, 4, 3, 6, 6, 5, 9, 10]))))