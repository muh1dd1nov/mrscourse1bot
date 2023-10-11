from aiogram import types
from keyboards.default.mainkey import get_start_button, get_course1_button , get_course2_button,get_course3_button,get_course4_button
from states.coursesss import CoursesState
from aiogram.dispatcher import FSMContext
from loader import dp , bot
from datetime import datetime


@dp.message_handler(text = "Courses📒")
async def bot_start(message: types.Message):
    await message.answer("Choose Courses📒 !", reply_markup=get_course1_button())
    await CoursesState.courses.set()

@dp.message_handler(state = CoursesState.courses)
async def bot_start(message: types.Message, state:FSMContext):
    course = message.text
    await state.update_data({
        "courses" : course
    })
    if course == "Design🖌️":
     repl_mark = get_course2_button()
    elif course == "Programming🗿💻":
        repl_mark = get_course3_button()
    elif course ==  "Starter📗":
        repl_mark = get_course4_button()  
    await message.answer("Choose course items !",reply_markup=repl_mark)
    await CoursesState.items.set()
    


    
@dp.callback_query_handler(state = CoursesState.items)
async def get_course_items(call: types.CallbackQuery, state:FSMContext):
    items = call.data
    await state.update_data({
        "items" : items
        })
    await call.message.answer("Choose clients for IT !")
    await CoursesState.clients.set()
    
@dp.message_handler(state= CoursesState.clients)
async def get_clients(message : types.Message , state:FSMContext):
    group_chat_id = -4049473709
    now = datetime.now()
    client = message.text
    course_price = 1090000
    await state.update_data({
        "clients" : client
    })
    data = await state.get_data()
    total_price = int(data['clients']) * course_price
    formatted_price = format(total_price, ",")
    await message.answer("THANKS FOR YOUR ATTENTION👌")
    await message.answer (f"Your course is :{data['courses']}\nYour courses items is :{data['items']}\nYour clients is : {data['clients']}")
    msg_to_admins = f"""
    Time : {now.date()} -{now.time()}
    User name : @{message.from_user.username}
    Course : {data['courses']}
    CourseItems : {data['items'].split("_")[0]}
    Number of Children : {data['clients']}
    Money : {formatted_price}
    """
    await bot.send_message(chat_id = group_chat_id , text = msg_to_admins)
    await state.finish()
    await state.reset_data()
 
# @dp.message_handler(text = "Design🖌️")
# async def get_disign(message:types.Message):
#     await message.answer("Design tanlang !", reply_markup=get_course2_button())
    
# @dp.message_handler(text = "Programming🗿💻")
# async def get_disign(message:types.Message):
#     await message.answer("Pro course tanlang  !", reply_markup=get_course3_button())    
    
# @dp.message_handler(text = "Starter📗")
# async def get_disign(message:types.Message):
#     await message.answer("Starter course tanlang  !", reply_markup=get_course4_button())   
    

@dp.message_handler(text = "Back🔙")
async def get_disign(message:types.Message):
    await message.answer("Back", reply_markup=get_start_button())    
    
    
    
@dp.callback_query_handler(text = "3D____course") 
async def get3d(call:types.CallbackQuery):
    await call.message.answer("Siz 3d kurslarini tanladingiz")
    
    
@dp.callback_query_handler(text = "Grafic___course") 
async def get3d(call:types.CallbackQuery):
    await call.message.answer("Siz Grafic kurslarini tanladingiz")
     
     

@dp.callback_query_handler(text = "motion___course") 
async def get3d(call:types.CallbackQuery):
    await call.message.answer("Siz Motion kurslarini tanladingiz")



@dp.callback_query_handler(text = "frontend____course") 
async def get3d(call:types.CallbackQuery):
    await call.message.answer("Siz Front-End kurslarini tanladingiz,About Front-End : Front-end dasturchi - bu veb-saytlar va veb-ilovalarning foydalanuvchi interfeysi (UI) va foydalanuvchi tajribasini (UX) yaratish va loyihalashga ixtisoslashgan dasturiy ta'minot ishlab chiqaruvchisi. Front-end dasturchining asosiy mas'uliyati veb-sayt yoki ilovaning vizual va interaktiv jihatlari foydalanuvchilarga qulay, estetik jihatdan yoqimli va funktsional jihatdan samarali bo'lishini ta'minlashdir.")
    
    
    
