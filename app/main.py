from contextlib import asynccontextmanager
import logging

from dotenv import load_dotenv
from fastapi import FastAPI, HTTPException

load_dotenv()

from app.gemini_client import ReviewAnalyzer
from app.schemas import ReviewRequest, ReviewResponse


logger = logging.getLogger(__name__)

@asynccontextmanager
async def lifespan(app: FastAPI):
    
    try :
        app.state.analyzer = ReviewAnalyzer()
        logger.info("분석기 초기화 완료")
    except ValueError as e:
        logger.error("분석기 초기화 실패") 
        raise

    yield

    logger.info("서비스 종료 중...")


app = FastAPI(
    title="고객 리뷰 분석 API",
    description="Gemini LLM 기반 고객 리뷰 감성 분석 API",
    version="1.0.0",
    lifespan= lifespan
)

@app.get('/')
async def root():
    return {"message": "환영합니다! chatgpt 기반 고객 리뷰 분석 서비스입니다."}

@app.get('/health')
def health_check():
    return {"status" : "healthy"}

@app.post("/analyze", response_model= ReviewResponse)
def analyze_review(request : ReviewRequest):

    try:

        result = app.state.analyzer.analyze(request.review_text)
        return ReviewResponse(**result)
    
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))