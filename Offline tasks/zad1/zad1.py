#Jakub Konopka
#W algorytmie przechodzę po kolei po literach słowa s, za środek potencjalnego palindromu uznaję s[i], sprawdzam po kolei w lewo i w prawo czy litery występują symetrycznie aż wyszedłbym za tablicę lub 
#gdyby słowo przestało być palindromem. Wtedy porównuję jego długość z maksymalną dotychczas długością. W ten sposób po wykonaniu się głównej pętli pod zmienną maxlen znajduje się długość najdłuższego palindromu.
#Złożoność obliczeniowa: O(n^2)

from zad1testy import runtests

"""
def ceasar( s ):
    n = len(s)
    if n == 0:
        return 0
    
    maxlen = 1
    
    for i in range(n):
        currlen = 1
        left = i - 1
        right = i + 1

        while left >= 0 and right < n:
            if s[left] == s[right]:
                currlen += 2

            else:
                break

            left -= 1
            right += 1
        
        if currlen > maxlen:
            maxlen = currlen

    return maxlen
"""


# Python program to implement Manacher's Algorithm

def findLongestPalindromicString(text):
    N = len(text)
    if N == 0:
        return 0
	
    N = 2*N+1 # Position count
    L = [0] * N
    L[0] = 0
    L[1] = 1
    C = 1
    R = 2
    i = 0
    iMirror = 0
    maxLPSLength = 0
    diff = -1
	
    for i in range(2,N):	
		# get currentLeftPosition iMirror for currentRightPosition i
        iMirror = 2*C-i
        L[i] = 0
        diff = R - i
		# If currentRightPosition i is within centerRightPosition R
        if diff > 0:
            L[i] = min(L[iMirror], diff)

		# Attempt to expand palindrome centered at currentRightPosition i
		# Here for odd positions, we compare characters and
		# if match then increment LPS Length by ONE
		# If even position, we just increment LPS by ONE without
		# any character comparison
        try:
            while ((i+L[i]) < N and (i-L[i]) > 0) and (((i+L[i]+1) % 2 == 0) or (text[(i+L[i]+1)//2] == text[(i-L[i]-1)//2])):
                L[i]+=1
				
        except Exception as e:
            pass

        if L[i] > maxLPSLength and L[i]%2 == 1:	 # Track maxLPSLength
            maxLPSLength = L[i]

		# If palindrome centered at currentRightPosition i
		# expand beyond centerRightPosition R,
		# adjust centerPosition C based on expanded palindrome.
        if i + L[i] > R:
            C = i
            R = i + L[i]

    return maxLPSLength


#zmien all_tests na True zeby uruchomic wszystkie testy
#runtests( ceasar , all_tests = True )

runtests( findLongestPalindromicString , all_tests = True )