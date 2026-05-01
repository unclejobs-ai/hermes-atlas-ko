# Hermes Atlas 한국어판

이 저장소는 https://hermesatlas.com 과 https://github.com/ksimback/hermes-ecosystem 를 기반으로 만든 Hermes Atlas 한국어판입니다.

## 목표

- Hermes Agent 생태계 지도를 한국어 사용자에게 읽히게 만들기
- 기존 정적 사이트/Vercel 배포 구조 유지
- 원본 데이터, API, RAG 챗봇, GitHub star 업데이트 구조 보존
- UI chrome, 주요 랜딩 문구, 카테고리, 검색/정렬/챗봇 문구를 한국어화

## 로컬 실행

정적 미리보기:

```bash
cd /Users/parkeungje/project/hermes-atlas-ko
python3 scripts/serve.py
```

브라우저에서 `http://localhost:4173` 접속.

Vercel 함수까지 확인하려면 Vercel CLI를 사용합니다.

```bash
npm install
npx vercel dev
```

## 배포

GitHub에 새 저장소로 push한 뒤 Vercel에서 import하면 됩니다.

```bash
gh repo create EungjePark/hermes-atlas-ko --public --source . --push --description "Korean localization of Hermes Atlas"
```

Vercel 환경 변수는 원본과 동일하게 설정합니다.

- `GITHUB_TOKEN`
- `OPENROUTER_API_KEY`
- Redis 관련 환경 변수, newsletter를 쓸 경우 beehiiv 관련 환경 변수

## 원본

- 사이트: https://hermesatlas.com/
- 저장소: https://github.com/ksimback/hermes-ecosystem

원본의 라이선스와 저작권 고지는 그대로 따릅니다.
