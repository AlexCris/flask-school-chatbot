#������� ������ ���� ��� ������
#�����������! �� ������ ����� �������, ��������� ���� � ������� �� ��������.
import telebot
from telebot import types
TOKEN = '362352422:AAGKyG6HLhrYrDBe1MGDC3UKKHC_lfWWOUo'
bot = telebot.TeleBot(TOKEN)
@bot.message_handler(commands=['start'])
# ��������� �������
def start(m):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.add(*[types.KeyboardButton(name) for name in ['������','������', '��', '���������', '�������', '�����������', '���', '���','������','�����������','�����','��������']])
    msg = bot.send_message(m.chat.id, '�����������! ���� ������ ������ � ������ �� ���� - ������ ������. ���� ������� ������ ������ ������ - ������.',
        reply_markup=keyboard)
    bot.register_next_step_handler(msg, name)
# �� ������ ��������� ����� ������, � �� ���!
# ������� - ��������
def name(m):
    if m.text == '������':
        g = bot.send_message(m.chat.id, '�����������!\n������� ����, ���� ����� ��� � ������ � ������ �������� � ����.\n� ������������������ ���-��� �������� ��� ����������, ������� ���� ���������� ���� ����� ���������� � ������ ���������� �� ����������� �������� ��������.\n������������� � ���� ���� ������������ ����������� ������,������� � �������������, �������� ������� � ������ ������.\n����� � ���� ������ ����������, �� ������ ������ �������� ������� ��� � ���������.\n���� �� ������ ������ ��� ��� ������� - ������ "������".\n� ���� �� ������� ����� ���������� ���������� ( ��� ���� �������� ), �� ������ ��� ������ ��������� � ������ - https://vk.com/10schoolbot10\n�� ����� ������!', parse_mode='Markdown') 
    elif m.text == '���':
        g = bot.send_message(m.chat.id, '�����������!\n��� ������ (�������� ������, ���������) � 101\n������� � 102\n������ ����������� ������ � 103\n��������� ������� ������ - 104\n������ ������ �������� � 112\n���� ����� - http://severschool10.ru/\n��������� - https://51gosuslugi.ru/rpeu/', parse_mode='Markdown') 
    elif m.text == '��������':
        g = bot.send_message(m.chat.id, '����\n������ �������\n����� - 25 ������\n������� � ����������, ��������, ����� � �����, �����, ���������, �������, ������� - 15 ������\n������� � ����� - 25 ������\n������\n��������; � ����������, ��������� � ����� - 35 ������\n� ��������, ����� � �������; ������ - 45 ������\n����\n����, ����������, ������ � �.�. - 40 ������(������� �� ��� ������)\n�������\n������� ������ � ������, ������� � �.� - 60 ������(������� �� ��� ������)\n�������\n��� - 5 ������\n��� � ������� - 7 ������\n��� - 15 ������\n������ � ������ - 15 ������\n��������\n��������� � ���� ������ ��������, ���, �����, ������� - 70 ������(������� �� ��� ������)', parse_mode='Markdown') 
    elif m.text == '�����':
        g = bot.send_message(m.chat.id, '�����������!\n������ ������� - 1 �������, ������ - 2\n1 ���\n1 �����\n�������� �. , �������� �.\n2 �����\n������������� �. , ����������� �.\n3 �����\n������������� �. , ������  �.\n4 ����� ������ �. , ������� �.\n 5 �����\n�������� �. , ������ �.\n2 ���\n1 �����\n������ �. , ��� �.\n2 �����\n������� �. , �������� �.\n3 �����\n����� �. , ������� �.\n4 �����\n�������� �. , �������� �.\n5 �����\n������������ �. , ��������� �.\n6 �����\n������ �. , ��������� �.\n3 ���\n1 �����\n������ �. , ����� �.\n2 �����\n������� �. , ��������� �.\n3 �����\n������ �. , �������� �.\n4 �����\n������������� �. , ����� �.\n6 �����\n������� �. , ������� �.' , parse_mode='Markdown') 
    elif m.text == '������':
        g = bot.send_message(m.chat.id, '�����������!\n�������� ��������� - http://multa.ch/\n������ - http://scanvord.net/sudoku/\n2048 - http://2048game.com/ru/\n������� - https://www.chess.com/ru/play/computer\n����� - http://www.shashky.ru/', parse_mode='Markdown') 
    elif m.text == '�����������':
        g = bot.send_message(m.chat.id, '����������� �� �����������:\n����������� - 5 ����\n����� - 7 ����', parse_mode='Markdown')    
    elif m.text == '������':
        g = bot.send_message(m.chat.id, '������ - �������� ����������� � �������������� ����\n��������� - ����� ��������������� ���������\n����������� - ����� ��������������� ������������\n���� - ����� ���� �� ������� � �������� ��������.\n����� - ����� �� ����� ����� � ����� �������� ����� ������.\n������� - ������ ������ ��������\n������ - ������ ������ ������\n����������� - ����� ��������������� �����������\n�� - ����� �������� �������\n��� - ����� ���������� �� ���\n������ - ���������� � ���\n��� - ������ ������ ������', parse_mode='Markdown')
    elif m.text == '��':
        g = bot.send_message(m.chat.id, '������', parse_mode='Markdown')
    elif m.text == '���������':
        g = bot.send_message(m.chat.id, '20.11.2017 - ����������, ������.\n21.11.2017 - ��������������.\n22.11.2017 - ����������.\n23.11.2017 - ��������, ����������� � ���.\n24.11.2017 - ������� ����.\n25.11.2017 - ����������� ����, ���������.\n27.11.2017 - ���������� ����(������������� ���).\n28.11.2017 - ���������� ����(����������� ���).\n29.11.2017 - ����������, �������.\n30.11.2017 - �������� ����, �����.\n01.12.2017 - ���, �����.\n07.12.2017 - ��������, ����������(������������� ����).\n08.12.2017 - ��������, ����������(������������ ����).', parse_mode='Markdown')
    elif m.text == '�������':
        g = bot.send_message(m.chat.id, '������� ��.; ����������  - ������� ����� ����������\n���������� - ������ �������� ������������\n������ - �������� �������� ����������\n����� - �������� �������� ����������\n����������� - ������� ������� �������������\n�������; �������������� - �������� ����� ��������\n�������� - ���������� ���� ���������\n�������� - ������� ������ ����������\n���������� ��. - �������� ����� ����������\n����������� - ��������� ������ ���������\n������  - �������� ���� ����������\n��� - ������� �������� ������������', parse_mode='Markdown')
    elif m.text == '�����������':
        g = bot.send_message(m.chat.id, '�� ������ ������ ����������� �� �������������', parse_mode='Markdown')
    elif m.text == '���':
        g = bot.send_message(m.chat.id, '���� ��� - https://ege.sdamgia.ru/\n������ ��� - https://ege.yandex.ru/ege/\n�������� ���������� - http://www.ege.edu.ru/ru/main/', parse_mode='Markdown')
    bot.register_next_step_handler(g, name)    
