"""
LeetCode #1 — Two Sum (Easy)

숫자 리스트에서 두 개를 골라 더하면 target이 되는 조합을 찾아라.
답은 두 숫자의 인덱스(위치)를 반환.

예시:
  nums = [2, 7, 11, 15], target = 9
  → 2 + 7 = 9 이니까 답은 [0, 1]

힌트:
  - for문 두 개로 모든 조합을 시도해보세요
  - nums[i] + nums[j] == target 이면 정답!
"""


def two_sum(nums, target):
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            print(f"검사 중: nums[{i}]={nums[i]} + nums[{j}]={nums[j]} == {target}?")
            if nums[i] + nums[j] == target:
                return [i, j]
        print(i, nums[i])

# --- 테스트 (건드리지 마세요) ---
if __name__ == "__main__":
    tests = [
        {"nums": [2, 7, 11, 15], "target": 9, "expected": [0, 1]},
        {"nums": [3, 2, 4], "target": 6, "expected": [1, 2]},
        {"nums": [3, 3], "target": 6, "expected": [0, 1]},
    ]

    for i, t in enumerate(tests, 1):
        result = two_sum(t["nums"], t["target"])
        status = "✅" if result == t["expected"] else "❌"
        print(f"테스트 {i}: {status}  입력: {t['nums']}, target={t['target']}")
        print(f"  기대값: {t['expected']}, 결과: {result}")
        print()
