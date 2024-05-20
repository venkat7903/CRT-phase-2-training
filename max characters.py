# S = sorted(input())
# max_count = 0
# max_str = ''
# for i in S:
#     count = S.count(i)
#     if max_count < count:
#         max_count = count
#         max_str = i
# print(max_str, max_count)

S = input().lower()
max_count = 0
max_str = S[0]
char_dict = dict()
for i in S:
    if i in char_dict:
        char_dict[i] += 1
    else:
        char_dict[i] = 1
    if char_dict[i] >= max_count:
        if max_str == "" or ord(max_str) >= ord(i):
            max_str = i
            print(max_str)
            max_count = char_dict[i]
       
print(max_count, max_str)