bot.polling()
# �����������!!! �� ������ �������� ���-���� � �������� ������

#������� ���������� �������
#def get_time_before_ring(time_now):
    #key_day, lesson_now, is_time_change = get_lesson_number(time_now)
    #if lesson_now == 'before':
        #td_first_lesson = timedelta(
            #hours=TIMETABLE[key_day][SHIFT][0][1].hour,
            #minutes=TIMETABLE[key_day][SHIFT][0][1].minute)
        #minute_before = td_first_lesson - time_now.td
        #message = '����� ��� �� ��������, �� ������ {0}:{1}'.\
                  #format(minute_before.seconds//3600,
                         #str(minute_before.seconds%3600//60).zfill(2))
    #elif lesson_now == 'after':
        #td_last_lesson = timedelta(
            #hours=TIMETABLE[key_day][SHIFT][-1][2].hour,
            #minutes=TIMETABLE[key_day][SHIFT][-1][2].minute)
        #minute_before = time_now.td - td_last_lesson
        #message = '����� ��� ������. {0} ���������� {1}:{2} �����'.\
                  #format(TIMETABLE[key_day][SHIFT][-1][0],
                         #minute_before.seconds//3600,
                         #str(minute_before.seconds%3600//60).zfill(2))
    #else:
        #if is_time_change:
            #next_lesson = TIMETABLE[key_day][SHIFT][lesson_now + 1]
            #td_next_lesson_beg = timedelta(
                #hours=next_lesson[1].hour,
                #minutes=next_lesson[1].minute)
            #minute_before = td_next_lesson_beg - time_now.td
            #message = '{} ��������. ��������, �� ������ {} �����'.\
                      #format(TIMETABLE[key_day][SHIFT][lesson_now][0],
                             #minute_before.seconds//60)
        #else:
            #td_lesson_end = timedelta(
                #hours=TIMETABLE[key_day][SHIFT][lesson_now][2].hour,
                #minutes=TIMETABLE[key_day][SHIFT][lesson_now][2].minute)
            #minute_before = td_lesson_end - time_now.td
            #message = '��� "{}", �� ������ {} �����'.\
                      #format(TIMETABLE[key_day][SHIFT][lesson_now][0].title(),
                             #minute_before.seconds//60)
    #return message


