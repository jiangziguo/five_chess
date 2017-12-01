"""
深度搜索算法:陪练版
"""
from numpy.ma import zeros
from game.search import Search


class DFS(Search):
    # 初始化棋盘大小
    def __init__(self, m, n):
        self.m = m
        self.n = n
        self.chess_board = zeros((m, n))

    def get_possible_next_state(self, current_state, index_x, index_y):

        for i in range(self.m):
            for j in range(self.n):
                pass

    # 逆时针旋转，四个危险状态
    def get_dangerous_state(self, current_state):
        for i in range(self.m):
            for j in range(self.n):
                if current_state[i][j] != -1:
                    continue
                # oxxxx_
                if j + 4 < self.n and j > 0 and current_state[i][j + 1] + current_state[i][j + 2] + current_state[i][
                            j + 3] == -4 and current_state[i][j + 4] == 0 and current_state[i][j - 1] == 1:
                    return current_state, i, j + 4
                # _xxxxo
                if j + 4 < self.n and j > 0 and current_state[i][j + 1] + current_state[i][j + 2] + current_state[i][
                            j + 3] == -4 and current_state[i][j + 4] == 0 and current_state[i][j - 1] == 1:
                    return current_state, i, j + 4

                # _xxxxo
                if j - 5 >= 0 and current_state[i][j - 1] + current_state[i][j - 2] + current_state[i][j - 3] + \
                        current_state[i][j - 4] == -4 and current_state[i][j - 5] == 0:
                    return current_state, i, j - 5
                # 第四象限：对角
                if i + 3 < self.m and j + 3 < self.n and current_state[i][j] + current_state[i + 1][j + 1] + \
                        current_state[i + 2][j + 2] + current_state[i + 3][j + 3] == -4:
                    return current_state, i, j, 2
                if i + 3 < self.m and current_state[i][j] + current_state[i + 1][j] + \
                        current_state[i + 2][j] + current_state[i + 3][j] == -4:
                    return current_state, i, j, 3
                if i + 3 < self.m and j - 3 >= 0 and current_state[i][j] + current_state[i + 1][j - 1] + \
                        current_state[i + 2][j - 2] + current_state[i + 3][j - 3] == -4:
                    return current_state, i, j, 4

    def get_score(self, current_state, index_x, index_y):
        score = 0
        # for i in range(self.m):
        #     for j in range(self.n):
        # pass

    # 获取100分的状态 -ooo--：四个方向，逆时针
    def get_100_state(self, current_state, index_x, index_y):
        # 第一种情况 -ooo--
        if index_y - 1 >= 0 and index_y + 4 < self.n and \
                        (current_state[index_x][index_y - 1] and current_state[index_x][index_y + 3] and
                             current_state[index_x][
                                     index_y + 4]) == 0 and current_state[index_x][index_y] + current_state[index_x][
                    index_y + 1] + current_state[index_x][index_y + 2] == 3:
            return current_state, 100, index_x, index_y + 3

            pass

    def get_next_state(self, index_x_new, index_y_new):
        pass
