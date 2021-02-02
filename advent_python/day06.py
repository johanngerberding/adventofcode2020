INPUT = ["abc", "", "a", "b", "c", "", "ab", "ac", "", "a", "a", "a", "a", "", "b"]

def count(answers: list) -> int:
    count = 0
    group = ""
    for answer in answers:
        if answer != "":
            group += answer
        elif answer == "":
            count += len(set(group))
            group = ""
    
    if answers[-1] != "":
        return (count + len(set(group)))
    return count

assert count(INPUT) == 11

def count_2(answers: list) -> int:
    count = 0
    groups = []
    group = []
    for answer in answers:
        if answer != "":
            group.append(set(answer))
        elif answer == "":
            if len(group) == 1:
                count += len(group[0])
                group = []
            elif len(group) > 1:
                result = group[0]
                for i in range(1, len(group)):
                    result = result.intersection(group[i])
                count += len(result)
                group = []
    
    if answers[-1] != "":
        if len(group) == 1:
            count += len(group[0])
        elif len(group) > 1:
            result = group[0]
            for i in range(1, len(group)):
                result = result.intersection(group[i])
            count += len(result)

    return count

assert count_2(INPUT) == 6

with open('../inputs/day06.txt') as f:
    data = [l.strip() for l in f]
    print(count_2(data))
    