#def get_daily_timetable(time_now, day):
   #if day == time_now.week_day:
      #key_day, lesson_now, is_time_change = get_lesson_number(time_now)
   #else:
      #lesson_now = None
   #for key_day in TIMETABLE:
      #if day in key_day:
         #message = DAYS_NAME[day].upper() + '\n'
         #if lesson_now == 'before':
            #message += '������ {0:%H}:{0:%M}\n'.format(time_now.time)
         #for n, lesson in enumerate(TIMETABLE[key_day][SHIFT]):
             #message += '{0}: {1:%H}:{1:%M} - {2:%H}:{2:%M}\n'.\
                        #format(lesson[0], lesson[1], lesson[2])
             #if lesson_now == n:
                #if is_time_change:
                   #message += '������ {0:%H}:{0:%M}\n'.format(time_now.time)
                #else:
                   #message = message[:-1] + \
                             #', ������ {0:%H}:{0:%M}\n'.format(time_now.time)
         #if lesson_now == 'after':
            #message += '������ {0:%H}:{0:%M}\n'.format(time_now.time)
   #return message


#def get_timetable(keyword=''):
   #time_now = TimeNow()
   #if keyword in keyword_gen('������ �������','������ �� �������','�������'):
      #message = get_daily_timetable(time_now, time_now.week_day)
   #elif keyword in keyword_gen('������ ������','������ �� ������','�������'):
      #message = get_daily_timetable(time_now, time_now.week_day+1)
   #elif keyword in keyword_gen('������ �����', '������ �� �����', '�������'):
      #message = get_daily_timetable(time_now, time_now.week_day-1)
   #elif keyword in keyword_gen('������ �����������','������ �� �����������','������'):
      #message = get_daily_timetable(time_now, 0)
   #elif keyword in keyword_gen('������ �������','������ �� �������','������'):
      #message = get_daily_timetable(time_now, 1)
   #elif keyword in keyword_gen('������ �����','������ �� �����','������'):
      #message = get_daily_timetable(time_now, 2)
   #elif keyword in keyword_gen('������ �������','������ �� �������','������'):
      #message = get_daily_timetable(time_now, 3)
   #elif keyword in keyword_gen('������ �������','������ �� �������','������'):
      #message = get_daily_timetable(time_now, 4)
   #elif keyword in keyword_gen('������ �������','������ �� �������','������'):
      #message = get_daily_timetable(time_now, 5)
   #elif keyword in keyword_gen('������ �����������','������ �� ������������','������'):
      #message = get_daily_timetable(time_now, 6)
   #else:
      #message = get_time_before_ring(time_now)
   #return message, ''


#timetable_command = command_system.Command()
#timetable_command.keys =  keyword_gen('������','�� ������','����', 'pdjyjr',
                                     #'������ �������','������ �� �������','�������','pdjyrb yf ctujlyz',
                                     #'������ ������','������ �� ������','�������', 'pdjyrb yf pfdnhf',
                                     #'������ �����', '������ �� �����', '�������', 'pdjyrb yf dxthf',
                                     #'������ �����������','������ �� �����������','������', 'pdjyrb yf gjytltkmybr',
                                     #'������ �������','������ �� �������','������', 'pdjyrb yf dnjhybr',
                                     #'������ �����','������ �� �����','������', 'pdjyrb yf chtle',
                                     #'������ �������','������ �� �������','������', 'pdjyrb yf xtndthu',
                                     #'������ �������','������ �� �������','������', 'pdjyrb yf gznybwe',
                                     #'������ �������','������ �� �������','������', 'pdjyrb yf ce,,jne',
                                     #'������ �����������','������ �� ������������','������','pdjyrb yf pfdnhf')
