"""
리스트 컴프리헨션 #1 — Filter and Square (Easy)

숫자 리스트에서 짝수만 골라서 제곱한 리스트를 반환하세요.

예시:
  nums = [1, 2, 3, 4, 5]
  → 짝수: 2, 4
  → 제곱: 4, 16
  → 답: [4, 16]

힌트:
  - 리스트 컴프리헨션 구조: [변환 for x in 리스트 if 조건]
  - 짝수 확인: x % 2 == 0
  - 제곱: x ** 2
"""


def filter_and_square(nums):
    # 한 줄로 풀어보세요!
    pass


# --- 테스트 ---
if __name__ == "__main__":
    tests = [
        {"nums": [1, 2, 3, 4, 5], "expected": [4, 16]},
        {"nums": [10, 15, 20], "expected": [100, 400]},
        {"nums": [1, 3, 5], "expected": []},
        {"nums": [2], "expected": [4]},
    ]

    for i, t in enumerate(tests, 1):
        result = filter_and_square(t["nums"])
        status = "✅" if result == t["expected"] else "❌"
        print(f"테스트 {i}: {status}  입력: {t['nums']}")
        print(f"  기대값: {t['expected']}, 결과: {result}")
        print()
