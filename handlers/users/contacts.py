from aiogram import types
from aiogram.dispatcher import FSMContext
from states.gdeya import ContactState


from loader import dp, bot

@dp.message_handler(text = "Contact🚻")
async def stateshand(message:types.Message):
    await message.answer("Enter your phone : ")
    await ContactState.phone.set()
    
    
@dp.message_handler(state=ContactState.phone)
async def contact(message:types.Message, state: FSMContext):
    phone = message.text
    group_chat_id = -4049473709
    data = await state.get_data()
    await state.update_data({
        "phone" : phone
    })
    data = await state.get_data()
    await message.answer("Thank you for your information👌") 
    await message.answer("Admins will contact you as soon as possible !")
    await message.answer(f"Your phone is : {data['phone']}")
    full_name = message.from_user.full_name
    msg_to_admins = f"✔️Yangi mijozdan so'rov!!!\n📱 : {data['phone']}\nName : {full_name}" 
    await bot.send_message(chat_id = group_chat_id , text = msg_to_admins)
    await state.finish()
    await state.reset_data()
    
     
    
