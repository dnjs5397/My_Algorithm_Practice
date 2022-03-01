# 모든 경우의 수를 상태공간트리로 표현
# DFS 방식을 이용해 탐색

def is_available(candidate, current_col):
    current_row = len(candidate)
    for queen_row in range(current_row):
        if candidate[queen_row] == current_col or abs(candidate[queen_row] - current_col) == current_row

def DFS(N, current_row, current_candidate, final_result):
    if current_row == N:
        final_result.append(current_candidate)
        return
    for candidate_col in range(N):
        if is_available(current_candidate, candidate_col):
            current_candidate.append(candidate_col)
            DFS(N, current_row+1, current_candidate, final_result)
            current_candidate.pop()

def solve_n_queen(N):
    final_result = []
    DFS(N, 0, [], final_result)
    return final_result