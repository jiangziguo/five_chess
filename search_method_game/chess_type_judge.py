# 八个方向，从水平开始，逆时针

class ChessTypeJudge:
    # 眠二
    @staticmethod
    def sleep_two(current_state, index_x, index_y, chess_board_length, chess_board_width):
        sleep_two_num = 0
        if current_state[index_x][index_y] == 0:
            return sleep_two_num
        # -111000
        if index_y + 5 < chess_board_width and current_state[index_x][index_y] == -1 and current_state[index_x][
                    index_y + 1] == current_state[index_x][index_y + 2] == 1 and current_state[index_x][
                    index_y + 3] == current_state[index_x][index_y + 4] == current_state[index_x][index_y + 5] == 0:
            sleep_two_num += 1
        if index_y + 5 < chess_board_width and index_x - 5 >= 0 and current_state[index_x][index_y] == -1 and \
                                current_state[index_x - 1][
                                            index_y + 1] == current_state[index_x - 2][index_y + 2] == 1 and \
                                        current_state[index_x - 3][
                                                    index_y + 3] == current_state[index_x - 4][index_y + 4] == \
                                current_state[index_x - 5][index_y + 5] == 0:
            sleep_two_num += 1
        if index_x - 5 >= 0 and current_state[index_x][index_y] == -1 and current_state[index_x - 1][
            index_y] == current_state[index_x - 2][index_y] == 1 and current_state[index_x - 3][
            index_y] == current_state[index_x - 4][index_y] == current_state[index_x - 5][index_y] == 0:
            sleep_two_num += 1
        if index_y - 5 >= 0 and index_x - 5 >= 0 and current_state[index_x][index_y] == -1 and \
                                current_state[index_x - 1][
                                            index_y - 1] == current_state[index_x - 2][index_y - 2] == 1 and \
                                        current_state[index_x - 3][
                                                    index_y - 3] == current_state[index_x - 4][index_y - 4] == \
                                current_state[index_x - 5][index_y - 5] == 0:
            sleep_two_num += 1
        if index_y - 5 >= 0 and current_state[index_x][index_y] == -1 and current_state[index_x][
                    index_y - 1] == current_state[index_x][index_y - 2] == 1 and current_state[index_x][
                    index_y - 3] == current_state[index_x][index_y - 4] == current_state[index_x][index_y - 5] == 0:
            sleep_two_num += 1
        if index_y - 5 >= 0 and index_x + 5 < chess_board_length and current_state[index_x][index_y] == -1 and \
                                current_state[index_x + 1][
                                            index_y - 1] == current_state[index_x + 2][index_y - 2] == 1 and \
                                        current_state[index_x + 3][
                                                    index_y - 3] == current_state[index_x + 4][index_y - 4] == \
                                current_state[index_x + 5][index_y - 5] == 0:
            sleep_two_num += 1
        if index_x + 5 < chess_board_length and current_state[index_x][index_y] == -1 and current_state[index_x + 1][
            index_y] == current_state[index_x + 2][index_y] == 1 and current_state[index_x + 3][
            index_y] == current_state[index_x + 4][index_y] == current_state[index_x + 5][index_y] == 0:
            sleep_two_num += 1
        if index_y + 5 < chess_board_width and index_x + 5 < chess_board_length and current_state[index_x][
            index_y] == -1 and current_state[index_x + 1][
                    index_y + 1] == current_state[index_x + 2][index_y + 2] == 1 and current_state[index_x + 3][
                    index_y + 3] == current_state[index_x + 4][index_y + 4] == current_state[index_x + 5][
                    index_y + 5] == 0:
            sleep_two_num += 1

        # -110100
        if index_y + 5 < chess_board_width and current_state[index_x][index_y] == -1 and current_state[index_x][
                    index_y + 1] == current_state[index_x][index_y + 3] == 1 and current_state[index_x][
                    index_y + 2] == current_state[index_x][index_y + 4] == current_state[index_x][index_y + 5] == 0:
            sleep_two_num += 1
        if index_y + 5 < chess_board_width and index_x - 5 >= 0 and current_state[index_x][index_y] == -1 and \
                                current_state[index_x - 1][
                                            index_y + 1] == current_state[index_x - 3][index_y + 3] == 1 and \
                                        current_state[index_x - 2][
                                                    index_y + 2] == current_state[index_x - 4][index_y + 4] == \
                                current_state[index_x - 5][index_y + 5] == 0:
            sleep_two_num += 1
        if index_x - 5 >= 0 and current_state[index_x][index_y] == -1 and current_state[index_x - 1][
            index_y] == current_state[index_x - 3][index_y] == 1 and current_state[index_x - 2][
            index_y] == current_state[index_x - 4][index_y] == current_state[index_x - 5][index_y] == 0:
            sleep_two_num += 1
        if index_y - 5 >= 0 and index_x - 5 >= 0 and current_state[index_x][index_y] == -1 and \
                                current_state[index_x - 1][
                                            index_y - 1] == current_state[index_x - 3][index_y - 3] == 1 and \
                                        current_state[index_x - 2][
                                                    index_y - 2] == current_state[index_x - 4][index_y - 4] == \
                                current_state[index_x - 5][index_y - 5] == 0:
            sleep_two_num += 1
        if index_y - 5 >= 0 and current_state[index_x][index_y] == -1 and current_state[index_x][
                    index_y - 1] == current_state[index_x][index_y - 3] == 1 and current_state[index_x][
                    index_y - 2] == current_state[index_x][index_y - 4] == current_state[index_x][index_y - 5] == 0:
            sleep_two_num += 1
        if index_y - 5 >= 0 and index_x + 5 < chess_board_length and current_state[index_x][index_y] == -1 and \
                                current_state[index_x + 1][
                                            index_y - 1] == current_state[index_x + 3][index_y - 3] == 1 and \
                                        current_state[index_x + 2][
                                                    index_y - 2] == current_state[index_x + 4][index_y - 4] == \
                                current_state[index_x + 5][index_y - 5] == 0:
            sleep_two_num += 1
        if index_x + 5 < chess_board_length and current_state[index_x][index_y] == -1 and current_state[index_x + 1][
            index_y] == current_state[index_x + 3][index_y] == 1 and current_state[index_x + 2][
            index_y] == current_state[index_x + 4][index_y] == current_state[index_x + 5][index_y] == 0:
            sleep_two_num += 1
        if index_y + 5 < chess_board_width and index_x + 5 < chess_board_length and current_state[index_x][
            index_y] == -1 and current_state[index_x + 1][
                    index_y + 1] == current_state[index_x + 3][index_y + 3] == 1 and current_state[index_x + 2][
                    index_y + 2] == current_state[index_x + 4][index_y + 4] == current_state[index_x + 5][
                    index_y + 5] == 0:
            sleep_two_num += 1

        # -110010
        if index_y + 5 < chess_board_width and current_state[index_x][index_y] == -1 and current_state[index_x][
                    index_y + 1] == current_state[index_x][index_y + 4] == 1 and current_state[index_x][
                    index_y + 2] == current_state[index_x][index_y + 3] == current_state[index_x][index_y + 5] == 0:
            sleep_two_num += 1
        if index_y + 5 < chess_board_width and index_x - 5 >= 0 and current_state[index_x][index_y] == -1 and \
                                current_state[index_x - 1][
                                            index_y + 1] == current_state[index_x - 4][index_y + 4] == 1 and \
                                        current_state[index_x - 2][
                                                    index_y + 2] == current_state[index_x - 3][index_y + 3] == \
                                current_state[index_x - 5][index_y + 5] == 0:
            sleep_two_num += 1
        if index_x - 5 >= 0 and current_state[index_x][index_y] == -1 and current_state[index_x - 1][
            index_y] == current_state[index_x - 4][index_y] == 1 and current_state[index_x - 2][
            index_y] == current_state[index_x - 3][index_y] == current_state[index_x - 5][index_y] == 0:
            sleep_two_num += 1
        if index_y - 5 >= 0 and index_x - 5 >= 0 and current_state[index_x][index_y] == -1 and \
                                current_state[index_x - 1][
                                            index_y - 1] == current_state[index_x - 4][index_y - 4] == 1 and \
                                        current_state[index_x - 2][
                                                    index_y - 2] == current_state[index_x - 3][index_y - 3] == \
                                current_state[index_x - 5][index_y - 5] == 0:
            sleep_two_num += 1
        if index_y - 5 >= 0 and current_state[index_x][index_y] == -1 and current_state[index_x][
                    index_y - 1] == current_state[index_x][index_y - 4] == 1 and current_state[index_x][
                    index_y - 2] == current_state[index_x][index_y - 3] == current_state[index_x][index_y - 5] == 0:
            sleep_two_num += 1
        if index_y - 5 >= 0 and index_x + 5 < chess_board_length and current_state[index_x][index_y] == -1 and \
                                current_state[index_x + 1][
                                            index_y - 1] == current_state[index_x + 4][index_y - 4] == 1 and \
                                        current_state[index_x + 2][
                                                    index_y - 2] == current_state[index_x + 3][index_y - 3] == \
                                current_state[index_x + 5][index_y - 5] == 0:
            sleep_two_num += 1
        if index_x + 5 < chess_board_length and current_state[index_x][index_y] == -1 and current_state[index_x + 1][
            index_y] == current_state[index_x + 4][index_y] == 1 and current_state[index_x + 2][
            index_y] == current_state[index_x + 3][index_y] == current_state[index_x + 5][index_y] == 0:
            sleep_two_num += 1
        if index_y + 5 < chess_board_width and index_x + 5 < chess_board_length and current_state[index_x][
            index_y] == -1 and current_state[index_x + 1][
                    index_y + 1] == current_state[index_x + 4][index_y + 4] == 1 and current_state[index_x + 2][
                    index_y + 2] == current_state[index_x + 3][index_y + 3] == current_state[index_x + 5][
                    index_y + 5] == 0:
            sleep_two_num += 1

        # 10001
        # if index_y + 4 < chess_board_width and current_state[index_x][index_y] == current_state[index_x][
        #             index_y + 4] == 1 and current_state[index_x][index_y + 1] == current_state[index_x][index_y + 2] == \
        #         current_state[index_x][index_y + 3] == 0:
        #     sleep_two_num += 1
        # if index_y + 4 < chess_board_width and index_x - 4 >= 0 and current_state[index_x][index_y] == \
        #         current_state[index_x - 4][
        #                     index_y + 4] == 1 and current_state[index_x - 1][index_y + 1] == current_state[index_x - 2][
        #             index_y + 2] == \
        #         current_state[index_x - 3][index_y + 3] == 0:
        #     sleep_two_num += 1
        # if index_y + 4 < chess_board_width and index_x - 4 >= 0 and current_state[index_x][index_y] == \
        #         current_state[index_x - 4][
        #                     index_y + 4] == 1 and current_state[index_x - 1][index_y + 1] == current_state[index_x - 2][
        #             index_y + 2] == \
        #         current_state[index_x - 3][index_y + 3] == 0:
        #     sleep_two_num += 1
        # if index_x - 4 >= 0 and current_state[index_x][index_y] == current_state[index_x - 4][
        #     index_y] == 1 and current_state[index_x - 1][index_y] == current_state[index_x - 2][index_y] == \
        #         current_state[index_x - 3][index_y] == 0:
        #     sleep_two_num += 1
        if index_y - 4 >= 0 and index_x - 4 >= 0 and current_state[index_x][index_y] == current_state[index_x - 4][
                    index_y - 4] == 1 and current_state[index_x - 1][index_y - 1] == current_state[index_x - 2][
                    index_y - 2] == \
                current_state[index_x - 3][index_y - 3] == 0:
            sleep_two_num += 1
        if index_y - 4 >= 0 and current_state[index_x][index_y] == current_state[index_x][
                    index_y - 4] == 1 and current_state[index_x][index_y - 1] == current_state[index_x][index_y - 2] == \
                current_state[index_x][index_y - 3] == 0:
            sleep_two_num += 1
        if index_y - 4 >= 0 and index_x + 4 < chess_board_length and current_state[index_x][index_y] == \
                current_state[index_x + 4][
                            index_y - 4] == 1 and current_state[index_x + 1][index_y - 1] == current_state[index_x + 2][
                    index_y - 2] == \
                current_state[index_x + 3][index_y - 3] == 0:
            sleep_two_num += 1
        if index_x + 4 < chess_board_length and current_state[index_x][index_y] == current_state[index_x + 4][
            index_y] == 1 and current_state[index_x + 1][index_y] == current_state[index_x + 2][index_y] == \
                current_state[index_x + 3][index_y] == 0:
            sleep_two_num += 1
        if index_y + 4 < chess_board_width and index_x + 4 < chess_board_length and current_state[index_x][index_y] == \
                current_state[index_x + 4][
                            index_y + 4] == 1 and current_state[index_x + 1][index_y + 1] == current_state[index_x + 2][
                    index_y + 2] == \
                current_state[index_x + 3][index_y + 3] == 0:
            sleep_two_num += 1
        return sleep_two_num

    # 活二
    @staticmethod
    def live_two(current_state, index_x, index_y, chess_board_length, chess_board_width):
        live_two_num = 0
        if current_state[index_x][index_y] == -1:
            return live_two_num
        # 001100
        # if index_y + 5 < chess_board_length and current_state[index_x][index_y] == current_state[index_x][
        #             index_y + 1] == current_state[index_x][index_y + 4] == current_state[index_x][
        #             index_y + 5] == 0 and current_state[index_x][index_y + 2] == current_state[index_x][
        #             index_y + 3] == 1:
        #     live_two_num += 1
        # if index_y + 5 < chess_board_length and index_x - 5 >= 0 and current_state[index_x][index_y] == \
        #         current_state[index_x - 1][
        #                     index_y + 1] == current_state[index_x - 4][index_y + 4] == current_state[index_x - 5][
        #             index_y + 5] == 0 and current_state[index_x - 2][index_y + 2] == current_state[index_x - 3][
        #             index_y + 3] == 1:
        #     live_two_num += 1
        # if index_x - 5 >= 0 and current_state[index_x][index_y] == current_state[index_x - 1][
        #     index_y] == current_state[index_x - 4][index_y] == current_state[index_x - 5][
        #     index_y] == 0 and current_state[index_x - 2][index_y] == current_state[index_x - 3][index_y] == 1:
        #     live_two_num += 1
        # if index_y - 5 >= 0 and index_x - 5 >= 0 and current_state[index_x][index_y] == current_state[index_x - 1][
        #             index_y - 1] == current_state[index_x - 4][index_y - 4] == current_state[index_x - 5][
        #             index_y - 5] == 0 and current_state[index_x - 2][index_y - 2] == current_state[index_x - 3][
        #             index_y - 3] == 1:
        #     live_two_num += 1
        if index_y - 5 >= 0 and current_state[index_x][index_y] == current_state[index_x][
                    index_y - 1] == current_state[index_x][index_y - 4] == current_state[index_x][
                    index_y - 5] == 0 and current_state[index_x][index_y - 2] == current_state[index_x][
                    index_y - 3] == 1:
            live_two_num += 1
        if index_y - 5 >= 0 and index_x + 5 < chess_board_length and current_state[index_x][index_y] == \
                current_state[index_x + 1][
                            index_y - 1] == current_state[index_x + 4][index_y - 4] == current_state[index_x + 5][
                    index_y - 5] == 0 and current_state[index_x + 2][index_y - 2] == current_state[index_x + 3][
                    index_y - 3] == 1:
            live_two_num += 1
        if index_x + 5 < chess_board_length and current_state[index_x][index_y] == current_state[index_x + 1][
            index_y] == current_state[index_x + 4][index_y] == current_state[index_x + 5][
            index_y] == 0 and current_state[index_x + 2][index_y] == current_state[index_x + 3][index_y] == 1:
            live_two_num += 1
        if index_y + 5 < chess_board_width and index_x + 5 < chess_board_length and current_state[index_x][index_y] == \
                current_state[index_x + 1][
                            index_y + 1] == current_state[index_x + 4][index_y + 4] == current_state[index_x + 5][
                    index_y + 5] == 0 and current_state[index_x + 2][index_y + 2] == current_state[index_x + 3][
                    index_y + 3] == 1:
            live_two_num += 1

        # 01010
        # if index_y + 4 < chess_board_width and current_state[index_x][index_y] == current_state[index_x][index_y + 2] == \
        #         current_state[index_x][index_y + 4] == 0 and current_state[index_x][index_y + 1] == \
        #         current_state[index_x][
        #                     index_y + 3] == 1:
        #     live_two_num += 1
        # if index_y + 4 < chess_board_width and index_x - 4 >= 0 and current_state[index_x][index_y] == \
        #         current_state[index_x - 2][index_y + 2] == \
        #         current_state[index_x - 4][index_y + 4] == 0 and current_state[index_x - 1][index_y + 1] == \
        #         current_state[index_x - 3][
        #                     index_y + 3] == 1:
        #     live_two_num += 1
        # if index_x - 4 >= 0 and current_state[index_x][index_y] == current_state[index_x - 2][index_y] == \
        #         current_state[index_x - 4][index_y] == 0 and current_state[index_x - 1][index_y] == \
        #         current_state[index_x - 3][
        #             index_y] == 1:
        #     live_two_num += 1
        # if index_y - 4 >= 0 and index_x - 4 >= 0 and current_state[index_x][index_y] == current_state[index_x - 2][
        #             index_y - 2] == \
        #         current_state[index_x - 4][index_y - 4] == 0 and current_state[index_x - 1][index_y - 1] == \
        #         current_state[index_x - 3][
        #                     index_y - 3] == 1:
        #     live_two_num += 1
        if index_y - 4 >= 0 and current_state[index_x][index_y] == current_state[index_x][index_y - 2] == \
                current_state[index_x][index_y - 4] == 0 and current_state[index_x][index_y - 1] == \
                current_state[index_x][
                            index_y - 3] == 1:
            live_two_num += 1
        if index_y - 4 >= 0 and index_x + 4 < chess_board_length and current_state[index_x][index_y] == \
                current_state[index_x + 2][index_y - 2] == \
                current_state[index_x + 4][index_y - 4] == 0 and current_state[index_x + 1][index_y - 1] == \
                current_state[index_x + 3][
                            index_y - 3] == 1:
            live_two_num += 1
        if index_x + 4 < chess_board_length and current_state[index_x][index_y] == current_state[index_x + 2][
            index_y] == \
                current_state[index_x + 4][index_y] == 0 and current_state[index_x + 1][index_y] == \
                current_state[index_x + 3][
                    index_y] == 1:
            live_two_num += 1
        if index_y + 4 < chess_board_width and index_x + 4 < chess_board_length and current_state[index_x][index_y] == \
                current_state[index_x + 2][index_y + 2] == \
                current_state[index_x + 4][index_y + 4] == 0 and current_state[index_x + 1][index_y + 1] == \
                current_state[index_x + 3][
                            index_y + 3] == 1:
            live_two_num += 1

        # 1001
        # if index_y + 3 < chess_board_width and current_state[index_x][index_y] == current_state[index_x][
        #             index_y + 3] == 1 and current_state[index_x][index_y + 1] == current_state[index_x][
        #             index_y + 2] == 0:
        #     live_two_num += 1
        # if index_y + 3 < chess_board_width and index_x - 3 >= 0 and current_state[index_x][index_y] == \
        #         current_state[index_x - 3][
        #                     index_y + 3] == 1 and current_state[index_x - 1][index_y + 1] == current_state[index_x - 2][
        #             index_y + 2] == 0:
        #     live_two_num += 1
        # if index_x - 3 >= 0 and current_state[index_x][index_y] == current_state[index_x - 3][index_y] == 1 and \
        #                         current_state[index_x - 1][index_y] == current_state[index_x - 2][index_y] == 0:
        #     live_two_num += 1
        # if index_y - 3 >= 0 and index_x - 3 >= 0 and current_state[index_x][index_y] == \
        #         current_state[index_x - 3][
        #                     index_y - 3] == 1 and current_state[index_x - 1][index_y - 1] == current_state[index_x - 2][
        #             index_y - 2] == 0:
        #     live_two_num += 1
        if index_y - 3 >= 0 and current_state[index_x][index_y] == current_state[index_x][
                    index_y - 3] == 1 and current_state[index_x][index_y - 1] == current_state[index_x][
                    index_y - 2] == 0:
            live_two_num += 1
        if index_y - 3 >= 0 and index_x + 3 < chess_board_length and current_state[index_x][index_y] == \
                current_state[index_x + 3][
                            index_y - 3] == 1 and current_state[index_x + 1][index_y - 1] == current_state[index_x + 2][
                    index_y - 2] == 0:
            live_two_num += 1
        if index_x + 3 < chess_board_length and current_state[index_x][index_y] == current_state[index_x + 3][
            index_y] == 1 and \
                                current_state[index_x + 1][index_y] == current_state[index_x + 2][index_y] == 0:
            live_two_num += 1
        if index_y + 3 < chess_board_width and index_x + 3 < chess_board_length and current_state[index_x][index_y] == \
                current_state[index_x + 3][
                            index_y + 3] == 1 and current_state[index_x + 1][index_y + 1] == current_state[index_x + 2][
                    index_y + 2] == 0:
            live_two_num += 1
        return live_two_num

    # 眠三
    @staticmethod
    def sleep_three(current_state, index_x, index_y, chess_board_length, chess_board_width):
        sleep_three_num = 0
        if current_state[index_x][index_y] == 0:
            return sleep_three_num
        # -111100
        if index_y + 5 < chess_board_width and current_state[index_x][index_y] == -1 and current_state[index_x][
                    index_y + 1] == current_state[index_x][index_y + 2] == current_state[index_x][
                    index_y + 3] == 1 and current_state[index_x][index_y + 4] == current_state[index_x][
                    index_y + 5] == 0:
            sleep_three_num += 1
        if index_y + 5 < chess_board_width and index_x - 5 >= 0 and current_state[index_x][index_y] == -1 and \
                                        current_state[index_x - 1][
                                                    index_y + 1] == current_state[index_x - 2][index_y + 2] == \
                                current_state[index_x - 3][
                                            index_y + 3] == 1 and current_state[index_x - 4][index_y + 4] == \
                current_state[index_x - 5][index_y + 5] == 0:
            sleep_three_num += 1
        if index_x - 5 >= 0 and current_state[index_x][index_y] == -1 and \
                                        current_state[index_x - 1][
                                            index_y] == current_state[index_x - 2][index_y] == \
                                current_state[index_x - 3][
                                    index_y] == 1 and current_state[index_x - 4][index_y] == \
                current_state[index_x - 5][index_y] == 0:
            sleep_three_num += 1
        if index_y - 5 >= 0 and index_x - 5 >= 0 and current_state[index_x][index_y] == -1 and \
                                        current_state[index_x - 1][
                                                    index_y - 1] == current_state[index_x - 2][index_y - 2] == \
                                current_state[index_x - 3][
                                            index_y - 3] == 1 and current_state[index_x - 4][index_y - 4] == \
                current_state[index_x - 5][index_y - 5] == 0:
            sleep_three_num += 1
        if index_y - 5 >= 0 and current_state[index_x][index_y] == -1 and \
                                        current_state[index_x][
                                                    index_y - 1] == current_state[index_x][index_y - 2] == \
                                current_state[index_x][
                                            index_y - 3] == 1 and current_state[index_x][index_y - 4] == \
                current_state[index_x][index_y - 5] == 0:
            sleep_three_num += 1
        if index_y - 5 >= 0 and index_x + 5 < chess_board_length and current_state[index_x][index_y] == -1 and \
                                        current_state[index_x + 1][
                                                    index_y - 1] == current_state[index_x + 2][index_y - 2] == \
                                current_state[index_x + 3][
                                            index_y - 3] == 1 and current_state[index_x + 4][index_y - 4] == \
                current_state[index_x + 5][index_y - 5] == 0:
            sleep_three_num += 1
        if index_x + 5 < chess_board_length and current_state[index_x][index_y] == -1 and \
                                        current_state[index_x + 1][
                                            index_y] == current_state[index_x + 2][index_y] == \
                                current_state[index_x + 3][
                                    index_y] == 1 and current_state[index_x + 4][index_y] == \
                current_state[index_x + 5][index_y] == 0:
            sleep_three_num += 1
        if index_y + 5 < chess_board_width and index_x + 5 < chess_board_length and current_state[index_x][
            index_y] == -1 and \
                                        current_state[index_x + 1][
                                                    index_y + 1] == current_state[index_x + 2][index_y + 2] == \
                                current_state[index_x + 3][
                                            index_y + 3] == 1 and current_state[index_x + 4][index_y + 4] == \
                current_state[index_x + 5][index_y + 5] == 0:
            sleep_three_num += 1

        # -1110-10
        if index_y + 5 < chess_board_width and current_state[index_x][index_y] == current_state[index_x][
                    index_y + 4] == -1 and current_state[index_x][index_y + 1] == current_state[index_x][
                    index_y + 2] == 1 and current_state[index_x][index_y + 3] == current_state[index_x][
                    index_y + 5] == 0:
            sleep_three_num += 1
        if index_y + 5 < chess_board_width and index_x - 5 >= 0 and current_state[index_x][index_y] == \
                current_state[index_x - 4][
                            index_y + 4] == -1 and current_state[index_x - 1][index_y + 1] == \
                current_state[index_x - 2][
                            index_y + 2] == 1 and current_state[index_x - 3][index_y + 3] == current_state[index_x - 5][
                    index_y + 5] == 0:
            sleep_three_num += 1
        if index_x - 5 >= 0 and current_state[index_x][index_y] == current_state[index_x - 4][
            index_y] == -1 and current_state[index_x - 1][index_y] == current_state[index_x - 2][
            index_y] == 1 and current_state[index_x - 3][index_y] == current_state[index_x - 5][index_y] == 0:
            sleep_three_num += 1
        if index_x - 5 >= 0 and index_y - 5 >= 0 and current_state[index_x][index_y] == current_state[index_x - 4][
                    index_y - 4] == -1 and current_state[index_x - 1][index_y - 1] == current_state[index_x - 2][
                    index_y - 2] == 1 and current_state[index_x - 3][index_y - 3] == current_state[index_x - 5][
                    index_y - 5] == 0:
            sleep_three_num += 1
        if index_y - 5 >= 0 and current_state[index_x][index_y] == current_state[index_x][
                    index_y - 4] == -1 and current_state[index_x][index_y - 1] == current_state[index_x][
                    index_y - 2] == 1 and current_state[index_x][index_y - 3] == current_state[index_x][
                    index_y - 5] == 0:
            sleep_three_num += 1
        if index_y - 5 >= 0 and index_x + 5 < chess_board_length and current_state[index_x][index_y] == \
                current_state[index_x + 4][
                            index_y - 4] == -1 and current_state[index_x + 1][index_y - 1] == \
                current_state[index_x + 2][
                            index_y - 2] == 1 and current_state[index_x + 3][index_y - 3] == current_state[index_x + 5][
                    index_y - 5] == 0:
            sleep_three_num += 1
        if index_x + 5 < chess_board_length and current_state[index_x][index_y] == current_state[index_x + 4][
            index_y] == -1 and current_state[index_x + 1][index_y] == current_state[index_x + 2][
            index_y] == 1 and current_state[index_x + 3][index_y] == current_state[index_x + 5][index_y] == 0:
            sleep_three_num += 1
        if index_y + 5 < chess_board_width and index_x + 5 < chess_board_length and current_state[index_x][index_y] == \
                current_state[index_x + 4][
                            index_y + 4] == -1 and current_state[index_x + 1][index_y + 1] == \
                current_state[index_x + 2][
                            index_y + 2] == 1 and current_state[index_x + 3][index_y + 3] == current_state[index_x + 5][
                    index_y + 5] == 0:
            sleep_three_num += 1

        # -110110
        if index_y + 5 < chess_board_width and current_state[index_x][index_y] == -1 and current_state[index_x][
                    index_y + 1] == current_state[index_x][index_y + 3] == current_state[index_x][
                    index_y + 4] == 1 and current_state[index_x][index_y + 2] == current_state[index_x][index_y + 5] == 0:
            sleep_three_num += 1
        if index_y + 5 < chess_board_width and index_x - 5 >= 0 and current_state[index_x][index_y] == -1 and \
                                current_state[index_x - 1][
                                            index_y + 1] == current_state[index_x - 3][index_y + 3] == \
                        current_state[index_x - 4][
                                    index_y + 4] == 1 and current_state[index_x - 2][index_y + 2] == \
                current_state[index_x - 5][
                            index_y + 5] == 0:
            sleep_three_num += 1
        if index_x - 5 >= 0 and current_state[index_x][index_y] == -1 and current_state[index_x - 1][
            index_y] == current_state[index_x - 3][index_y] == current_state[index_x - 4][
            index_y] == 1 and current_state[index_x - 2][index_y] == current_state[index_x - 5][index_y] == 0:
            sleep_three_num += 1
        if index_x - 5 >= 0 and index_y - 5 >= 0 and current_state[index_x][index_y] == -1 and \
                                current_state[index_x - 1][
                                            index_y - 1] == current_state[index_x - 3][index_y - 3] == \
                        current_state[index_x - 4][
                                    index_y - 4] == 1 and current_state[index_x - 2][index_y - 2] == \
                current_state[index_x - 5][
                            index_y - 5] == 0:
            sleep_three_num += 1
        if index_y - 5 >= 0 and current_state[index_x][index_y] == -1 and current_state[index_x][
                    index_y - 1] == current_state[index_x][index_y - 3] == current_state[index_x][
                    index_y - 4] == 1 and current_state[index_x][index_y - 2] == current_state[index_x][index_y - 5] == 0:
            sleep_three_num += 1
        if index_y - 5 >= 0 and index_x + 5 < chess_board_length and current_state[index_x][index_y] == -1 and \
                                current_state[index_x + 1][
                                            index_y - 1] == current_state[index_x + 3][index_y - 3] == \
                        current_state[index_x + 4][
                                    index_y - 4] == 1 and current_state[index_x + 2][index_y - 2] == \
                current_state[index_x + 5][
                            index_y - 5] == 0:
            sleep_three_num += 1
        if index_x + 5 < chess_board_length and current_state[index_x][index_y] == -1 and current_state[index_x + 1][
            index_y] == current_state[index_x + 3][index_y] == current_state[index_x + 4][
            index_y] == 1 and current_state[index_x + 2][index_y] == current_state[index_x + 5][index_y] == 0:
            sleep_three_num += 1
        if index_x + 5 < chess_board_length and index_y + 5 < chess_board_width and current_state[index_x][
            index_y] == -1 and current_state[index_x + 1][
                    index_y + 1] == current_state[index_x + 3][index_y + 3] == current_state[index_x + 4][
                    index_y + 4] == 1 and current_state[index_x + 2][index_y + 2] == current_state[index_x + 5][
                    index_y + 5] == 0:
            sleep_three_num += 1

        # 11001
        if index_y + 4 < chess_board_width and current_state[index_x][index_y] == current_state[index_x][
                    index_y + 1] == current_state[index_x][index_y + 4] == 1 and current_state[index_x][
                    index_y + 2] == current_state[index_x][index_y + 3] == 0:
            sleep_three_num += 1
        if index_y + 4 < chess_board_width and index_x - 4 >= 0 and current_state[index_x][index_y] == \
                current_state[index_x - 1][
                            index_y + 1] == current_state[index_x - 4][index_y + 4] == 1 and current_state[index_x - 2][
                    index_y + 2] == current_state[index_x - 3][index_y + 3] == 0:
            sleep_three_num += 1
        if index_x - 4 >= 0 and current_state[index_x][index_y] == current_state[index_x - 1][
            index_y] == current_state[index_x - 4][index_y] == 1 and current_state[index_x - 2][
            index_y] == current_state[index_x - 3][index_y] == 0:
            sleep_three_num += 1
        if index_x - 4 >= 0 and index_y - 4 >= 0 and current_state[index_x][index_y] == current_state[index_x - 1][
                    index_y - 1] == current_state[index_x - 4][index_y - 4] == 1 and current_state[index_x - 2][
                    index_y - 2] == current_state[index_x - 3][index_y - 3] == 0:
            sleep_three_num += 1
        if index_y - 4 >= 0 and current_state[index_x][index_y] == current_state[index_x][
                    index_y - 1] == current_state[index_x][index_y - 4] == 1 and current_state[index_x][
                    index_y - 2] == current_state[index_x][index_y - 3] == 0:
            sleep_three_num += 1
        if index_x + 4 < chess_board_length and index_y - 4 >= 0 and current_state[index_x][index_y] == \
                current_state[index_x + 1][
                            index_y - 1] == current_state[index_x + 4][index_y - 4] == 1 and current_state[index_x + 2][
                    index_y - 2] == current_state[index_x + 3][index_y - 3] == 0:
            sleep_three_num += 1
        if index_x + 4 < chess_board_length and current_state[index_x][index_y] == current_state[index_x + 1][
            index_y] == current_state[index_x + 4][index_y] == 1 and current_state[index_x + 2][
            index_y] == current_state[index_x + 3][index_y] == 0:
            sleep_three_num += 1
        if index_x + 4 < chess_board_length and index_y + 4 < chess_board_width and current_state[index_x][index_y] == \
                current_state[index_x + 1][
                            index_y + 1] == current_state[index_x + 4][index_y + 4] == 1 and current_state[index_x + 2][
                    index_y + 2] == current_state[index_x + 3][index_y + 3] == 0:
            sleep_three_num += 1

        # 10101
        # if index_y + 4 < chess_board_width and current_state[index_x][index_y] == current_state[index_x][
        #             index_y + 2] == current_state[index_x][index_y + 4] == 1 and current_state[index_x][
        #             index_y + 1] == current_state[index_x][index_y + 3] == 0:
        #     sleep_three_num += 1
        # if index_y + 4 < chess_board_width and index_x - 4 >= 0 and current_state[index_x][index_y] == \
        #         current_state[index_x - 2][
        #                     index_y + 2] == current_state[index_x - 4][index_y + 4] == 1 and current_state[index_x - 1][
        #             index_y + 1] == current_state[index_x - 3][index_y + 3] == 0:
        #     sleep_three_num += 1
        # if index_x - 4 >= 0 and current_state[index_x][index_y] == current_state[index_x - 2][
        #     index_y] == current_state[index_x - 4][index_y] == 1 and current_state[index_x - 1][
        #     index_y] == current_state[index_x - 3][index_y] == 0:
        #     sleep_three_num += 1
        # if index_x - 4 >= 0 and index_y - 4 >= 0 and current_state[index_x][index_y] == current_state[index_x - 2][
        #             index_y - 2] == current_state[index_x - 4][index_y - 4] == 1 and current_state[index_x - 1][
        #             index_y - 1] == current_state[index_x - 3][index_y - 3] == 0:
        #     sleep_three_num += 1
        if index_y - 4 >= 0 and current_state[index_x][index_y] == current_state[index_x][
                    index_y - 2] == current_state[index_x][index_y - 4] == 1 and current_state[index_x][
                    index_y - 1] == current_state[index_x][index_y - 3] == 0:
            sleep_three_num += 1
        if index_x + 4 < chess_board_length and index_y - 4 >= 0 and current_state[index_x][index_y] == \
                current_state[index_x + 2][
                            index_y - 2] == current_state[index_x + 4][index_y - 4] == 1 and current_state[index_x + 1][
                    index_y - 1] == current_state[index_x + 3][index_y - 3] == 0:
            sleep_three_num += 1
        if index_x + 4 < chess_board_length and current_state[index_x][index_y] == current_state[index_x + 2][
            index_y] == current_state[index_x + 4][index_y] == 1 and current_state[index_x + 1][
            index_y] == current_state[index_x + 3][index_y] == 0:
            sleep_three_num += 1
        if index_x + 4 < chess_board_length and index_y + 4 < chess_board_width and current_state[index_x][index_y] == \
                current_state[index_x + 2][
                            index_y + 2] == current_state[index_x + 4][index_y + 4] == 1 and current_state[index_x + 1][
                    index_y + 1] == current_state[index_x + 3][index_y + 3] == 0:
            sleep_three_num += 1

        # -101110-1
        # if index_y + 6 < chess_board_width and current_state[index_x][index_y] == current_state[index_x][
        #             index_y + 6] == -1 and current_state[index_x][index_y + 2] == current_state[index_x][index_y + 3] == \
        #         current_state[index_x][index_y + 4] == 1 and current_state[index_x][index_y + 1] == \
        #         current_state[index_x][
        #                     index_y + 5] == 0:
        #     sleep_three_num += 1
        # if index_y + 6 < chess_board_width and index_x - 6 >= 0 and current_state[index_x][index_y] == \
        #         current_state[index_x - 6][
        #                     index_y + 6] == -1 and current_state[index_x - 2][index_y + 2] == \
        #         current_state[index_x - 3][
        #                     index_y + 3] == \
        #         current_state[index_x - 4][index_y + 4] == 1 and current_state[index_x - 1][index_y + 1] == \
        #         current_state[index_x - 5][
        #                     index_y + 5] == 0:
        #     sleep_three_num += 1
        # if index_x - 6 >= 0 and current_state[index_x][index_y] == current_state[index_x - 6][
        #     index_y] == -1 and current_state[index_x - 2][index_y] == current_state[index_x - 3][index_y] == \
        #         current_state[index_x - 4][index_y] == 1 and current_state[index_x - 1][index_y] == \
        #         current_state[index_x - 5][
        #             index_y] == 0:
        #     sleep_three_num += 1
        # if index_x - 6 >= 0 and index_y - 6 >= 0 and current_state[index_x][index_y] == current_state[index_x - 6][
        #             index_y - 6] == -1 and current_state[index_x - 2][index_y - 2] == current_state[index_x - 3][
        #             index_y - 3] == \
        #         current_state[index_x - 4][index_y - 4] == 1 and current_state[index_x - 1][index_y - 1] == \
        #         current_state[index_x - 5][
        #                     index_y - 5] == 0:
        #     sleep_three_num += 1
        if index_y - 6 >= 0 and current_state[index_x][index_y] == current_state[index_x][
                    index_y - 6] == -1 and current_state[index_x][index_y - 2] == current_state[index_x][index_y - 3] == \
                current_state[index_x][index_y - 4] == 1 and current_state[index_x][index_y - 1] == \
                current_state[index_x][
                            index_y - 5] == 0:
            sleep_three_num += 1
        if index_y - 6 >= 0 and index_x + 6 < chess_board_length and current_state[index_x][index_y] == \
                current_state[index_x + 6][
                            index_y - 6] == -1 and current_state[index_x + 2][index_y - 2] == \
                current_state[index_x + 3][
                            index_y - 3] == \
                current_state[index_x + 4][index_y - 4] == 1 and current_state[index_x + 1][index_y - 1] == \
                current_state[index_x + 5][
                            index_y - 5] == 0:
            sleep_three_num += 1
        if index_x + 6 < chess_board_length and current_state[index_x][index_y] == current_state[index_x + 6][
            index_y] == -1 and current_state[index_x + 2][index_y] == current_state[index_x + 3][index_y] == \
                current_state[index_x + 4][index_y] == 1 and current_state[index_x + 1][index_y] == \
                current_state[index_x + 5][
                    index_y] == 0:
            sleep_three_num += 1
        if index_x + 6 < chess_board_length and index_y + 6 < chess_board_width and current_state[index_x][index_y] == \
                current_state[index_x + 6][
                            index_y + 6] == -1 and current_state[index_x + 2][index_y + 2] == \
                current_state[index_x + 3][
                            index_y + 3] == \
                current_state[index_x + 4][index_y + 4] == 1 and current_state[index_x + 1][index_y + 1] == \
                current_state[index_x + 5][
                            index_y + 5] == 0:
            sleep_three_num += 1
        return sleep_three_num

    # 活三
    @staticmethod
    def live_three(current_state, index_x, index_y, chess_board_length, chess_board_width):
        live_three_num = 0
        if current_state[index_x][index_y] == -1:
            return live_three_num
        # 01110 因为对称，所以要遍历方向要减半
        # if index_y + 4 < chess_board_width and current_state[index_x][index_y] == current_state[index_x][
        #             index_y + 4] == 0 and current_state[index_x][index_y + 1] == current_state[index_x][
        #             index_y + 2] == current_state[index_x][index_y + 3] == 1:
        #     live_three_num += 1
        # if index_y + 4 < chess_board_width and index_x - 4 >= 0 and current_state[index_x][index_y] == \
        #         current_state[index_x - 4][
        #                     index_y + 4] == 0 and current_state[index_x - 1][index_y + 1] == current_state[index_x - 2][
        #             index_y + 2] == current_state[index_x - 3][index_y + 3] == 1:
        #     live_three_num += 1
        # if index_x - 4 >= 0 and current_state[index_x][index_y] == current_state[index_x - 4][
        #     index_y] == 0 and current_state[index_x - 1][index_y] == current_state[index_x - 2][
        #     index_y] == current_state[index_x - 3][index_y] == 1:
        #     live_three_num += 1
        # if index_x - 4 >= 0 and index_y - 4 >= 0 and current_state[index_x][index_y] == current_state[index_x - 4][
        #             index_y - 4] == 0 and current_state[index_x - 1][index_y - 1] == current_state[index_x - 2][
        #             index_y - 2] == current_state[index_x - 3][index_y - 3] == 1:
        #     live_three_num += 1
        if index_y - 4 >= 0 and current_state[index_x][index_y] == current_state[index_x][
                    index_y - 4] == 0 and current_state[index_x][index_y - 1] == current_state[index_x][
                    index_y - 2] == current_state[index_x][index_y - 3] == 1:
            live_three_num += 1
        if index_y - 4 >= 0 and index_x + 4 < chess_board_length and current_state[index_x][index_y] == \
                current_state[index_x + 4][
                            index_y - 4] == 0 and current_state[index_x + 1][index_y - 1] == current_state[index_x + 2][
                    index_y - 2] == current_state[index_x + 3][index_y - 3] == 1:
            live_three_num += 1
        if index_x + 4 < chess_board_length and current_state[index_x][index_y] == current_state[index_x + 4][
            index_y] == 0 and current_state[index_x + 1][index_y] == current_state[index_x + 2][
            index_y] == current_state[index_x + 3][index_y] == 1:
            live_three_num += 1
        if index_y + 4 < chess_board_width and index_x + 4 < chess_board_length and current_state[index_x][index_y] == \
                current_state[index_x + 4][
                            index_y + 4] == 0 and current_state[index_x + 1][index_y + 1] == current_state[index_x + 2][
                    index_y + 2] == current_state[index_x + 3][index_y + 3] == 1:
            live_three_num += 1

        # 1101
        if index_y + 3 < chess_board_width and current_state[index_x][index_y] == current_state[index_x][
                    index_y + 1] == current_state[index_x][index_y + 3] == 1 and current_state[index_x][
                    index_y + 2] == 0:
            live_three_num += 1
        if index_y + 3 < chess_board_width and index_x - 3 >= 0 and current_state[index_x][index_y] == \
                current_state[index_x - 1][
                            index_y + 1] == current_state[index_x - 3][index_y + 3] == 1 and current_state[index_x - 2][
                    index_y + 2] == 0:
            live_three_num += 1
        if index_x - 3 >= 0 and current_state[index_x][index_y] == current_state[index_x - 1][
            index_y] == current_state[index_x - 3][index_y] == 1 and current_state[index_x - 2][index_y] == 0:
            live_three_num += 1
        if index_y - 3 >= 0 and index_x - 3 >= 0 and current_state[index_x][index_y] == current_state[index_x - 1][
                    index_y - 1] == current_state[index_x - 3][index_y - 3] == 1 and current_state[index_x - 2][
                    index_y - 2] == 0:
            live_three_num += 1
        if index_y - 3 >= 0 and current_state[index_x][index_y] == current_state[index_x][
                    index_y - 1] == current_state[index_x][index_y - 3] == 1 and current_state[index_x][
                    index_y - 2] == 0:
            live_three_num += 1
        if index_y - 3 >= 0 and index_x + 3 < chess_board_length and current_state[index_x][index_y] == \
                current_state[index_x + 1][
                            index_y - 1] == current_state[index_x + 3][index_y - 3] == 1 and current_state[index_x + 2][
                    index_y - 2] == 0:
            live_three_num += 1
        if index_x + 3 < chess_board_length and current_state[index_x][index_y] == current_state[index_x + 1][
            index_y] == current_state[index_x + 3][index_y] == 1 and current_state[index_x + 2][index_y] == 0:
            live_three_num += 1
        if index_y + 3 < chess_board_width and index_x + 3 < chess_board_length and current_state[index_x][index_y] == \
                current_state[index_x + 1][
                            index_y + 1] == current_state[index_x + 3][index_y + 3] == 1 and current_state[index_x + 2][
                    index_y + 2] == 0:
            live_three_num += 1
        return live_three_num

    # 冲四
    @staticmethod
    def punching_four(current_state, index_x, index_y, chess_board_length, chess_board_width):
        punching_four = 0
        if current_state[index_x][index_y] == 0:
            return punching_four
        # -111110
        if index_y + 5 < chess_board_width and current_state[index_x][index_y] == -1 and current_state[index_x][
                    index_y + 5] == 0 and current_state[index_x][index_y + 1] == current_state[index_x][index_y + 2] == \
                current_state[index_x][index_y + 3] == current_state[index_x][index_y + 4] == 1:
            punching_four += 1
        if index_y + 5 < chess_board_width and index_x - 5 >= 0 and current_state[index_x][index_y] == -1 and \
                        current_state[index_x - 5][
                                    index_y + 5] == 0 and current_state[index_x - 1][index_y + 1] == \
                current_state[index_x - 2][index_y + 2] == \
                current_state[index_x - 3][index_y + 3] == current_state[index_x - 4][index_y + 4] == 1:
            punching_four += 1
        if index_x - 5 >= 0 and current_state[index_x][index_y] == -1 and current_state[index_x - 5][
            index_y] == 0 and current_state[index_x - 1][index_y] == current_state[index_x - 2][index_y] == \
                current_state[index_x - 3][index_y] == current_state[index_x - 4][index_y] == 1:
            punching_four += 1
        if index_x - 5 >= 0 and index_y - 5 >= 0 and current_state[index_x][index_y] == -1 and \
                        current_state[index_x - 5][
                                    index_y - 5] == 0 and current_state[index_x - 1][index_y - 1] == \
                current_state[index_x - 2][
                            index_y - 2] == \
                current_state[index_x - 3][index_y - 3] == current_state[index_x - 4][index_y - 4] == 1:
            punching_four += 1
        if index_y - 5 >= 0 and current_state[index_x][index_y] == -1 and current_state[index_x][
                    index_y - 5] == 0 and current_state[index_x][index_y - 1] == current_state[index_x][index_y - 2] == \
                current_state[index_x][index_y - 3] == current_state[index_x][index_y - 4] == 1:
            punching_four += 1
        if index_y - 5 >= 0 and index_x + 5 < chess_board_length and current_state[index_x][index_y] == -1 and \
                        current_state[index_x + 5][
                                    index_y - 5] == 0 and current_state[index_x + 1][index_y - 1] == \
                current_state[index_x + 2][index_y - 2] == \
                current_state[index_x + 3][index_y - 3] == current_state[index_x + 4][index_y - 4] == 1:
            punching_four += 1
        if index_x + 5 < chess_board_length and current_state[index_x][index_y] == -1 and current_state[index_x + 5][
            index_y] == 0 and current_state[index_x + 1][index_y] == current_state[index_x + 2][index_y] == \
                current_state[index_x + 3][index_y] == current_state[index_x + 4][index_y] == 1:
            punching_four += 1
        if index_x + 5 < chess_board_length and index_y + 5 < chess_board_width and current_state[index_x][
            index_y] == -1 and current_state[index_x + 5][
                    index_y + 5] == 0 and current_state[index_x + 1][index_y + 1] == current_state[index_x + 2][
                    index_y + 2] == \
                current_state[index_x + 3][index_y + 3] == current_state[index_x + 4][index_y + 4] == 1:
            punching_four += 1

        # 11101
        if index_y + 4 < chess_board_width and current_state[index_x][index_y] == current_state[index_x][
                    index_y + 1] == current_state[index_x][index_y + 2] == current_state[index_x][index_y + 4] == 1 and \
                        current_state[index_x][index_y + 3] == 0:
            punching_four += 1
        if index_y + 4 < chess_board_width and index_x - 4 >= 0 and current_state[index_x][index_y] == \
                current_state[index_x - 1][
                            index_y + 1] == current_state[index_x - 2][index_y + 2] == current_state[index_x - 4][
                    index_y + 4] == 1 and \
                        current_state[index_x - 3][index_y + 3] == 0:
            punching_four += 1
        if index_x - 4 >= 0 and current_state[index_x][index_y] == current_state[index_x - 1][
            index_y] == current_state[index_x - 2][index_y] == current_state[index_x - 4][index_y] == 1 and \
                        current_state[index_x - 3][index_y] == 0:
            punching_four += 1
        if index_x - 4 >= 0 and index_y - 4 >= 0 and current_state[index_x][index_y] == current_state[index_x - 1][
                    index_y - 1] == current_state[index_x - 2][index_y - 2] == current_state[index_x - 4][
                    index_y - 4] == 1 and \
                        current_state[index_x - 3][index_y - 3] == 0:
            punching_four += 1
        if index_y - 4 >= 0 and current_state[index_x][index_y] == current_state[index_x][
                    index_y - 1] == current_state[index_x][index_y - 2] == current_state[index_x][index_y - 4] == 1 and \
                        current_state[index_x][index_y - 3] == 0:
            punching_four += 1
        if index_x + 4 < chess_board_length and index_y - 4 >= 0 and current_state[index_x][index_y] == \
                current_state[index_x + 1][
                            index_y - 1] == current_state[index_x + 2][index_y - 2] == current_state[index_x + 4][
                    index_y - 4] == 1 and \
                        current_state[index_x + 3][index_y - 3] == 0:
            punching_four += 1
        if index_x + 4 < chess_board_length and current_state[index_x][index_y] == current_state[index_x + 1][
            index_y] == current_state[index_x + 2][index_y] == current_state[index_x + 4][index_y] == 1 and \
                        current_state[index_x + 3][index_y] == 0:
            punching_four += 1
        if index_x + 4 < chess_board_length and index_y + 4 < chess_board_width and current_state[index_x][index_y] == \
                current_state[index_x + 1][
                            index_y + 1] == current_state[index_x + 2][index_y + 2] == current_state[index_x + 4][
                    index_y + 4] == 1 and \
                        current_state[index_x + 3][index_y + 3] == 0:
            punching_four += 1

        # 11011
        # if index_y + 4 < chess_board_width and current_state[index_x][index_y] == current_state[index_x][
        #             index_y + 1] == current_state[index_x][index_y + 3] == current_state[index_x][index_y + 4] == 1 and \
        #                 current_state[index_x][index_y + 2] == 0:
        #     punching_four += 1
        # if index_y + 4 < chess_board_width and index_x - 4 >= 0 and current_state[index_x][index_y] == \
        #         current_state[index_x - 1][
        #                     index_y + 1] == current_state[index_x - 3][index_y + 3] == current_state[index_x - 4][
        #             index_y + 4] == 1 and \
        #                 current_state[index_x - 2][index_y + 2] == 0:
        #     punching_four += 1
        # if index_x - 4 >= 0 and current_state[index_x][index_y] == current_state[index_x - 1][
        #     index_y] == current_state[index_x - 3][index_y] == current_state[index_x - 4][index_y] == 1 and \
        #                 current_state[index_x - 2][index_y] == 0:
        #     punching_four += 1
        # if index_x - 4 >= 0 and index_y - 4 >= 0 and current_state[index_x][index_y] == current_state[index_x - 1][
        #             index_y - 1] == current_state[index_x - 3][index_y - 3] == current_state[index_x - 4][
        #             index_y - 4] == 1 and \
        #                 current_state[index_x - 2][index_y - 2] == 0:
        #     punching_four += 1
        if index_y - 4 >= 0 and current_state[index_x][index_y] == current_state[index_x][
                    index_y - 1] == current_state[index_x][index_y - 3] == current_state[index_x][index_y - 4] == 1 and \
                        current_state[index_x][index_y - 2] == 0:
            punching_four += 1
        if index_x + 4 < chess_board_length and index_y - 4 >= 0 and current_state[index_x][index_y] == \
                current_state[index_x + 1][
                            index_y - 1] == current_state[index_x + 3][index_y - 3] == current_state[index_x + 4][
                    index_y - 4] == 1 and \
                        current_state[index_x + 2][index_y - 2] == 0:
            punching_four += 1
        if index_x + 4 < chess_board_length and current_state[index_x][index_y] == current_state[index_x + 1][
            index_y] == current_state[index_x + 3][index_y] == current_state[index_x + 4][index_y] == 1 and \
                        current_state[index_x + 2][index_y] == 0:
            punching_four += 1
        if index_x + 4 < chess_board_length and index_y + 4 < chess_board_width and current_state[index_x][index_y] == \
                current_state[index_x + 1][
                            index_y + 1] == current_state[index_x + 3][index_y + 3] == current_state[index_x + 4][
                    index_y + 4] == 1 and \
                        current_state[index_x + 2][index_y + 2] == 0:
            punching_four += 1
        return punching_four

    # 活四
    @staticmethod
    def live_four(current_state, index_x, index_y, chess_board_length, chess_board_width):
        live_four = 0
        if current_state[index_x][index_y] != 0:
            return live_four
        # 011110
        if index_y + 5 < chess_board_width and current_state[index_x][index_y] == current_state[index_x][
                    index_y + 5] == 0 and current_state[index_x][index_y + 1] == current_state[index_x][index_y + 2] == \
                current_state[index_x][index_y + 3] == current_state[index_x][index_y + 4] ==1:
            live_four += 1
        if index_y + 5 < chess_board_width and index_x - 5 >= 0 and current_state[index_x][index_y] == \
                current_state[index_x - 5][
                            index_y + 5] == 0 and current_state[index_x - 1][index_y + 1] == current_state[index_x - 2][
                    index_y + 2] == \
                current_state[index_x - 3][index_y + 3] == current_state[index_x - 4][index_y + 4] ==1:
            live_four += 1
        if index_x - 5 >= 0 and current_state[index_x][index_y] == current_state[index_x - 5][
            index_y] == 0 and current_state[index_x - 1][index_y] == current_state[index_x - 2][index_y] == \
                current_state[index_x - 3][index_y] == current_state[index_x - 4][index_y] == 1:
            live_four += 1
        if index_x - 5 >= 0 and index_y - 5 >= 0 and current_state[index_x][index_y] == current_state[index_x - 5][
                    index_y - 5] == 0 and current_state[index_x - 1][index_y - 1] == current_state[index_x - 2][
                    index_y - 2] == \
                current_state[index_x - 3][index_y - 3] == current_state[index_x - 4][index_y - 4] == 1:
            live_four += 1
        if index_y - 5 >= 0 and current_state[index_x][index_y] == current_state[index_x][
                    index_y - 5] == 0 and current_state[index_x][index_y - 1] == current_state[index_x][index_y - 2] == \
                current_state[index_x][index_y - 3] == current_state[index_x][index_y - 4] == 1:
            live_four += 1
        if index_y - 5 >= 0 and index_x + 5 < chess_board_length and current_state[index_x][index_y] == \
                current_state[index_x + 5][
                            index_y - 5] == 0 and current_state[index_x + 1][index_y - 1] == current_state[index_x + 2][
                    index_y - 2] == \
                current_state[index_x + 3][index_y - 3] == current_state[index_x + 4][index_y - 4] == 1:
            live_four += 1
        if index_x + 5 < chess_board_length and current_state[index_x][index_y] == current_state[index_x + 5][
            index_y] == 0 and current_state[index_x + 1][index_y] == current_state[index_x + 2][index_y] == \
                current_state[index_x + 3][index_y] == current_state[index_x + 4][index_y] == 1:
            live_four += 1
        if index_x + 5 < chess_board_length and index_y + 5 < chess_board_width and current_state[index_x][index_y] == \
                current_state[index_x + 5][
                            index_y + 5] == 0 and current_state[index_x + 1][index_y + 1] == current_state[index_x + 2][
                    index_y + 2] == \
                current_state[index_x + 3][index_y + 3] == current_state[index_x + 4][index_y + 4] == 1:
            live_four += 1
        return live_four

    # 连五
    @staticmethod
    def link_five(current_state, index_x, index_y, chess_board_length, chess_board_width):
        link_five_num = 0
        if current_state[index_x][index_y] != 1:
            return link_five_num
        # if index_y + 4 < chess_board_width and current_state[index_x][index_y] == current_state[index_x][index_y + 1] == \
        #         current_state[index_x][index_y + 2] == current_state[index_x][index_y + 3] == current_state[index_x][
        #             index_y + 4] == 1:
        #     link_five_num += 1
        # if index_y + 4 < chess_board_width and index_x - 4 >= 0 and current_state[index_x][index_y] == \
        #         current_state[index_x - 1][index_y + 1] == \
        #         current_state[index_x - 2][index_y + 2] == current_state[index_x - 3][index_y + 3] == \
        #         current_state[index_x - 4][
        #                     index_y + 4] == 1:
        #     link_five_num += 1
        # if index_x - 4 >= 0 and current_state[index_x][index_y] == current_state[index_x - 1][index_y] == \
        #         current_state[index_x - 2][index_y] == current_state[index_x - 3][index_y] == \
        #         current_state[index_x - 4][
        #             index_y] == 1:
        #     link_five_num += 1
        # if index_x - 4 >= 0 and index_y - 4 >= 0 and current_state[index_x][index_y] == current_state[index_x - 1][
        #             index_y - 1] == \
        #         current_state[index_x - 2][index_y - 2] == current_state[index_x - 3][index_y - 3] == \
        #         current_state[index_x - 4][
        #                     index_y - 4] == 1:
        #     link_five_num += 1
        if index_y - 4 >= 0 and current_state[index_x][index_y] == current_state[index_x][index_y - 1] == \
                current_state[index_x][index_y - 2] == current_state[index_x][index_y - 3] == current_state[index_x][
                    index_y - 4] == 1:
            link_five_num += 1
        if index_x + 4 < chess_board_length and index_y - 4 >= 0 and current_state[index_x][index_y] == \
                current_state[index_x + 1][index_y - 1] == \
                current_state[index_x + 2][index_y - 2] == current_state[index_x + 3][index_y - 3] == \
                current_state[index_x + 4][
                            index_y - 4] == 1:
            link_five_num += 1
        if index_x + 4 < chess_board_length and current_state[index_x][index_y] == current_state[index_x + 1][
            index_y] == \
                current_state[index_x + 2][index_y] == current_state[index_x + 3][index_y] == \
                current_state[index_x + 4][
                    index_y] == 1:
            link_five_num += 1
        if index_x + 4 < chess_board_length and index_y + 4 < chess_board_width and current_state[index_x][index_y] == \
                current_state[index_x + 1][index_y + 1] == \
                current_state[index_x + 2][index_y + 2] == current_state[index_x + 3][index_y + 3] == \
                current_state[index_x + 4][
                            index_y + 4] == 1:
            link_five_num += 1
        return link_five_num
