import copy

import datetime
import numpy as np
from numpy import mat

from search_method_game.chess_type_judge import ChessTypeJudge

# 眠二
SLEEP_TWO = 0
# 活二
LIVE_TWO = 1
# 眠三
SLEEP_THREE = 2
# 活三
LIVE_THREE = 3
# 冲四
PUNCHING_FOUR = 4
# 活四
LIVE_FOUR = 5
# 连五
LINK_FIVE = 6
# 棋盘初始状态
INIT_STATE = [
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
]
# 棋盘的位置价值
POSITION_VALUE = [
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0],
    [0, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 1, 0],
    [0, 1, 2, 3, 3, 3, 3, 3, 3, 3, 3, 3, 2, 1, 0],
    [0, 1, 2, 3, 4, 4, 4, 4, 4, 4, 4, 3, 2, 1, 0],
    [0, 1, 2, 3, 4, 5, 5, 5, 5, 5, 4, 3, 2, 1, 0],
    [0, 1, 2, 3, 4, 5, 6, 6, 6, 5, 4, 3, 2, 1, 0],
    [0, 1, 2, 3, 4, 5, 6, 7, 6, 5, 4, 3, 2, 1, 0],
    [0, 1, 2, 3, 4, 5, 6, 6, 6, 5, 4, 3, 2, 1, 0],
    [0, 1, 2, 3, 4, 5, 5, 5, 5, 5, 4, 3, 2, 1, 0],
    [0, 1, 2, 3, 4, 4, 4, 4, 4, 4, 4, 3, 2, 1, 0],
    [0, 1, 2, 3, 3, 3, 3, 3, 3, 3, 3, 3, 2, 1, 0],
    [0, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 1, 0],
    [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
]

# 是否计算过
CALCULATED = {}


