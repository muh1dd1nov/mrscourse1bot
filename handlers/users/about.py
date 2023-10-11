from aiogram import types

from loader import dp


@dp.message_handler(text = "About us🗣")
async def aboutus(message: types.Message):
   photo = "https://avatars.mds.yandex.net/get-altay/927916/2a00000185bedb2a15156f16141730efa685/L_height"
   msg = """
    <a href='https://marsit.uz'>Mars IT School</a>, O'zbekistondagi bolalar ta'lim muassasalari orasida yetakchi o’quv markazi."""

   await message.answer_photo(photo=photo)
   await message.answer(text=msg)

    
    