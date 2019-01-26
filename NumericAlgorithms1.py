def AND(a, b):
        """
        return a single character '0' or '1' representing 
        the logical AND  of bit a and bit b (whic are each '0' or '1')
        pytest --doctest-module (for running the doctests below)
        >>> AND('0', '1')
        '0'
        >>> AND('1', '1')
        '1'
        """

        if ( a == '1' and b == '1' ):
                return '1'        
        return '0'

def OR(a,b):
        if( a == '1' or b == '1' ):
                return '1'
        return '0'

def XOR(a,b):
        if( a == b ):
                return '0'
        return '1'

#Reverse the string for printing
def REVERSE(a):
        return a[::-1]

#Function that takes in 2 one-bit numbers and returns a two
#bit number that is the sum of the two
def PLUS2(a,b):
        sum = XOR(a,b)
        carry = AND(a,b)
        return sum + carry

#Fucntion that takes in 3 one-bit numbers and returns a two bit sum of the three
def PLUS(a,b,c = '0'):
        sum = PLUS2(a,b)
        if(c == '0'):
                return sum
        if sum == '00':
                return '10'
        elif sum == '10':
                return '01'
        else: 
                return '11'

#Find the sum of a binary number of any length
def SUM(a,b):        
        maxAnswerLength = max(len(a), len(b)) + 1
        a = padWithZeroes(REVERSE(a), maxAnswerLength)
        b = padWithZeroes(REVERSE(b), maxAnswerLength)
        print(a,b)

        answerStr = []*maxAnswerLength
        i = 0
        carry = '0'
        while(i < maxAnswerLength-1):
                sum = PLUS(a[i], b[i], carry)
                answerStr.append(sum[0])
                carry = sum[1]
                i+=1
        answerStr.append(carry)
        return ''.join(answerStr)

def padWithZeroes(str, length):
        zeroes = '0' * (length - len(str))
        return str + zeroes

def test_and():
        assert AND('0','0') == '0'
        assert AND('0','1') == '0'
        assert AND('1','0') == '0'
        assert AND('1','1') == '1'

def test_or():
        assert OR('0','0') == '0'
        assert OR('0','1') == '1'
        assert OR('1','0') == '1'
        assert OR('1','1') == '1'

def test_xor():
        assert XOR('0','0') == '0'
        assert XOR('0','1') == '1'
        assert XOR('1','0') == '1'
        assert XOR('1','1') == '0'

def test_plus2():
        assert REVERSE(PLUS2('0','0')) == '00'
        assert REVERSE(PLUS2('0','1')) == '01'
        assert REVERSE(PLUS2('1','0')) == '01'
        assert REVERSE(PLUS2('1','1')) == '10'

def test_plus3():
        assert REVERSE(PLUS('0','0','0')) == '00'
        assert REVERSE(PLUS('0','0','1')) == '01'
        assert REVERSE(PLUS('0','1','0')) == '01'
        assert REVERSE(PLUS('0','1','1')) == '10'
        assert REVERSE(PLUS('1','0','0')) == '01'
        assert REVERSE(PLUS('1','0','1')) == '10'
        assert REVERSE(PLUS('1','1','0')) == '10'
        assert REVERSE(PLUS('1','1','1')) == '11'
        #with default argument
        assert REVERSE(PLUS('0','0')) == '00'
        assert REVERSE(PLUS('0','1')) == '01'
        assert REVERSE(PLUS('1','0')) == '01'
        assert REVERSE(PLUS('1','1')) == '10'

def test_sum():
        assert REVERSE(SUM('01','01')) == '010'
        assert REVERSE(SUM('100','1')) == '0101'
        assert REVERSE(SUM('110101010', '1011')) == '0110110101'
        assert REVERSE(SUM('110101010','11011010110110011')) == '011011011101011101'


def test_padWithZeroes():
        assert padWithZeroes('1', 4) == '1000'

print(REVERSE(SUM('10','1')))
