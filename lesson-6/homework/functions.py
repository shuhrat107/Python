def uncommon_elements(list1, list2):

    set1 = set(list1)
    set2 = set(list2)
    

    uncommon_in_list1 = [x for x in list1 if x not in set2]
    uncommon_in_list2 = [x for x in list2 if x not in set1]

    return uncommon_in_list1 + uncommon_in_list2


def insert_underscore(txt):
    vowels = "aeiouAEIOU"
    result = []
    count = 0  

    for i, char in enumerate(txt):
        result.append(char)
        count += 1

        if count == 3 and i != len(txt) - 1:  
            if char in vowels or (i > 0 and result[-2] == '_'):
                continue  
            else:
                result.append('_')
                count = 0  

    return ''.join(result)
