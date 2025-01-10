import asyncio
import logging
import sys
from aiogram import Bot, Dispatcher, types, F
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.filters import Command
from aiogram.types import Message, CallbackQuery
from config import BOT_TOKEN as Token
from button import *
bot = Bot(token='7756676755:AAFHrd1ZhwKtTRmWqZRJYTIf_bJv4S1DhFo', default=DefaultBotProperties(parse_mode=ParseMode.HTML))
dp = Dispatcher()

@dp.message(Command('start'))
async def StartCommand(message: Message):
    await message.answer_photo(photo="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSFEiQPXBHuiecjYKed51v-LUahBUTRyY4bCA&s",caption='Alphabet/한글' , reply_markup=menu)

@dp.message(F.data == "한글")
async def StartCommand(call:CallbackQuery):
    await call.message.answer_photo(photo="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSFEiQPXBHuiecjYKed51v-LUahBUTRyY4bCA&s",caption='Alphabet/한글' , reply_markup=menu)


@dp.message(F.data == "한글")
async def shop2(call:CallbackQuery):
    await call.message.answer_document(document="https://chatgpt.com/#:~:text=Koreyscha%20%27%E3%84%B1%27%20harfi,talaffuz%20qurish.%202.", reply_markup=maxx.as_markup())
    await call.message.delete()


@dp.callback_query(F.data == '비디오_레슨')
async def shop2(call:CallbackQuery):
    await call.message.answer_video(video="https://youtu.be/f3eyYpa13xk", caption="Vidio_Lessons/비디오_레슨", reply_markup=menu)
    await call.message.delete()


@dp.callback_query(F.data == '서적')
async def shop2(call:CallbackQuery):
    await call.message.answer_document(document="https://www.koreasociety.org/images/pdf/KoreanStudies/Monographs_LessonPlans/Elementary/3%20The%20Korean%20Alphabet.pdf", reply_markup=menu)
    await call.message.delete()


async def main():
    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())