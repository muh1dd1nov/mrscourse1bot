from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart
from keyboards.default.mainkey import get_start_button



from loader import dp
admin_id = 754390348

 
@dp.message_handler(CommandStart(),user_id = 754390348)
async def bot_start(message: types.Message):
    photo = "https://avatars.mds.yandex.net/get-altay/998620/2a00000185bedb0cfe606686bf9d0f3c6bac/L_height"  
    await message.answer_photo(photo=photo, caption="Welcome to Mars IT School", reply_markup=get_start_button())  
    


@dp.message_handler(text = "Back")
async def bot_start(message: types.Message):
    photo = "https://avatars.mds.yandex.net/get-altay/998620/2a00000185bedb0cfe606686bf9d0f3c6bac/L_height"
    await message.answer_photo(photo=photo, caption="Welcome to Mars IT School", reply_markup=get_start_button())
    
    
    


# @dp.message_handler(text = "Contact")
# async def get_details(message: types.Message): 
#     await message.answer("Enter a yourName :")
#     await COntact.name.set()
    
    
# @dp.message_handler(state=COntact.name)
# async def get_num1(message: types.Message, state: FSMContext):
#     name = message.text
#     await state.update_data({  
#         "name": name
#     })  
#     await message.answer("Thanks!\n Enter your age :")
#     await COntact.age.set()



# @dp.message_handler(state=COntact.age)
# async def get_opp(message: types.Message, state: FSMContext):
#     age = message.text
#     data = await state.get_data()
#     await state.update_data({
#         "age": age
#     })
#     await message.answer("Thanks!\n Enter your TelNumber :")
#     await COntact.phone.set()   
    
    
# @dp.message_handler(state=COntact.phone)
# async def get_num2(message: types.Message, state: FSMContext):
#     phone = message.text
#     data = await state.get_data()
#     await state.update_data({
#         "phone": phone
#     })
#     await message.answer("Thanks for your attention and information !👌")
#     data = await state.get_data()
#     name = data.get('name')
#     age = data.get('age')
#     phone = data.get('phone')
    
    
    
    
#     msg = f"Your Name is: {name}\n Your AGE is: {age}\n Your Phone is: {phone}"
#     await message.answer(msg)
#     await state.finish()
#     await state.reset_data()