@dp.callback_query_handler(text = "backend___course") 
async def get3d(call:types.CallbackQuery):
    await call.message.answer("Siz Back-End kurslarinni tanladingiz, About Back - End : Orqa tomon dasturiy ta'minot yoki apparatning ma'lumotlarga kirish qatlami deb ham ataladi va raqamli vositalar orqali kirish va harakatlanish kerak bo'lgan har qanday funksiyani o'z ichiga oladi. Orqa tomonning ustidagi qatlam old tomon bo'lib, u foydalanuvchi interfeysining bir qismi bo'lgan barcha dasturiy ta'minot yoki uskunani o'z ichiga oladi.")
    


@dp.callback_query_handler(text = "8-12____course") 
async def get3d(call:types.CallbackQuery):
    await call.message.answer("Siz Starter 8-12 kurslarinni tanladingiz,ABout starter 8-12 : Yangi boshlanuvchilar uchun o'rganish uchun mos bo'lgan eng oddiy dasturlash tillari Python va JavaScript hisoblanadi. Ular oson sintaksisga ega va ularning yordami bilan oddiy dastur yaratish oson. Dasturlash ko'nikmalariga ega bo'lganlar uchun juda oddiy tillar - PHP, Swift va Kotlin.")
    
    
    
@dp.callback_query_handler(text = "12-16___course") 
async def get3d(call:types.CallbackQuery):
    await call.message.answer("Siz Starter 12-16 kurslarinni tanladingiz, About starter 12-16 : Yangi boshlanuvchilar uchun o'rganish uchun mos bo'lgan eng oddiy dasturlash tillari Python va JavaScript hisoblanadi. Ular oson sintaksisga ega va ularning yordami bilan oddiy dastur yaratish oson. Dasturlash ko'nikmalariga ega bo'lganlar uchun juda oddiy tillar - PHP, Swift va Kotlin.")
    
    
    
@dp.callback_query_handler(text = "intensive____course") 
async def get3d(call:types.CallbackQuery):
    await call.message.answer("Siz Starter Intensive kurslarinni tanladingiz, About starter Intensive : Yangi boshlanuvchilar uchun o'rganish uchun mos bo'lgan eng oddiy dasturlash tillari Python va JavaScript hisoblanadi. Ular oson sintaksisga ega va ularning yordami bilan oddiy dastur yaratish oson. Dasturlash ko'nikmalariga ega bo'lganlar uchun juda oddiy tillar - PHP, Swift va Kotlin.")
    
    
# @dp.message_handler(text = "Courses📒") 
# async def get_course(message:types.Message):
#     await message.answer("Select Courses📒 :")
#     await CoursesState.courses.set()
    
# @dp.message_handler(state=CoursesState.courses)
# async def contact(message:types.Message, state: FSMContext):
#     courses = message.text
#     data = await state.get_data()
#     await state.update_data({
#         "courses" : courses
#     })
    
#     await message.answer("Thanks✊\nSelect a courseItems :")
#     await CoursesState.items.set()
    
    
    
# @dp.message_handler(state=CoursesState.items)
# async def contact(message:types.Message, state: FSMContext):
#     items = message.text
#     data = await state.get_data()
#     await state.update_data({
#         "items" : items
#     })
    
#     await message.answer("Thanks✊\nEnter how many children do you teach in your Mars IT Schoool :")
#     await CoursesState.clients.set()
    
    
# @dp.message_handler(state=CoursesState.clients)
# async def contact(message:types.Message, state: FSMContext):
#     clients = message.text
#     group_chat_id = -4049473709
#     data = await state.get_data()
#     await state.update_data({
#         "clients" : clients
#     })
#     data = await state.get_data()
#     await message.answer("Thank you for your information👌") 
#     await message.answer("Admins will contact you as soon as possible !")
#     await message.answer(f"Your Courses is : {data['courses']}\nYour CoursesItems is : {data['items']}\nYour NumOfCHildren is : {data['clients']}")
#     full_name = message.from_user.full_name
#     msg_to_admins = f"✔️Yangi mijozdan so'rov!!!\n📱 : {data['phone']}\nName : {full_name}\n Courses is : {data['courses']}\nCoursesItems is : {data['items']}\nNumOfCHildren is : {data['clients']}" 
#     await bot.send_message(chat_id = group_chat_id , text = msg_to_admins)
#     await state.finish()
#     await state.reset_data()
    