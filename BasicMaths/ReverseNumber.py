def reverse(x):
        MAX_INT = 2**31 - 1
        MIN_INT = -2**31

        revN = 0
        sign = 1 if x > 0 else -1
        x = abs(x)

        while x != 0:
                lastDigit = x % 10
                x = x // 10
                revN = revN * 10 + lastDigit

                # early exit if overflow is detected
                if revN > MAX_INT:
                        return 0
                
        revN *= sign

        if revN < MIN_INT or revN > MAX_INT:
            return 0
        
        return revN

print(reverse(7985))