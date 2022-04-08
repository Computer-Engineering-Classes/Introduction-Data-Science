import random
import re
import string
import time

def double_char(s: str) -> str:
    str = ""
    for c in s:
        str += 2 * c
    return str

def count_hi(str: str) -> int:
    return str.count("hi")

def cat_dog(str: str) -> bool:
    return str.count("cat") == str.count("dog")

#without re
def count_code(str: str) -> int:
    count = 0
    for i in range(len(str) - 3):
        if str[i : i + 2] == "co" and str[i + 3] == "e":
            count += 1
    return count

def count_code_re(str: str) -> int:
    regex = re.compile("co.e")
    return len(regex.findall(str))

def end_other(a: str, b: str) -> bool:
    a, b = a.lower(), b.lower()
    return a.endswith(b) or b.endswith(a)

def xyz_there(str: str) -> bool:
    return str.count("xyz") > str.count(".xyz")

if __name__ == "__main__":
    letters = string.ascii_lowercase
    s = ''.join(random.choice(letters) for _ in range(1000))

    start = time.perf_counter()
    print(count_code(s))
    print(f"Time elapsed (without RE module): {time.perf_counter() - start}s")

    start = time.perf_counter()
    print(count_code_re(s))
    print(f"Time elapsed (with RE module): {time.perf_counter() - start}s")
    pass