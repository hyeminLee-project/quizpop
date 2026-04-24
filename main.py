import json
from pathlib import Path

PROGRESS_FILE = Path(__file__).parent / "progress.json"


def load_progress():
    if PROGRESS_FILE.exists():
        return json.loads(PROGRESS_FILE.read_text(encoding="utf-8"))
    return {
        "user": "hyemin",
        "total_quizzes": 0,
        "total_correct": 0,
        "sessions": [],
        "concept_stats": {},
        "weak_concepts": [],
    }


def save_progress(progress):
    PROGRESS_FILE.write_text(
        json.dumps(progress, ensure_ascii=False, indent=2), encoding="utf-8"
    )


def update_progress(progress, concept, is_correct):
    stats = progress.setdefault("concept_stats", {})
    if concept not in stats:
        stats[concept] = {"attempts": 0, "correct": 0, "rate": 0.0}
    stats[concept]["attempts"] += 1
    if is_correct:
        stats[concept]["correct"] += 1
    stats[concept]["rate"] = round(
        stats[concept]["correct"] / stats[concept]["attempts"], 2
    )
    progress["weak_concepts"] = [
        c for c, s in stats.items() if s["rate"] < 0.6
    ]


def show_weak_concepts(progress):
    weak = progress.get("weak_concepts", [])
    if not weak:
        print("\n취약 개념이 없습니다! 잘하고 있어요.")
        return
    print("\n📊 취약 개념 (정답률 60% 미만):")
    stats = progress.get("concept_stats", {})
    for concept in weak:
        s = stats[concept]
        bar = "❌" * (s["attempts"] - s["correct"]) + "✅" * s["correct"]
        print(f"  - {concept}: {s['rate']*100:.0f}% ({s['correct']}/{s['attempts']}) {bar}")


def show_stats(progress):
    total = progress.get("total_quizzes", 0)
    correct = progress.get("total_correct", 0)
    if total == 0:
        print("\n아직 푼 문제가 없습니다.")
        return
    rate = correct / total * 100
    print(f"\n📈 전체 성적: {correct}/{total} ({rate:.0f}%)")
    print(f"📅 세션 수: {len(progress.get('sessions', []))}")
    show_weak_concepts(progress)


def main():
    progress = load_progress()
    print("=" * 40)
    print("  🎯 QuizPop - 파이썬 퀴즈")
    print("=" * 40)
    print("\n명령어:")
    print("  stats  - 성적 확인")
    print("  weak   - 취약 개념 보기")
    print("  quit   - 종료\n")

    show_stats(progress)

    while True:
        cmd = input("\n> ").strip().lower()
        if cmd in ("quit", "q", "exit"):
            save_progress(progress)
            print("진도가 저장되었습니다. 다음에 또 만나요!")
            break
        elif cmd == "stats":
            show_stats(progress)
        elif cmd == "weak":
            show_weak_concepts(progress)
        else:
            print("알 수 없는 명령어입니다. (stats / weak / quit)")


if __name__ == "__main__":
    main()
