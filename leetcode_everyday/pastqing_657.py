# coding:utf8

class Solution:
    dirs = {
        'U' : (-1, 0),
        'D' : (1, 0),
        'L' : (0, -1),
        'R' : (0, 1)

    }

    def judgeCircle(self, moves: str) -> bool:
        if not moves:
            return True
        res = self.helper(0, moves, 0, 0, len(moves))
        return res
    
    def helper(self, start, moves, rowIdx, colIdx, size):
        if start >= len(moves):
            if rowIdx == 0 and colIdx == 0:
                return True
            return False

        res = False	
        dx, dy = Solution.dirs.get(moves[start])
        res = self.helper(start + 1, moves ,rowIdx + dx, colIdx + dy, size)

        return res


if __name__ == '__main__':
    obj = Solution()
    moves = 'UD'
    res = obj.judgeCircle(moves)
    print(res)
