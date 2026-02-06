# 띵동 텔레그램 봇

간단한 텔레그램 봇으로 `/띵동` 명령어에 재미있는 응답을 제공합니다.

## 기능

- `/start` - 봇 시작 및 인사
- `/띵동` - 랜덤 응답 메시지 전송

## 응답 메시지 목록

- 누구세요?
- @사용자명 벨누르지마
- @사용자명 너 그때 그 놈이지?
- 준식이 없다
- 피자 안시켰어요
- 옆집이에요

## 로컬 실행 방법

1. 의존성 설치:
```bash
pip install -r requirements.txt
```

2. 환경변수 설정:
```bash
cp .env.example .env
# .env 파일에 실제 봇 토큰 입력
```

3. 봇 실행:
```bash
export TELEGRAM_BOT_TOKEN="your_bot_token_here"
python bot.py
```

## Railway 배포 방법

1. Railway 프로젝트 생성
2. GitHub 저장소 연결 또는 직접 배포
3. 환경변수 설정:
   - `TELEGRAM_BOT_TOKEN`: BotFather로부터 받은 텔레그램 봇 토큰
4. 자동으로 배포됨

## 텔레그램 봇 토큰 받기

1. 텔레그램에서 [@BotFather](https://t.me/botfather) 검색
2. `/newbot` 명령어 실행
3. 봇 이름과 username 설정
4. 받은 토큰을 환경변수에 설정

## 기술 스택

- Python 3.11+
- python-telegram-bot 21.0.1
- Railway (배포 플랫폼)
