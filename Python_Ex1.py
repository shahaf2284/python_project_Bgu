import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--task", dest="task", help="The function is for Vowels")
parser.add_argument("--arg", dest="arg", help="The value appropriate for perfect or lazy")
args = parser.parse_args()

def count_vowels(string:str)->int:
    vowels = "YOIAEU"
    count = 0
    for i in string:
        if i.upper() in vowels:
            count += 1
        else:
            pass
    return count

def perfect_power(Index_Number:int)->int:
    perfect = []
    index = 1
    list2 = []
    while len(perfect) <= Index_Number:
        for i in range(1, int(index ** 0.5) + 1):
            if not index % i:
                list2.append(i)
        for x in list2:
            for j in range(0, index // 2 + 1):
                if x ** j == index:
                    if index not in perfect:
                        perfect.append(index)

        index += 1
    return perfect[Index_Number - 1]

def lazy(IndexLazyNumber : int)-> int:
    return int(((IndexLazyNumber-1)**2 + (IndexLazyNumber-1) + 2)/2)

if args.task == "vowels":
    print(count_vowels(args.arg))
elif args.task =="perfect":
    print(perfect_power(int(args.arg)))
elif args.task =="lazy":
    print(lazy(int(args.arg)))
else:
    print("wrong input")