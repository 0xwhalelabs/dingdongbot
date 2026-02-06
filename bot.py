import os
import random
import logging
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes

# 로깅 설정
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)
logger = logging.getLogger(__name__)

# 띵동 명령어에 대한 응답 목록
DINGDONG_RESPONSES = [
    "누구세요?",
    "{username} 벨누르지마",
    "{username} 너 그때 그 놈이지?",
    "준식이 없다",
    "피자 안시켰어요",
    "옆집이에요"
]

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Start 명령어 핸들러"""
    await update.message.reply_text(
        '안녕하세요! !띵동 명령어를 사용해보세요!'
    )

async def dingdong(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """띵동 명령어 핸들러"""
    user = update.effective_user
    username = f"@{user.username}" if user.username else user.first_name
    
    # 랜덤으로 응답 선택
    response = random.choice(DINGDONG_RESPONSES)
    
    # {username}이 포함된 경우 실제 사용자 이름으로 대체
    response = response.format(username=username)
    
    await update.message.reply_text(response)

def main() -> None:
    """봇 실행"""
    # 환경변수에서 토큰 가져오기
    token = os.getenv('TELEGRAM_BOT_TOKEN')
    
    if not token:
        logger.error("TELEGRAM_BOT_TOKEN 환경변수가 설정되지 않았습니다!")
        return
    
    # Application 생성
    application = Application.builder().token(token).build()
    
    # 명령어 핸들러 등록
    application.add_handler(CommandHandler("start", start))
    application.add_handler(MessageHandler(filters.Regex(r'^!띵동$'), dingdong))
    
    # 봇 시작
    logger.info("봇이 시작되었습니다...")
    application.run_polling(allowed_updates=Update.ALL_TYPES)

if __name__ == '__main__':
    main()
