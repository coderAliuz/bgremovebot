from aiogram.types import Message
from config import dp
from aiogram.dispatcher import FSMContext
from utils import bgremove_def
import os

@dp.message_handler(commands="start",state="*")
async def start(message:Message,state:FSMContext):
    await message.answer(f"Salom {message.chat.full_name}.\nMenga rasm yubor men orqa fonini olib tashlayman")
    await state.set_state("image")


@dp.message_handler(content_types="photo",state="image")
async def get_photo(message:Message,state:FSMContext):
    await state.set_state("other")
    await message.reply("⌛️")
    await message.photo[-1].download(destination_file=f"files/{message.chat.id}.jpg")
    if bgremove_def(message.chat.id):
        await message.answer_photo(photo=open(f"files/{message.chat.id}.png","rb"))
    else:
        await message.answer("Rasmni orqa fonini olib tashlab bo'lmadi")
    try:
        os.remove(f"files/{message.chat.id}.jpg")
        os.remove(f"files/{message.chat.id}.png")
    except:print("xato")
    await state.set_state("image")

