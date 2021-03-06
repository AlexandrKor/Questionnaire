# "Вопросы к руководителю"

### Как использовать TaskWarrior

Откройте отдельную сессию терминала. 
Перейдите в корень репозитория и выполните команду `source TASKDATA`.
Все команды для работы с задачами выполняйте из корня репозитория.

Чтобы быстро отправлять задачи в репозиторий, можно применить алиас `tasks_push`.
Вначале, подключим алиас. Это нужно сделать один раз за одну сессию в терминале.
Если вы откроете другое окно терминала, то алиас будет недоступен и его снова
нужно будет подключить. Подключается алиас командой: `source ALIASES`. Сам алиас
определен в файле `ALIASES`. После того, как алиас станет доступен, его можно
использовать как обычную команду.

### Получение задач из репозитория

Командой `git pull origin master`. Так как все задачи мы храним в мастер-ветке
(по крайне мере, сейчас), нужно переключиться на эту ветку или клонировать проект
повторно и работать там. Задачи будут приходить как обычные изменения из
репозитория.

### Добавление и редактирование задач

Используйте taskwarrior и туториал к нему: 
https://taskwarrior.org/docs/30second.html

### Отправка задач в репозиторий

После изменения задач, выполните команду `tasks_push`.

### Клоны проекта

Для работы используется три клона проекта: 

TASKS - для работы с задачами (мастер-ветка), 
ACTUAL - актуальная (мастер-ветка),
WORK процессная (где вы будете переключаться между ветками). 

На каждый клон - своё окно терминала.
