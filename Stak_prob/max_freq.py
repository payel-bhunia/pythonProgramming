class Solution:
    # @param A : list of list of integers
    # @return a list of integers
    def solve(self, A):
        hash_map = {}
        freq_stack = {}
        max_count = 0
        ans = []
        for i in A:
            if i[0] == 1:
                if i[1] in hash_map:
                    hash_map[i[1]] += 1
                else:
                    hash_map[i[1]] = 1
                val = hash_map[i[1]]
                max_count = max(max_count, val)

                if val not in freq_stack:
                    freq_stack[val] = []
                freq_stack[val].append(i[1])
                ans.append(-1)
            else:
                item = freq_stack[max_count][-1]
                ans.append(item)
                hash_map[item] -= 1
                freq_stack[max_count].pop()
                if hash_map[item] == 0:
                    del hash_map[item]
                if len(freq_stack[max_count]) == 0:
                    del freq_stack[max_count]
                    max_count -= 1

        return ans


if __name__ == "__main__":
    A = [
        [1, 5],
        [1, 7],
        [1, 5],
        [1, 7],
        [1, 4],
        [1, 5],
        [2, 0],
        [2, 0],
        [2, 0],
        [2, 0]]
    s = Solution()
    ans = s.solve(A)
    print(ans)