#timetable_command.description = '''����� ���������� ������� �� �����/�������/������/��/��/��/��/��/��/��, ���� ������� �������� �� ������'''
#timetable_command.process = get_timetable
#����������
#def get_daily_schedule(week_day):
    #lessons = DAYS_NAME[week_day].upper() + ':\n'
    #for lesson in SCHEDULE[week_day]:
        #subject = "�����" if lesson[1] == '' else lesson[1]
        #lessons += '{}. {}\n'.format(lesson[0], subject)
    #return lessons

#def get_schedule(keyword=''):
    #time_now = TimeNow()
    #if keyword in keyword_gen('����������','����'):
        #message = '\n\n'.join([get_daily_schedule(week_day) for week_day in range(7)])
    #elif keyword in keyword_gen('���������� �� �������', '���������� �������', '�������'):
        #message = get_daily_schedule(time_now.week_day)
    #elif keyword in keyword_gen('���������� �� ������','���������� ������','�������'):
        #message = get_daily_schedule((time_now.week_day + 1) % 7)
    #elif keyword in keyword_gen('���������� �� �����','���������� �����','�������'):
        #message = get_daily_schedule((time_now.week_day - 1) % 7)
    #elif keyword in keyword_gen('���������� �� �����������','���������� �����������','������'):
        #message = get_daily_schedule(0)
    #elif keyword in keyword_gen('���������� �� �������','���������� �������','������'):
        #message = get_daily_schedule(1)
    #elif keyword in keyword_gen('���������� �� �����','���������� �����','������'):
        #message = get_daily_schedule(2)
    #elif keyword in keyword_gen('���������� �� �������','���������� �������','������'):
        #message = get_daily_schedule(3)
    #elif keyword in keyword_gen('���������� �� �������','���������� �������','������'):
        #message = get_daily_schedule(4)
    #elif keyword in keyword_gen('���������� �� �������','���������� �������','������'):
        #message = get_daily_schedule(5)
    #elif keyword in keyword_gen('���������� �� �����������','���������� �����������','������'):
        #message = get_daily_schedule(6)
    #else:
        #message = ' sorry...'
    #return message, ''


#schedule_command = command_system.Command()
#schedule_command.keys = keyword_gen('����������','����', 'hfcgbcfybt', 'hfcg',
                                    #'���������� �� �������', '���������� �������', '�������', 'hfcgbcfybt yf ctujlyz', 'hfcg yf ctujlyz',
                                    #'���������� �� ������','���������� ������','�������', 'hfcgbcfybt yf pfdnhf', 'hfcg yf pfdnhf',
                                    #'���������� �� �����','���������� �����','�������', 'hfcgbcfybt yf dxthf', 'hfcg yf dxthf',
                                    #'���������� �� �����������','���������� �����������','������', 'hfcgbcfybt yf gjytltkmybr', 'hfcg yf gjytltkmybr',
                                    #'���������� �� �������','���������� �������','������', 'hfcgbcfybt yf dnjhybr', 'hfcg yf dnjhybr',
                                    #'���������� �� �����','���������� �����','������', 'hfcgbcfybt yf chtle', 'hfcg yf chtle',
                                    #'���������� �� �������','���������� �������','������', 'hfcgbcfybt yf xtndthu', 'hfcg yf xtndthu',
                                    #'���������� �� �������','���������� �������','������', 'hfcgbcfybt yf gznybwe', 'hfcg yf gznybwe',
                                    #'���������� �� �������','���������� �������','������', 'hfcgbcfybt yf ce,,jne', 'hfcg yf ce,,jne',
                                    #'���������� �� �����������','���������� �����������','������','hfcgbcfybt yf djcrhtctymt', 'hfcg yf djcrhtctymt',)
#schedule_command.description = '����� ���������� ������ �� �����/�������/������/��/��/��/��/��/��/��, ���� �� ��� ������'
#schedule_command.process = get_schedule