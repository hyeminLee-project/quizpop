# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project

QuizPop — a Python 3.11 project managed with uv (pyproject.toml, .python-version).

## Commands

- **Run**: `uv run main.py`
- **Add dependency**: `uv add <package>`
- **Sync environment**: `uv sync`

## Quiz Rules

### 출제 방식
- `progress.json`을 읽고 취약 개념(정답률 60% 미만) 위주로 출제
- 매일 10문제, 4지선다, 코드 실행 결과 맞추기 형식
- 틀리면 단계별 풀이를 표로 보여주고 핵심 포인트 설명
- 맞추면 다음 문제
- 10문제 완료 후 성적표 + progress.json 업데이트

### 난이도 상승
- 정답률 60% 이상 → 해당 개념 **심화 문제**로 전환
  - 예: 슬라이싱 초급(`nums[1:4]`) → 심화(`nums[-3::-1]`, 다차원)
  - 예: 함수 기본값 → 심화(mutable 기본값 함정, 클로저)
  - 예: 리스트 컴프리헨션 → 심화(이중 컴프리헨션, 중첩 조건)
- 정답률 100% + 2회 이상 → 취약 목록에서 제거, 새 개념 도입

### 진도 저장
- 퀴즈 완료 후 `progress.json`에 세션 결과, 개념별 정답률 업데이트
- 커밋 메시지: `📝 docs: Add Day N quiz results (X/10)`
