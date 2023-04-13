from collections import deque


def solution(begin, target, words):
    if target not in words:  # target이 words에 없으면 변환이 불가능한 경우이므로 0을 반환
        return 0

    visited = [False] * len(words)  # 단어 방문 여부를 기록할 리스트를 생성합니다.
    # BFS 탐색을 위한 큐를 생성합니다. 시작 단어(begin)와 변환 횟수(0)를 큐에 추가합니다.
    queue = deque([(begin, 0)])

    while queue:
        cur_word, count = queue.popleft()  # 현재 큐의 첫번째 원소를 꺼냅니다.

        # 현재 단어가 target과 같으면 탐색을 종료하고 변환 횟수(count)를 반환합니다.
        if cur_word == target:
            return count

        for i in range(len(words)):
            # 방문하지 않은 단어이며, 변환 가능한 단어일 경우 탐색을 계속합니다.
            if not visited[i] and is_convertible(cur_word, words[i]):
                visited[i] = True  # 해당 단어를 방문으로 처리합니다.
                # 변환 가능한 단어를 큐에 추가하고 변환 횟수를 1 증가시켜서 큐에 추가합니다.
                queue.append((words[i], count+1))

    return 0  # 큐가 빈 상태로 종료되었다면 변환할 수 없는 경우이므로 0을 반환합니다.


def is_convertible(word1, word2):
    count = 0
    for w1, w2 in zip(word1, word2):
        if w1 != w2:
            count += 1
        if count > 1:  # 알파벳 하나만 바꿀 수 있으므로 count가 1보다 크면 변환할 수 없는 단어이므로 False를 반환합니다.
            return False
    return True  # 변환 가능한 단어이므로 True를 반환합니다.
