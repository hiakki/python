# this decorator function, takes 'whole function and its arguments' as its own argument
def check_invalid(func):
    def check(x,y):
        if y != 0:
            return func(x,y)
    return check

@check_invalid
def kuch_bhi_divide(x,y):
    print(x/y)

kuch_bhi_divide(1,2)


# Flow of this program -
# 1. from line 12 -> kuch_bhi_divide
# 2. from line 8 -> check_invalid (likha bhale hi function k upar ho, but it is kind of 1st step inside this function - kuch_bhi_divide)
# 3. from line 6 -> check
# 4. from line 5 (if cond is true) -> now literally goes under function kuch_bhi_divide and prints output