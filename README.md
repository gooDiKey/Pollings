# Pollings
Тестовый проект системы опросов

# О проекте:
Здесь реализован не весь функционал из задания
### Присутствуют:
- Авторизация пользователей(как админ, так и юзер), но с регистрацией.
- Добавление/изменение/удаление опросов, вопросов и ответов
- Получение списка активных вопросов
- Прохождение опросов с сохранением данных в бд
### Отсутсвуют:
- Возможность просмотра пройденных опросов (можно посмотреть только сразу после прохождения, если пользователь пройдет тест во второй раз, то показываются ответы за оба прохождения)
- Анонимное прохождение опросов
- Блокирование поля "дата старта" после после создания опроса
### Использование:
- В таблице "Опросы" можно создавать опрос, добавлять всю информацию о нем и так же добавлять связынные с ним вопросы
- В таблице "Вопросы" можно добавить варианты ответов к вопросам
- Данные по прохождению опроса добавляются в таблицу "Ответы", каждый вариант связан с вопросом и авторизованным пользователем