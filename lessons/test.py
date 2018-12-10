
str = b'ok\ntest 0.5 1\ntest 0.4 2\nload 301 3\n\n'
answer = (str.decode()[3::]).split() # Получился список

print(answer)

ans_dict = dict()

# for key in answer[::3]:
for i, key in enumerate(answer[::3]):
    if key in ans_dict:
        ans_dict[key].append(tuple([answer[i*3+1], answer[i*3+2]]))
    else:
        ans_dict.update({key: [tuple([answer[i*3+1], answer[i*3+2]])]})

print(ans_dict)

