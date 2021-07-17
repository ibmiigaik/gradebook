Система "Электронная зачетка" предполагает прохождение аутентификации пользователей через сервис аутентификации (session_service).

Если у пользвователя есть активная сессия, то можно продолжать работать, иначе перенаправлять на страницу аутентификации.

Пользователи могут иметь одну (или несколько) из 3-х ролей:
 
- преподаватель;
- студент;
- сотрудник деканата;

Дальнейшее описание предполагает выполнения внутри реализуемой системы.
 
Система должна обеспечивать следующий бизнес-процесс:
 
1) Деканат создает ведомость на группу студентов и назначает преподавателя (группы, преподаватели, студенты должны находиться в системе и иметь отношения внутри БД. Например, студент принадлежит группе);
2) В день экзамена преподаватель может редактировать эту ведомость (вносить оценки). После того, как преподаватель выставил оценки, он может отправить форму, после чего, студент может увидеть оценку за этот экзамен в своей электронной зачетке. В случае, если преподаватель решил изменить оценку после отправки ведомости, он может вернуть ее в работу, но такие действия должны логироваться и должна сохраняться версионность;
3) В личном кабинете студент может видеть свои оценки за сданные им экзамены и зачеты (выставленные внутри системы), что и является электронной зачеткой. В случае, если студент не согласен с оценкой, то он может ее отметить и написать комментарий, почему оценка некорректна;
4) Сотрудник деканата должен иметь возможность видеть оценки всех студентов, с возможность фильтрации по курсам, группам, преподавателю и т.п.
5) В случае, если студент отмечает несогласие с оценкой, то сотрудник деканата должен видеть уведомление внутри системы, что оперативно отреагировать на это событие.
