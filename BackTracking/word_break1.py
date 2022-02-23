from sys import stdin, setrecursionlimit

setrecursionlimit(10 ** 7)


def gen_line(s, dic, size, start, end, curr, ans):
    if start == end and end == len(s):
        #print(curr)
        ans.append(curr)
        return
    if start > len(s) or end > len(s):
        return
    # base
    if end - start + 1 <= size:
        if s[start:end + 1] not in dic:
            gen_line(s, dic, size, start, end + 1, curr, ans)
        else:
            curr.append(s[start:end + 1])
            gen_line(s, dic, size, end+1, end+1, curr.copy(), ans)
            curr.pop()
            gen_line(s, dic, size, start, end + 1, curr, ans)
    else:
        return


def getAllValidSentences(sentence, dic, size):
    start = 0
    n = len(sentence)
    end = 0
    curr = []
    ans = []
    gen_line(sentence, dic, size, start, end, curr, ans)
    printAnswer(ans)


#   taking inpit using fast I/O
def takeInput():
    n = int(input().strip())
    dictionary = [stdin.readline().strip() for i in range(n)]
    sentence = stdin.readline().strip()

    return sentence, dictionary


def printAnswer(ans):
    for sentence in ans:
        print(' '.join(sentence))


#   main
sentence, dictionary = ['godisnowherenowhere',['god','is','now','no','where','here']]
dic = set(dictionary)
size = 0
for i in dic:
    size = max(size, len(i))
getAllValidSentences(sentence, dic, size)
#printAnswer(ans)
