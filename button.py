from aiogram.types import InlineKeyboardButton,InlineKeyboardMarkup
from aiogram.utils.keyboard import InlineKeyboardBuilder
menu=InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="Alphabet/한글", 
callback_data='한글')],
        [InlineKeyboardButton(text="Vidio_Lessons/비디오_레슨",
callback_data='비디오_레슨')],
        [InlineKeyboardButton(text="Books/서적",
callback_data='서적')],
    ], 
)
maxx=["ㄱ", "ㄴ", "ㄷ", "ㄹ", "ㅁ", "ㅂ", "ㅅ", "ㅇ", "ㅈ", "ㅊ", "ㅋ", "ㅌ", "ㅍ", "ㅎ", "ㅂㅂ", "ㅈㅈ", "ㄷㄷ", "ㄱㄱ", "ㅅㅅ", "ㅏ", "ㅑ", "ㅓ", "ㅕ", "ㅗ", "ㅛ", "ㅜ", "ㅠ", "ㅡ", "ㅣ", "ㅐ", "ㅔ"]
harflar=InlineKeyboardBuilder()
for i in maxx:
    harflar.button(text=f'{i}',callback_data=f'{i}')
harflar.adjust(2)