-- Script:    maths-basic.hs
-- Desc:      Practicing basic knowledge of maths to learn Haskell
-- Author:    Fraser Dumayne
-- Created:   23/07/2015
---------------------------------------------

-- Decide if number is odd
oddNumber :: Int -> Bool
oddNumber n 
	| n `mod` 2 == 0 = False
	| otherwise = True

-- Decide if number is even
evenNumber :: Int -> Bool
evenNumber n 
	| n `mod` 2 == 0 = True
	| otherwise = False

-- Add numbers
addNumber :: [Int] -> Int
addNumber [] = 0
addNumber (x:xs) = x + addNumber xs

-- Double a number
doubleMe :: Int -> Int
doubleMe 0 = 0

-- Add numbers up to a given number
addNumberLimit :: Int -> Int 
addNumberLimit 0 = 0
addNumberLimit n = n + addNumberLimit (n-1)

-- Decide if remainder is 0 for any numbers
divideNumber :: Int -> Int -> Bool
divideNumber m n = rem m n == 0

-- Return the factorial for a number
factorial :: Int -> Int
factorial 0 = 1
factorial n = n * factorial (n-1)

-- Find item in a list
listSearch :: (Eq a) => a -> [a] -> a
listSearch x [] = error "Item not found"
listSearch x (y:ys)
	| x == y = y
	| otherwise = listSearch x ys
	
-- Return length of a list
listLength :: [a] -> Int
listLength [] = 0
listLength (x:xs) = listLength xs + 1

-- Return unique elements of a list
listUnique :: (Eq a) => [a] -> [a]
listUnique [] = []
listUnique (x:xs) | x `elem` xs	= listUnique xs
				  | otherwise = x : listUnique xs	

-- Sort a list in ascending order
listSort :: (Ord a) => [a] -> [a]
listSort [] = []
listSort (x:xs) = (lessThan xs) ++ [x] ++ greaterThan (xs)
	where lessThan xs = listSort (filter (<x) xs)
	      greaterThan xs = listSort (filter (>=x) xs)
		  