from datacenter.models import Mark, Chastisement, Schoolkid, Commendation, Subject, Lesson
from django.core.exceptions import ObjectDoesNotExist, MultipleObjectsReturned
import random


used_lessons = []
used_commendations = []


def remove_chastisement(schoolkid):
    try:
        schoolkid = Schoolkid.objects.get(full_name__contains=schoolkid)
        chastisements = Chastisement.objects.filter(schoolkid=schoolkid)
        chastisements.delete()
    except ObjectDoesNotExist:
        print("Ошибка при вводе ученика! Такого ученика в базе данных нет! Проверьте данные на опечатку и попробуйте ещё раз.")
    except MultipleObjectsReturned:
        print("Ошибка при вводе ученика! Таких учеников слишком много! Уточните введённые данные и попробуйте ещё раз.")


def fix_marks(schoolkid):
    try:
        schoolkid = Schoolkid.objects.get(full_name__contains=schoolkid)
        marks = Mark.objects.filter(schoolkid=schoolkid, points__in=[2, 3])
        for mark in marks:
            mark.points = 5
            mark.save()
    except ObjectDoesNotExist:
        print("Ошибка при вводе ученика! Такого ученика в базе данных нет! Проверьте данные на опечатку и попробуйте ещё раз.")
    except MultipleObjectsReturned:
        print("Ошибка при вводе ученика! Таких учеников слишком много! Уточните введённые данные и попробуйте ещё раз.")


def create_commendation(name, subject):
    commendations = ['Молодец!',
                     'Отлично!',
                     'Хорошо!',
                     'Ты меня приятно удивляешь!',
                     'Великолепно!',
                     'Прекрасно!',
                     'Ты меня очень радуешь!',
                     'Именно этого я давно жду от тебя!',
                     'Сказано здорово – просто и ясно!',
                     'Ты, как всегда, точен!',
                     'Очень хороший ответ!',
                     'Талантливо!',
                     'Ты сегодня занимаешься выше головы!',
                     'Уже существенно лучше!',
                     'Потрясающе!',
                     'Замечательно!',
                     'Так держать!',
                     'Ты на верном пути!',
                     'Здорово!',
                     'Это как раз то, что нужно!',
                     'Я тобой горжусь!',
                     'С каждым разом у тебя получается всё лучше!',
                     'Мы с тобой не зря поработали!',
                     'Я вижу, как ты стараешься!',
                     'Ты растешь над собой!',
                     'Теперь у тебя точно все получится!']
    try:
        schoolkid = Schoolkid.objects.get(full_name__contains=name)
        try:
            subject = Subject.objects.get(year_of_study=schoolkid.year_of_study, title=subject)
            lessons = Lesson.objects.filter(subject=subject, year_of_study=schoolkid.year_of_study, group_letter=schoolkid.group_letter)
            lessons = lessons.order_by('-date')
            for lesson in lessons:
                if len(commendations) == len(used_commendations):
                    commendations.shuffle()
                    used_commendations.clear()
                commendation = random.choice(commendations)
                if lesson not in used_lessons and commendation not in commendations:
                    Commendation.objects.create(text=commendation, created=lesson.date, schoolkid=schoolkid, subject=lesson.subject, teacher=lesson.teacher)
                    used_lessons.append(lesson)
                    used_commendations.append(commendation)
                    break
        except ObjectDoesNotExist:
            print("Ошибка при вводе предмета! Такого предмета в базе данных нет! Проверьте предмет на опечатку и попробуйте ещё раз.")
    except ObjectDoesNotExist:
        print("Ошибка при вводе ученика! Такого ученика в базе данных нет! Проверьте данные на опечатку и попробуйте ещё раз.")
    except MultipleObjectsReturned:
        print("Ошибка при вводе ученика! Таких учеников слишком много! Уточните введённые данные и попробуйте ещё раз.")