class Game:
    def __init__(self, init_state, chess_board_length, chess_board_width):
        self.init_state = init_state
        self.chess_board_length = chess_board_length
        self.chess_board_width = chess_board_width
        self.chess_type_num = 7

    def judge_change(self, state, index_x, index_y):
        key = (index_x, index_y, state[index_x][index_y])
        each_direction_chess = []
        if not CALCULATED.__contains__(key):
            for i in range(0, 8):
                each_direction_chess.append(self.get_each_direction_chess(state, index_x, index_y, i))
        if CALCULATED.__contains__(key):
            old_chess_type = CALCULATED[key]
            flag = True
            for i in range(0, 8):
                each_direction_chess.append(self.get_each_direction_chess(state, index_x, index_y, i))
                if flag and old_chess_type[i] != each_direction_chess[i]:
                    flag = False
            if flag:
                return old_chess_type[8]
        chess_type = self.get_one_chess_type(state, index_x, index_y, self.chess_board_length, self.chess_board_width)
        each_direction_chess.append(copy.deepcopy(chess_type))
        CALCULATED[key] = each_direction_chess
        return chess_type

    # 获取每一个方向的五颗棋子，从右水平方向开始，逆时针
    def get_each_direction_chess(self, state, index_x, index_y, direction):
        chess = []
        if direction == 0:
            num_y = index_y + 6 if index_y + 5 < self.chess_board_width else self.chess_board_width
            # if index_y + 5 > self.chess_board_width:
            #     num = self.chess_board_width
            for j in range(index_y + 1, num_y):
                chess.append(state[index_x][j])
            return chess
        if direction == 1:
            num_y = index_y + 6 if index_y + 5 < self.chess_board_width else self.chess_board_width
            i = 0
            for j in range(index_y + 1, num_y):
                i += 1
                if index_x - i >= 0:
                    chess.append(state[index_x - i][j])
            return chess
        if direction == 2:
            num_x = index_x - 5 if index_x - 5 >= 0 else 0
            for i in range(num_x, index_x):
                chess.append(state[i][index_y])
            return chess
        if direction == 3:
            num_x = index_x - 5 if index_x - 5 >= 0 else 0
            num_y = index_y - 5 if index_y - 5 >= 0 else 0
            j = 0
            for i in range(num_x, index_x):
                if num_y + j < index_y:
                    chess.append(state[i][num_y + j])
                j += 1
            return chess
        if direction == 4:
            num_x = index_x - 5 if index_x - 5 >= 0 else 0
            for i in range(num_x, index_x):
                chess.append(state[i][index_y])
            return chess
        if direction == 5:
            num_x = index_x + 6 if index_x + 5 < self.chess_board_length else self.chess_board_length
            # num_y = index_y - 5 if index_y - 5 >= 0 else 0
            j = 0
            for i in range(index_x + 1, num_x):
                j += 1
                if index_y - j >= 0:
                    chess.append(state[i][index_y - j])
            return chess
        if direction == 6:
            num_x = index_x + 6 if index_x + 5 < self.chess_board_length else self.chess_board_length
            for i in range(index_x + 1, num_x):
                chess.append(state[i][index_y])
            return chess
        if direction == 7:
            num_x = index_x + 6 if index_x + 5 < self.chess_board_length else self.chess_board_length
            num_y = index_y + 6 if index_y + 5 < self.chess_board_width else self.chess_board_width
            j = 0
            for i in range(index_x + 1, num_x):
                j += 1
                if index_y + j < num_y:
                    chess.append(state[i][index_y + j])
            return chess
    # 获取棋盘所有子的棋型
    def get_chess_type(self, current_state):
        chess_type_result = np.array([0 for row in range(self.chess_type_num)])
        for i in range(self.chess_board_length):
            for j in range(self.chess_board_width):
                new_chess_type = self.judge_change(current_state, i, j)
                chess_type_result += np.array(new_chess_type)
        return chess_type_result.tolist()

    # 获取棋盘一个子的棋型
    def get_one_chess_type(self, current_state, index_x, index_y, chess_board_length, chess_board_width):
        chess_type = []
        chess_type.append(
            ChessTypeJudge.sleep_two(current_state, index_x, index_y, chess_board_length, chess_board_width))
        chess_type.append(
            ChessTypeJudge.live_two(current_state, index_x, index_y, chess_board_length, chess_board_width))
        chess_type.append(
            ChessTypeJudge.sleep_three(current_state, index_x, index_y, chess_board_length, chess_board_width))
        # if ChessTypeJudge.live_three(current_state, index_x, index_y, chess_board_length, chess_board_width):
        #     print(current_state)
        chess_type.append(
            ChessTypeJudge.live_three(current_state, index_x, index_y, chess_board_length, chess_board_width))
        chess_type.append(
            ChessTypeJudge.punching_four(current_state, index_x, index_y, chess_board_length, chess_board_width))
        chess_type.append(
            ChessTypeJudge.live_four(current_state, index_x, index_y, chess_board_length, chess_board_width))
        chess_type.append(
            ChessTypeJudge.link_five(current_state, index_x, index_y, chess_board_length, chess_board_width))
        return chess_type

    # 搜索落子处以3为半径的圆内是否有棋子
    def get_children(self, state, who):
        children = []
        for i in range(self.chess_board_length):
            for j in range(self.chess_board_width):
                if state[i][j] != 0:
                    continue
                # if (j + 3 < self.chess_board_width and
                #         (state[i][j + 1] != 0 or state[i][j + 2] != 0 or state[i][j + 3] != 0)) or \
                #         (j + 3 < self.chess_board_width and i - 3 >= 0 and
                #              (state[i - 1][j + 1] != 0 or state[i - 2][j + 2] != 0 or state[i - 3][j + 3] != 0)) or \
                #         (i - 3 >= 0 and
                #              (state[i - 1][j] != 0 or state[i - 2][j] != 0 or state[i - 3][j] != 0)) or \
                #         (j - 3 >= 0 and i - 3 >= 0 and
                #              (state[i - 1][j - 1] != 0 or state[i - 2][j - 2] != 0 or state[i - 3][j - 3] != 0)) or \
                #         (j - 3 >= 0 and
                #              (state[i][j - 1] != 0 or state[i][j - 2] != 0 or state[i][j - 3] != 0)) or \
                #         (j - 3 >= 0 and i + 3 < self.chess_board_length and
                #              (state[i + 1][j - 1] != 0 or state[i + 2][j - 2] != 0 or state[i + 3][j - 3] != 0)) or \
                #         (i + 3 < self.chess_board_length and
                #              (state[i + 1][j] != 0 or state[i + 2][j] != 0 or state[i + 3][j] != 0)) or \
                #         (j + 3 < self.chess_board_width and i + 3 < self.chess_board_length and
                #              (state[i + 1][j + 1] != 0 or state[i + 2][j + 2] != 0 or state[i + 3][j + 3] != 0)):
                if ((j + 2 < self.chess_board_width and
                         (state[i][j + 1] != 0 or state[i][j + 2] != 0)) or \
                            (j + 2 < self.chess_board_width and i - 2 >= 0 and
                                 (state[i - 1][j + 1] != 0 or state[i - 2][j + 2] != 0)) or \
                            (i - 2 >= 0 and
                                 (state[i - 1][j] != 0 or state[i - 2][j] != 0)) or \
                            (j - 2 >= 0 and i - 2 >= 0 and
                                 (state[i - 1][j - 1] != 0 or state[i - 2][j - 2] != 0)) or \
                            (j - 2 >= 0 and
                                 (state[i][j - 1] != 0 or state[i][j - 2] != 0)) or \
                            (j - 2 >= 0 and i + 2 < self.chess_board_length and
                                 (state[i + 1][j - 1] != 0 or state[i + 2][j - 2] != 0)) or \
                            (i + 2 < self.chess_board_length and
                                 (state[i + 1][j] != 0 or state[i + 2][j] != 0)) or \
                            (j + 2 < self.chess_board_width and i + 2 < self.chess_board_length and
                                 (state[i + 1][j + 1] != 0 or state[i + 2][j + 2] != 0))):
                    child = copy.deepcopy(state)
                    child[i][j] = who
                    # child = copy.deepcopy(state)
                    # child[i][j] = type_value
                    children.append(child)
        return children

    def eval(self, state, who):
        myself = self.get_chess_type(copy.deepcopy(state))
        opponent = self.get_chess_type(np.array(copy.deepcopy(state)) * -1)
        # 必死棋型
        if who == 1:
            if myself[LINK_FIVE]:
                return 9999
            if opponent[LINK_FIVE]:
                return -9999
        else:
            if opponent[LINK_FIVE]:
                return -9999
            if myself[LINK_FIVE]:
                return 9999
        # 两个冲四等于一个活四
        if myself[PUNCHING_FOUR] > 1:
            myself[LIVE_FOUR] += 1
        if opponent[PUNCHING_FOUR] > 1:
            opponent[LIVE_FOUR] += 1

        myself_value = 0
        opponent_value = 0
        if who == 1:
            if myself[LIVE_FOUR] > 0:
                return 9990
            if myself[PUNCHING_FOUR] > 0:
                return 9980
            if opponent[LIVE_FOUR] > 0:
                return -9970
            if opponent[PUNCHING_FOUR] > 0 and opponent[LIVE_THREE] > 0:
                return -9960
            if myself[LIVE_THREE] and opponent[PUNCHING_FOUR] == 0:
                return 9950
            if opponent[LIVE_THREE] > 1 and myself[PUNCHING_FOUR] + myself[LIVE_THREE] + myself[SLEEP_THREE] == 0:
                return -9940
            if myself[LIVE_THREE] > 1:
                myself_value += 2000
            else:
                if myself[LIVE_THREE] > 0:
                    myself_value += 200
            if opponent[LIVE_THREE] > 1:
                opponent_value += 500
            else:
                if opponent[LIVE_THREE] > 0:
                    opponent_value += 100
            myself_value += (myself[SLEEP_THREE] * 10 + myself[LIVE_TWO] * 4 + myself[SLEEP_TWO])
            opponent_value += (opponent[SLEEP_THREE] * 10 + opponent[LIVE_TWO] * 4 + opponent[SLEEP_TWO])
            value = myself_value - opponent_value
        if who == -1:
            if opponent[LIVE_FOUR] > 0:
                return -9990
            if opponent[PUNCHING_FOUR] > 0 and opponent[LIVE_THREE] > 0:
                return -9980
            if myself[LIVE_FOUR] > 0:
                return 9970
            if myself[PUNCHING_FOUR] > 0:
                return 9960
            if opponent[LIVE_THREE] and myself[PUNCHING_FOUR] == 0:
                return -9950
            if myself[LIVE_THREE] > 1 and opponent[PUNCHING_FOUR] + opponent[LIVE_THREE] + opponent[SLEEP_THREE] == 0:
                return 9940
            if opponent[LIVE_THREE] > 1:
                opponent_value += 2000
            else:
                if opponent[LIVE_THREE] > 0:
                    opponent_value += 200
            if myself[LIVE_THREE] > 1:
                myself_value += 500
            else:
                if myself[LIVE_THREE] > 0:
                    myself_value += 100
            opponent_value += (opponent[SLEEP_THREE] * 10 + opponent[LIVE_TWO] * 4 + opponent[SLEEP_TWO])
            myself_value += (myself[SLEEP_THREE] * 10 + myself[LIVE_TWO] * 4 + myself[SLEEP_TWO])
            value = myself_value - opponent_value
        #
        #
        # if opponent[LINK_FIVE] > 0:
        #     return -9999
        # if myself[LINK_FIVE] > 0:
        #     return 9999
        # if who == 1 and (myself[PUNCHING_FOUR] + myself[LIVE_FOUR] > 0 or (
        #                     opponent[PUNCHING_FOUR] + opponent[LIVE_FOUR] == 0 and myself[LIVE_THREE] > 0)):
        #     return 9990
        # if who == -1 and (opponent[PUNCHING_FOUR] + opponent[LIVE_FOUR] > 0 or (
        #                     myself[PUNCHING_FOUR] + myself[LIVE_FOUR] == 0 and opponent[LIVE_THREE] > 0)):
        #     return -9990
        # if who == -1 and (myself[PUNCHING_FOUR] > 1 or myself[LIVE_FOUR] > 0) and opponent[PUNCHING_FOUR] + opponent[
        #     LIVE_FOUR] == 0:
        #     return 9000
        # if who == 1 and (opponent[PUNCHING_FOUR] > 1 or opponent[LIVE_FOUR] > 0) and myself[PUNCHING_FOUR] + myself[
        #     LIVE_FOUR] == 0:
        #     return -9000
        # if who == -1 and (myself[PUNCHING_FOUR] == 1 or myself[LIVE_THREE] > 0):
        #     return 8500
        # if who == 1 and (opponent[PUNCHING_FOUR] > 1 or opponent[LIVE_THREE] > 1):
        #     return -8500
        # if who == 1 and myself[LIVE_THREE] > 0:
        #     return 8000
        # if who == -1 and opponent[LIVE_THREE] > 0:
        #     return -8000
        # if who == -1 and myself[LIVE_THREE] > 1:
        #     return 7000
        # if who == 1 and opponent[LIVE_THREE] > 1:
        #     return -7000
        #
        # # 不一定死:危险状态
        # if who == 1 and opponent[PUNCHING_FOUR] == 1:
        #     return -6000
        # if who == -1 and myself[PUNCHING_FOUR] == 1:
        #     return 6000
        #
        # # 安全状态
        # value = 0
        # if who == 1:
        #     myself_value = myself[SLEEP_THREE] * 30 + myself[LIVE_TWO] * 10 + myself[SLEEP_TWO] * 5
        #     opponent_value = opponent[SLEEP_THREE] * 10 + opponent[LIVE_TWO] * 5 + opponent[SLEEP_TWO] * 1
        #     value = myself_value - opponent_value
        # if who == -1:
        #     opponent_value = opponent[SLEEP_THREE] * 20 + opponent[LIVE_TWO] * 10 + opponent[SLEEP_TWO] * 3
        #     myself_value = myself[SLEEP_THREE] * 10 + myself[LIVE_TWO] * 5 + myself[SLEEP_TWO] * 1
        #     value = myself_value - opponent_value

        # if chess_type[LINK_FIVE] > 0 or chess_type[LIVE_FOUR] > 0 or chess_type[PUNCHING_FOUR] > 1 or chess_type[
        #     LIVE_THREE] > 1:
        #     return 9999
        # if chess_type[LIVE_THREE]:
        #     value += 20
        # if chess_type[SLEEP_THREE]:
        #     value += chess_type[SLEEP_THREE] * 10
        # if chess_type[LIVE_TWO]:
        #     value += chess_type[LIVE_TWO] * 5
        # if chess_type[SLEEP_TWO]:
        #     value += chess_type[SLEEP_TWO] * 1
        # # 加上每一颗棋子的位置评估
        for i in range(self.chess_board_length):
            for j in range(self.chess_board_width):
                if state[i][j] == 1:
                    value += POSITION_VALUE[i][j]
        return value

    def alpha_beta(self, state, depth, a, b, who):
        if depth == 0:
            return self.eval(state, who)
        children = self.get_children(state, who)
        if who == 1:
            worst = -10000000
            for i in range(len(children)):
                if worst > a:
                    a = worst
                max_v = self.alpha_beta(children[i], depth - 1, a, b, who * -1)
                if max_v > worst:
                    worst = max_v
                if max_v > b:
                    print("b剪枝：", len(children), len(children) - i)
                    break
                    # a = max(b, self.alpha_beta(children[i], depth - 1, a, b, who * -1))
                    # if b <= a:
                    #     return a
                    # a = max(a, self.alpha_beta(children[i], depth - 1, who * -1))
            return worst
        if who == -1:
            best = 10000000
            for i in range(len(children)):
                if best < b:
                    b = best
                min_v = self.alpha_beta(children[i], depth - 1, a, b, who * -1)
                if min_v < best:
                    best = min_v
                if min_v < a:
                    print("a 剪枝：", len(children), len(children) - i)
                    break
                    # a = min(a, self.alpha_beta(children[i], depth - 1, who * -1))
                    # b = min(a, self.alpha_beta(children[i], depth - 1, a, b, who * -1))
                    # if a >= b:
                    #     return b
            return best

    def get_action(self, current_state):
        children = self.get_children(current_state, 1)
        max_value = -1000000
        step = 0
        for i in range(len(children)):
            next_step_value = self.alpha_beta(children[i], 1, -1000000, 1000000, -1)
            # next_step_value = self.alpha_beta(children[i], 3, -1)
            print(next_step_value)
            if max_value < next_step_value:
                max_value = next_step_value
                step = i
        next_state = children[step]
        print(np.array(next_state))
        for i in range(self.chess_board_length):
            for j in range(self.chess_board_width):
                if current_state[i][j] != 0:
                    continue
                if next_state[i][j] != 0:
                    return i, j


if __name__ == '__main__':
    game = Game(INIT_STATE, 15, 15)
    # children = game.get_children(INIT_STATE, 1)
    # for i in range(len(children)):
    #     print(np.mat(children[i]))
    start_time = datetime.datetime.now()
    print(game.get_action(INIT_STATE))
    end_time = datetime.datetime.now()
    print((end_time - start_time).seconds)
    # print(np.array(copy.deepcopy(INIT_STATE)) * -1)
    # for i in range(15):
    #     for j in range(15):
    #         if ChessTypeJudge.live_four(INIT_STATE, i, j, 15, 15) != 0:
    #             print("have a live four")
    # print(game.get_chess_type(np.array(copy.deepcopy(INIT_STATE))*-1))
