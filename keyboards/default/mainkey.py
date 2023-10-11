import requests
from aiogram.types import( ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup,InlineKeyboardButton)

def get_start_button():
    states_button = ReplyKeyboardMarkup(
        [
            [
                KeyboardButton(text="Contact🚻"),
                KeyboardButton(text = "Courses📒")
            ],
            [
                KeyboardButton(text="About us🗣")
            ],
        ],
        resize_keyboard=True
    )
    return states_button



def get_course1_button():
    course_button = ReplyKeyboardMarkup(
        [
            [
                KeyboardButton(text="Design🖌️"),
                KeyboardButton(text="Programming🗿💻")
            ],
            [
                KeyboardButton(text="Starter📗")
            ],
            [
              KeyboardButton(text="Back🔙")  
            ],
            
        ],
        resize_keyboard=True
    )
    return course_button 

def get_course2_button():
    cours2_button = InlineKeyboardMarkup(
       inline_keyboard= [
            [
                InlineKeyboardButton(text="3D", callback_data = "3D____course"),
                InlineKeyboardButton(text="Grafic", callback_data="Grafic___course")
            ],
            [
                InlineKeyboardButton(text="Motion", callback_data="motion___course")
            ],
        ],
    )
    return cours2_button




def get_course3_button():
    cours2_button = InlineKeyboardMarkup(
       inline_keyboard= [
            [
                InlineKeyboardButton(text="Front-End", callback_data = "frontend____course"),
                InlineKeyboardButton(text="Back-End", callback_data="backend___course")
            ],
        ],
    )
    return cours2_button




def get_course4_button():
    cours2_button = InlineKeyboardMarkup(
       inline_keyboard= [
            [
                InlineKeyboardButton(text="Starter 8-12", callback_data = "8-12____course"),
                InlineKeyboardButton(text="Starter 12-16", callback_data="12-16___course")
            ],
            [
                
                InlineKeyboardButton(text="Intensive", callback_data = "intensive____course"),
            ],
        ],
    )
    return cours2_button