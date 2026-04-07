# 고객 리뷰 분석 API

OpenAI GPT 기반 고객 리뷰 감성 분석 REST API 서버

## 기능

- 고객 리뷰 텍스트의 감성 분석 (긍정/부정/중립)
- 리뷰 카테고리 분류 (배송, 품질, 가격, 고객서비스, 기타)
- 리뷰 요약 및 신뢰도 점수 제공

## 설치

```bash
pip install -r requirements.txt
```

## 환경 변수

`.env` 파일을 프로젝트 루트에 생성:

```
OPENAI_API_KEY=your-api-key
```

## 실행

```bash
uvicorn app.main:app --reload --port 8001
```

## API 엔드포인트

| 메서드 | 경로 | 설명 |
|--------|------|------|
| GET | `/health` | 헬스체크 |
| POST | `/analyze` | 리뷰 분석 |

### POST /analyze 요청 예시

```json
{
  "review_text": "이 제품 정말 좋아요! 배송도 빠르고 품질이 우수합니다."
}
```

### 응답 예시

```json
{
  "sentiment": "긍정",
  "category": "품질",
  "summary": "제품 품질과 배송 속도에 대한 만족을 표현한 리뷰",
  "confidence": 0.95
}
```

## API 문서

서버 실행 후 `http://localhost:8001/docs`에서 Swagger UI 확인 가능
