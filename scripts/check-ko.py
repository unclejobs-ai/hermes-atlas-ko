#!/usr/bin/env python3
from pathlib import Path
import sys
root = Path(__file__).resolve().parents[1]
index = (root / "index.html").read_text(encoding="utf-8")
required = [
    '<html lang="ko">',
    '커뮤니티 생태계 지도',
    'Atlas에게 질문',
    '큐레이션 목록',
    '저장소 검색',
    '코어 &amp; 공식',
]
missing = [s for s in required if s not in index]
if missing:
    print('FAIL missing:', missing)
    sys.exit(1)
print('OK: Korean localization smoke check passed')
