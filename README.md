# Взлом электронного дневника

Программа исправляет плохие оценки ученика на пятёрки, удаляет все замечания и хвалит ученика по введённому предмету.  

## Запуск

- Скачайте код
- Python3 должен быть уже установлен. 
- Также должен быть настроен сайт электронного дневника, который работает на отдельном сервере. 
- Затем достаточно положить файл `scripts.py` в репозиторий дневника. 
- Для работы понадобится два терминала: в первом терминале запускаем сайт командой `python manage.py runserver`. А во втором терминале запускаем Django shell командой `python manage.py shell`.

### Пример запуска проекта

Команды будем писать только во втором терминале. 
Для начала импортируем все функции из файла `scripts.py` с помощью команды 
```from scripts import remove_chastisement, fix_marks, create_commendation```
Чтобы исправить все плохие оценки на пятёрки введите в функции remove_chastisement ФИО ученика, например: 
```fix_marks('Иван Иванов Иванович')```
Чтобы удалить у ученика все замечания введите воспользуйтесь функцией remove_chastisement: 
```remove_chastisement('Иван Иванов Иванович')```
Чтобы похвалить ученика введите в функцию create_commendation ФИО ученика и предмет, по которому надо похвалить:
```create_commendation('Иван Иванов Иванович', 'Математика')```
При вводе ученика и предмета не допускайте опечаток, иначе программа выдаст соответствующие ошибки. 

### Цель проекта

Код написан в образовательных целях на онлайн-курсе для веб-разработчиков [dvmn.org](https://dvmn.org/).