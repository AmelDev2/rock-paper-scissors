# مشروع حجرة، ورقة، مقص


import random

# بداية اللوب
while True:
 
 choices = {'r':'r'          
 ,'rock':'r',
 'p':'p',
 'paper':'p',
 's':'s',
 'scissors':'s' }
 
#  المستخدم يدخل الاختيار
 user = input("Choose one to start the game ('r' for Rock, 'p' for Paper, 's' for Scissors): ").strip()
 user_input = user.lower().strip()


# التحقق من صحة الإدخال
 if user_input not in choices:
    print("Error: Invalid choice. Please select 'r' or Rock, 'p' or Paper, 's' or Scissors.\n")
    continue
   
 
 user_choice = choices[user_input]

# اختيار الكمبيوتر عشوائيًا
 computer_choice = random.choice(['r' , 'p', 's'])


# ضبط  اختيار الكمبيوتر حسب شكل اختيار إدخال المستخدم
 if user[0].isupper():
   pc_display={'r':'Rock','p':'Paper','s':'Scissors'}

 else:
   pc_display={'r':'rock','p':'paper','s':'scissors'}   

 computer_display = pc_display[computer_choice]



# عرض اختيارات الطرفين

 print(f"the choice of the user is: {user}")
 print(f"the choice of the pc is : {computer_display}")



# تحديد الفائز
 if user_choice == computer_choice:
   print("It's a tie!\n")

 elif (user_choice == 'p' and computer_choice == 'r')  or (user_choice == 's' and computer_choice == 'p') or (user_choice == 'r' and computer_choice == 's'):
   print("You win! Great job!\n")

 else:
   print("You lost. Better luck next time! :( \n ")  




 # سؤال هل يريد اللاعب إعادة اللعب
 ask = input("Would you like to play again? (Yes or No): ").lower().strip()

 if ask in ["n","no"]:
   print("Goodbye! Thanks for playing. Have a great day!")
   break
 


 