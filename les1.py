"""
PEP - 8
переменная snake_case
CamelCase
"""

first_variable_string = "HELLO' GB"  # строки str неизменяемые
first_variable_string2 = 'Hello" \'Gb'

"""
Арифметические операторы
+
-
*
/
// - целочисленное деление
% - остаток целочисленного деления
** - возвести в степень

+=
-=

"""

# числа и числовые типы

variable_int = 12  # int целое число
variable_float = 12.122  # float дробное число

# user_name = input('ваше имя\n>>>')
# age = input('ваш возраст\n>>>')
# age = int(age)
# print('Привет {1} твой возраст {0}'.format(user_name, age))
# user_hello_string = "Привет %s твой" % user_name

variable_bool = False  # bool только 2 значения
variable_bool2 = True

"""
Операторы сравнения и логические операторы
>
<
==
>=
<=
!=
and
or
not
"""
#
# if age >= 18:
#     print('Доступ к разделу ХХХ')
# elif age > 16:
#     print('Доступ к боевикам')
# elif age > 8:
#     print('Доступ к мультикам')
# else:
#     print('Доступ запрещен')

idx = 0
while idx < 10:
    if idx % 2:
        idx += 3

    print(idx)
    idx += 1
    # if idx == 6:
    #     print('Тут BREAK')
    #     break
    # idx = idx + 1
else:
    print('ELSE CYCLE')
