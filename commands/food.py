import command_system

FOODS = {
    'Мучные изделия':
        {
            'Пицца': 25,  # это упрощённый вариант
            'Пирожки': (('с картофелем', 'c капустой', 'c луком и яйцом', 'c мясом', 'c шоколадом', 'c печенью', 'c яблоком'), 15),  # это вариант с видами продукта
            'Сосиска в тесте': ('очень вкусная', 25) # а это вариант с комментарием
        },  # выбрать какой-нибудь один
    '':
        {
            '': 0
        }
    }



def food(keyword=''):
   message = 'Меню\nМУЧНЫЕ ИЗДЕЛИЯ\nПицца - 25 рублей\nПирожки с картофелем, капустой, луком и яйцом, мясом, шоколадом, печенью, яблоком - 15 рублей\nСосиска в тесте - 25 рублей\nСАЛАТЫ\nВинегрет; С картофелем, кукурузой и луком - 35 рублей\nС ветчиной, сыром и огурцом; Оливье - 45 рублей\nСУПЫ\nБорщ, Рассольник, Мясной и т.д. - 40 рублей(Зависит от дня недели)\nГОРЯЧЕЕ\nКотлеты мясные и рыбные, Голубцы и т.д - 60 рублей(Зависит от дня недели)\nНАПИТКИ\nЧай - 5 рублей\nЧай с лимоном - 7 рублей\nСок - 15 рублей\nКисель и Компот - 15 рублей\nКОМПЛЕКС\nСовмещает в себе порцию Горячего, Суп, Салат, Напиток - 70 рублей(Зависит от дня недели)'
   return message, ''

food_command = command_system.Command()

food_command.keys = ['Меню','Еда', 'menu', 'food']
food_command.description = 'Выдам цены на питание в школьной столовой.'
food_command.process = food