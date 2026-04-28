"""
리스트 컴프리헨션 #2 — Word Lengths (Easy)

문자열 리스트에서 3글자 이상인 단어만 골라서
각 단어의 길이를 반환하세요.

예시:
  words = ["hi", "hello", "ok", "python"]
  → 3글자 이상: "hello", "python"
  → 길이: 5, 6
  → 답: [5, 6]

힌트:
  - 구조: [변환 for w in 리스트 if 조건]
  - 길이: len(w)
  - 조건: len(w) >= 3
"""


def word_lengths(words):
    # 한 줄로 풀어보세요!
    pass


# --- 테스트 ---
if __name__ == "__main__":
    tests = [
        {"words": ["hi", "hello", "ok", "python"], "expected": [5, 6]},
        {"words": ["a", "bb", "ccc", "dddd"], "expected": [3, 4]},
        {"words": ["yes", "no", "maybe"], "expected": [3, 5]},
        {"words": ["ab", "cd"], "expected": []},
    ]

    for i, t in enumerate(tests, 1):
        result = word_lengths(t["words"])
        status = "✅" if result == t["expected"] else "❌"
        print(f"테스트 {i}: {status}  입력: {t['words']}")
        print(f"  기대값: {t['expected']}, 결과: {result}")
        print()
