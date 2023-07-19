from datacenter.models import Mark, Chastisement, Schoolkid, Commendation, Subject, Lesson
import random


COMMENDATIONS = ['Молодец!',
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


def check_schoolkid(schoolkid):
    try:
        schoolkid = Schoolkid.objects.get(full_name__contains=schoolkid)
        return schoolkid
    except Schoolkid.DoesNotExist:
        print("Ошибка при вводе ученика! Такого ученика в базе данных нет! Проверьте данные на опечатку и попробуйте ещё раз.")
    except Schoolkid.MultipleObjectsReturned:
        print("Ошибка при вводе ученика! Таких учеников слишком много! Уточните введённые данные и попробуйте ещё раз.")


def remove_chastisement(schoolkid):
    schoolkid = check_schoolkid(schoolkid)
    chastisements = Chastisement.objects.filter(schoolkid=schoolkid)
    chastisements.delete()


def fix_marks(schoolkid):
    schoolkid = check_schoolkid(schoolkid)
    Mark.objects.filter(schoolkid=schoolkid, points__in=[2, 3]).update(points=5)


def create_commendation(name, subject):
    try:
        schoolkid = Schoolkid.objects.get(full_name__contains=name)
        try:
            subject = Subject.objects.get(year_of_study=schoolkid.year_of_study, title=subject)
            lessons = Lesson.objects.filter(subject=subject, year_of_study=schoolkid.year_of_study, group_letter=schoolkid.group_letter).order_by('-date')
            lesson = random.choice(lessons)
            commendation = random.choice(COMMENDATIONS)
            if lesson:
                Commendation.objects.create(text=commendation, created=lesson.date, schoolkid=schoolkid, subject=lesson.subject, teacher=lesson.teacher)
        except Subject.DoesNotExist:
            print("Ошибка при вводе предмета! Такого предмета в базе данных нет! Проверьте предмет на опечатку и попробуйте ещё раз.")
    except Schoolkid.DoesNotExist:
        print("Ошибка при вводе ученика! Такого ученика в базе данных нет! Проверьте данные на опечатку и попробуйте ещё раз.")
    except Schoolkid.MultipleObjectsReturned:
        print("Ошибка при вводе ученика! Таких учеников слишком много! Уточните введённые данные и попробуйте ещё раз.")
