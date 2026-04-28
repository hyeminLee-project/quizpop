"""
LeetCode #1 복습 — Two Sum 변형

이번엔 print 없이, 보지 않고 직접 풀어보세요!
구조는 똑같아요:
  1. 첫 번째 숫자 고르기 (for i)
  2. 두 번째 숫자 고르기 (for j, i 다음부터)
  3. 합이 target이면 [i, j] 반환
"""


def two_sum(nums, target):
    # 여기에 풀이를 작성하세요!
    pass


# --- 테스트 ---
if __name__ == "__main__":
    tests = [
        {"nums": [1, 5, 3, 7], "target": 8, "expected": [0, 3]},
        {"nums": [10, 20, 30, 40], "target": 50, "expected": [1, 2]},
        {"nums": [4, 4], "target": 8, "expected": [0, 1]},
        {"nums": [1, 2, 3, 4, 5], "target": 9, "expected": [3, 4]},
    ]

    for i, t in enumerate(tests, 1):
        result = two_sum(t["nums"], t["target"])
        status = "✅" if result == t["expected"] else "❌"
        print(f"테스트 {i}: {status}  입력: {t['nums']}, target={t['target']}")
        print(f"  기대값: {t['expected']}, 결과: {result}")
        print()
