import re

ret1 = re.match(r"test[0-9a-zA-Z]", "testZ")
ret2 = re.match(r"test\d", "test1")
ret3 = re.match(r"test\s", "test    ")
ret4 = re.match(r"test\w", "test_")

ret22 = re.match(r"test\D", "test ")
ret33 = re.match(r"test\S", "test1")
ret44 = re.match(r"test\W", "test=")

print(ret1.group())
print(ret2.group())
print(ret3.group())
print(ret4.group())
print(ret22.group())
print(ret33.group())
print(ret44.group())