import re

# For converting String to List(Array)

some_var = """            bac-p-farmiso-relay           farmiso-relay         Deployment/farmiso-relay         0%/50%    3  9
3
26d        """

def string_to_list(a):
    c = 'farmiso'

    print(a)

    # This command will only remove spaces from beginning and end of the string (this is not required if you are using re.sub())
    # a = a.strip()

    print(a)


    # This will replace all multi-spaces from a into single space
    a = re.sub(r"\s+", " ", a)

    # Regex can't be handled by replace()
    # a = a.replace(r"\s+", '')

    print(a)

    b = a.split(" ")

    # If we want to explicitly check for any string and then perform any action on it
    if "farmiso" in c:
        e = c.replace('farmiso', 'meesho')


    print(type(b))

    print(b)

    print(e)


def multi_dimension_array_handling():
    # For handling multidimensional arrays

    d = [ 'abcd', [ 'xyz', 'pqr', 'lmn', "abc" ]]

    for f in d[1]:
        if f in d[0]:
            print(f)



if __name__ == '__main__':
    string_to_list(some_var)
    multi_dimension_array_handling()