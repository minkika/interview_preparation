# interview_preparation

Набор домашних заданий к курсу GeekBrains "Подготовка к собеседованию Python-разработчика"

## Урок 1. Python - синтаксис языка, базовые структуры данных, функциональное программирование.

1. Написать функцию, реализующую вывод таблицы умножения размерностью AｘB. Первый и второй множитель должны задаваться в
   виде аргументов функции. Элементы строки
   (элементы таблицы умножения) должны разделяться табуляцией.
1. Дополнить следующую функцию недостающим кодом:
    ```
    def print_directory_contents(sPath):
    
        Функция принимает имя каталога и распечатывает его содержимое
        в виде «путь и имя файла», а также любые другие
        файлы во вложенных каталогах.
    
        Эта функция подобна os.walk. Использовать функцию os.walk
        нельзя. Данная задача показывает ваше умение работать с
        вложенными структурами.
    ```
1. Разработать генератор случайных чисел. В функцию передавать начальное и конечное число генерации
   (нуль необходимо исключить). Заполнить этими данными список и словарь. Ключи словаря должны создаваться по шаблону:
   “elem_<номер_элемента>”. Вывести содержимое созданных списка и словаря.
1. Написать программу «Банковский депозит». Она должна состоять из функции и ее вызова с аргументами. Клиент банка
   делает депозит на определенный срок. В зависимости от суммы и срока вклада определяется процентная ставка:
   1000–10000 руб (6 месяцев — 5 % годовых, год — 6 % годовых, 2 года — 5 % годовых). 10000–100000 руб (6 месяцев — 6 %
   годовых, год — 7 % годовых, 2 года – 6.5 % годовых). 100000–1000000 руб (6 месяцев — 7 % годовых, год — 8 % годовых,
   2 года — 7.5 % годовых). Необходимо написать функцию, в которую будут передаваться параметры:
   сумма вклада и срок вклада. Каждый из трех банковских продуктов должен быть представлен в виде словаря с ключами (
   begin_sum, end_sum, 6, 12, 24). Ключам соответствуют значения начала и конца диапазона суммы вклада и значения
   процентной ставки для каждого срока. В функции необходимо проверять принадлежность суммы вклада к одному из
   диапазонов и выполнять расчет по нужной процентной ставке. Функция возвращает сумму вклада на конец срока.
1. Усовершенствовать программу «Банковский депозит». Третьим аргументом в функцию должна передаваться фиксированная
   ежемесячная сумма пополнения вклада. Необходимо в главной функции реализовать вложенную функцию подсчета процентов
   для пополняемой суммы. Примем, что клиент вносит средства в последний день каждого месяца, кроме первого и
   последнего. Например, при сроке вклада в 6 месяцев пополнение происходит в течение 4 месяцев. Вложенная функция
   возвращает сумму дополнительно внесенных средств (с процентами), а главная функция — общую сумму по вкладу на конец
   периода.

## Урок 2. Python - парадигма ООП особенности и отличия от других ЯП.

1. Проверить механизм наследования в Python. Для этого создать два класса. Первый — родительский (`ItemDiscount`),
   должен содержать статическую информацию о товаре: название и цену. Второй — дочерний (`ItemDiscountReport`), должен
   содержать функцию (`get_parent_data`), отвечающую за отображение информации о товаре в одной строке. Проверить работу
   программы, создав экземпляр (объект) родительского класса.
2. Инкапсулировать оба параметра (название и цену) товара родительского класса. Убедиться, что при сохранении текущей
   логики работы программы будет сгенерирована ошибка выполнения.
3. Усовершенствовать родительский класс таким образом, чтобы получить доступ к защищенным переменным. Результат
   выполнения заданий 1 и 2 должен быть идентичным.
4. Реализовать возможность переустановки значения цены товара. Необходимо, чтобы и родительский, и дочерний классы
   получили новое значение цены. Следует проверить это, вызвав соответствующий метод родительского класса и функцию
   дочернего (функция, отвечающая за отображение информации о товаре в одной строке).
5. Реализовать расчет цены товара со скидкой. Величина скидки должна передаваться в качестве аргумента в дочерний класс.
   Выполнить перегрузку методов конструктора дочернего класса (метод init, в который должна передаваться переменная —
   скидка), и перегрузку метода str дочернего класса. В этом методе должна пересчитываться цена и возвращаться результат
   — цена товара со скидкой. Чтобы все работало корректно, не забудьте инициализировать дочерний и родительский классы (
   вторая и третья строка после объявления дочернего класса).
6. Проверить на практике возможности полиморфизма. Необходимо разделить дочерний класс `ItemDiscountReport` на два
   класса. Инициализировать классы необязательно. Внутри каждого поместить функцию `get_info`, которая в первом классе
   будет отвечать за вывод названия товара, а вторая — его цены. Далее реализовать выполнение каждой из функции тремя
   способами.

## Урок 3. Python - стандартная библиотека Python.

1. Написать программу, которая будет содержать функцию для получения имени файла из полного пути до него. При вызове
   функции в качестве аргумента должно передаваться имя файла с расширением. В функции необходимо реализовать поиск
   полного пути по имени файла, а затем «выделение» из этого пути имени файла (без расширения).
2. Написать программу, которая запрашивает у пользователя ввод числа. На введенное число она отвечает сообщением, целое
   оно или дробное. Если дробное — необходимо далее выполнить сравнение чисел до и после запятой. Если они совпадают,
   программа должна возвращать значение True, иначе False.
3. Создать два списка с различным количеством элементов. В первом должны быть записаны ключи, во втором — значения.
   Необходимо написать функцию, создающую из данных ключей и значений словарь. Если ключу не хватает значения, в словаре
   для него должно сохраняться значение None. Значения, которым не хватило ключей, необходимо отбросить.
4. Написать программу, в которой реализовать две функции. В первой должен создаваться простой текстовый файл. Если файл
   с таким именем уже существует, выводим соответствующее сообщение. Необходимо открыть файл и подготовить два списка: с
   текстовой и числовой информацией. Для создания списков использовать генераторы. Применить к спискам функцию zip().
   Результат выполнения этой функции должен быть обработан и записан в файл таким образом, чтобы каждая строка файла
   содержала текстовое и числовое значение. Вызвать вторую функцию. В нее должна передаваться ссылка на созданный файл.
   Во второй функции необходимо реализовать открытие файла и простой построчный вывод содержимого. Вся программа должна
   запускаться по вызову первой функции.
5. Усовершенствовать первую функцию из предыдущего примера. Необходимо просканировать текстовый файл, созданный на
   предыдущем задании и реализовать создание и запись нового текстового файла. В новый текстовый файл обеспечить запись
   строк вида:  
   `zmsebjvdgi zmsebjvdgi ychpwljtzn ychpwljtzn`  
   Т.е. извлекаются строки из первого текстового файла, а в новый они записываются в виде, где вместо числа ставится
   строка. Здесь необходимо использовать регулярные выражения.

## Урок 4. Django - основные понятия ORM, структура и особенности проектирования.

Практическим заданием будет каталог товаров, состоящий из двух страниц:

* главной со списком товаров и кнопкой их добавления;
* страницы добавления товара.

Приложение должно функционировать в синхронном режиме: пользователь нажимает кнопку «Добавить товар», переходит на
предназначенную для этого страницу, указывает в форме необходимые данные и нажимает «Сохранить». После этого он
перенаправляется на главную страницу, где в табличной форме отображается список всех товаров. Проект должен быть
привязан к базе данных SQLite3 (БД по умолчанию) и иметь минимальную сложность стилевого оформления. При работе над
проектом:

1. Создать виртуальное окружение проекта, под которым установить необходимый инструментарий (файл `requirements.txt`).
2. Под виртуальным окружением создать Django-проект и одно приложение, настроить файл `settings.py`, выполнить базовые
   миграции. Запустить Django-сервер для проверки работоспособности проекта.
3. В каталоге приложения создать модель, которая должна хранить информацию о поступивших товарах: название, дату
   поступления, цену, единицу измерения, имя поставщика. Выполнить миграции.
4. Проверить правильность созданной модели, зарегистрировав ее в админке приложения.
5. На основе модели добавить класс формы указания данных о товаре. Использовать наследование от `forms.ModelForm`.
6. Настроить файл `urls.py` внутреннего каталога проекта. Он должен содержать два шаблона url-адресов: привязку к
   url-адресу админки проекта (будет в файле по умолчанию после создания проекта) и привязку к набору шаблонов
   url-адресов созданного приложения (оператор `include`).
7. Создать и настроить файл привязок `urls.py` для приложения. В этом файле создать две привязки: к url-адресу главной
   страницы проекта и к странице добавления товара. Для каждой из привязок указать функцию-контроллер и название.
   Функции-контроллеры должны отвечать за загрузку списка товаров на главной странице и добавление товара на второй
   странице.
8. В файле `views.py` каталога проекта реализовать два контроллера в формате функций. Первый должен извлекать все записи
   из модели с каталогом товаром и передавать переменную со списком товаров в контекст шаблона (html-страница со списком
   товаров). Во втором контроллере должен создаваться объект формы для ввода данных о товаре и выполняться рендеринг
   шаблона страницы добавления товара. В контекст шаблона необходимо передавать объект формы.
9. В корне проекта создать директорию templates с двумя стандартными шаблонами: базовым (`base.html`) и шаблоном формы (
   `form.html`). Базовый шаблон будет соответствовать каркасу главной страницы. В нем необходимо реализовать один
   динамически обновляемый блок — например, `{% block content %}{% endblock %}`. Он будет содержать таблицу со списком
   товаров, которая динамически подгружается из шаблона-наследника (html-страница со списком товаров). В файле base.html
   необходимо подключить статику и указать ссылку на CSS-файл со стилизацией проекта. Можно воспользоваться файлом
   `bootstrap.min.css` (его нужно скачать и поместить в каталог `.static/css`).
10. В шаблоне формы `form.html`, используя теги шаблонов, реализовать разметку формы. При этом использовать переменную
    контекста шаблона, содержащую объект формы, — например, form. К надписям полей обращаться по `field.label`, к самим
    полям — `field`.
11. В каталоге приложения создать директорию `templates` с двумя шаблонами: шаблоном html-страницы со списком
    товаров (`goods_list.html`) и html-страницы (формы) их добавления (`good_create.html`). В первом шаблоне необходимо 
    указать шаблон-родитель `base.html`, кнопку добавления товара и разметить html-таблицу. Каждая из ее строк (кроме 
    той, что с заголовками) должна формироваться при переборе содержимого переменной со списком товаров — мы ее 
    предварительно передали в контекст данного шаблона из соответствующего контроллера. Для каждого из значений 
    переменной (фактически — это запись базы данных), полученного в цикле, необходимо обратиться к нужному полю и
    вывести его в соответствующей ячейке. К кнопке привязать ссылку на страницу добавления товара. Для этого 
    использовать имя нужного шаблона url-адреса файла urls.py приложения.
12. В шаблоне `good_create.html` создать html-тег form. В него поместить тег `include`, добавляющий html-разметку
    формы (`form.html`) и кнопку добавления товара. Для тега form необходимо определить два атрибута: `method` со
    значением `post` и `enctype` со значением `multipart/form-data`.
    
## Урок 5. Django - AJAX, JavaScript, jQuery

1. Доработка шаблонов  
   В первую очередь необходимо внести изменения в шаблон `goods_list.html`. Создадим пустую структуру вложенных блочных 
   элементов `div` (три элемента). Ее содержимое будет динамически изменяться при нажатии кнопки добавления товара, т.е. 
   будет загружаться модальное окно формы добавления товара. Данную структуру можно реализовать следующим образом:
   ```html
   
   <div class="modal fade" id="modal-good">
      <div class="modal-dialog">
         <div class="modal-content">
   
         </div>
      </div>
   </div>
   ```
   В данном случае первый блочный элемент `div` с идентификатором `modal-good` соответствует модальному окну формы 
   добавления товара. Второй `div` позволяет определить стилизацию компактного окна, а третий будет содержать html-код 
   самой формы. Он будет динамически передаваться в этот `div`, и пользователь увидит на экране подгружаемую форму. 
   Приведенный код необходимо разместить в конце шаблона `goods_list.html`.
   Далее в этом же шаблоне `goods_list.html` следует изменить разметку кнопки добавления товара: убрать из тега `button` 
   тег ссылки `<a>` и заменить его простым тегом строки `span` c названием кнопки. Тегу `button` назначить два атрибута: 
   `class` (необходим для получения доступа к элементу из файла-скрипта) и `data-url` (позволяет идентифицировать страницу, 
   генерируемую посредством `jQuery`).
   Разметка кнопки при этом может принять такой вид:
   ```html
   <button type="button" class="js-create-good" data-url="{% url 'good_create' %}">
   ```
   Следующее, что необходимо сделать с файлом `goods_list.html`, — подключить скрипт на языке `JavaScript`, который 
   позволит силами библиотеки `jQuery` реализовать асинхронное взаимодействие с сервером. При этом тег `script` надо 
   поместить в соответствующий тег шаблона `{% block javascript %}{% endblock %}`.
   Поскольку динамически у нас должна обновляться не вся главная html-страница, а лишь табличная часть со списком товаров, 
   создадим дополнительный шаблон `partial_goods_list.html`. В него поместим шаблонный тег цикла, отвечающего за 
   формирование таблицы с данными. При этом в файле шаблона `goods_list.html` выполним импорт файла нового шаблона 
   `partial_goods_list.html`.  
   В файле `base.html` необходимо добавить подключение библиотеки `jQuery`. Для локального подключения следует скачать и 
   поместить в директорию `static/js` файл с кодом библиотеки — например, `jquery-3.3.1.min.js`. В эту же директорию 
   следует добавить файл `bootstrap.min.js`, который позволит упростить стилизацию элементов страницы.  
   Шаблон `good_create.html` следует модифицировать, указав в атрибуте `action` тега form имя url-шаблона адреса, при 
   переходе на который запускается контроллер записи в модель введенных данных. В нашем случае это шаблон `good_create.html`.
   Также в данный шаблон необходимо поместить тег импорта разметки самой формы `form.html` в блочный элемент и добавить 
   две кнопки: сохранения данных в форме и ее закрытия.
   Пример кода до изменений:
   ```html
   <form method="post" enctype="multipart/form-data">
      {% include "form.html" %}
   
      <div class="submit-button"><input type="submit"
                                        value="Добавить"></div>
   </form>
   ```
   И после изменений:
   ```html
   <form method="post" action="{% url 'good_create' %}" class="js-good-create-form">
      {% csrf_token %}
      <div class="modal-body">
         {% include "form.html" %}
      </div>
      <div class="modal-footer">
         <button type="button" class="btn btn-default" data-dismiss="modal">Close</button>
         <button type="submit" class="btn btn-primary">Create good</button>
      </div>
   </form>
   ```
   Атрибут `data-dismiss` со значением `modal` позволяет реализовать закрытие формы по нажатию данной кнопки.  
   В шаблон формы `form.html` необходимо выполнить загрузку инструментов пакета `django-widget-tweaks`:
   `{% load widget_tweaks %}`

2. Доработка контроллеров  
   Необходимо доработать один из двух наших контроллеров и написать третий. С первым — `good_list` — все в порядке, а 
   во втором контроллере необходимо реализовать только проверку типа запроса: `POST` или `GET`. При этом также должен 
   генерироваться экземпляр формы. Возвращать этот контроллер должен вызов дополнительного контроллера-функции 
   `save_good_form` со следующими параметрами: объект запроса, объект формы, шаблон. Поскольку данный контроллер 
   должен «открыть» форму добавления товара, в качестве шаблона следует передавать `good_create.html`.
   Контроллер `save_good_form` используется для проверки валидности и формирования словаря data, в котором мы будем 
   указывать, является ли форма валидной, а также передавать преобразованный в строку шаблон и контекст 
   (метод `render_to_string`). Данный контроллер будет возвращать ответ в формате JSON. Это позволит работать с формой 
   и контекстом из файла скрипта средствами библиотеки jQuery, то есть асинхронно делать форму и передавать данные на 
   сторону сервера.
   
   Пример того, как может быть реализован дополнительный контроллер `save_good_form`:
   ```python
   def save_good_form(request, form, template_name):
       data = dict()
       if request.method == 'POST':
           if form.is_valid():
               form.save()
               data['form_is_valid'] = True
               goods = Good_Item.objects.all()
               data['html_good_list'] = render_to_string('good_list.html', {'goods': goods})
           else:
               data['form_is_valid'] = False
       context = {'form': form}
       data['html_form'] = render_to_string(template_name, context, request=request)
       return JsonResponse(data)
   ```
   

3. Написание скрипта  
   Этот скрипт должен обрабатывать переданные в формате JSON данные: обращаться с помощью селекторов к элементам 
   веб-страницы и осуществлять манипуляции над ними. Подразумевается динамическое обновление содержимого главной 
   страницы: подгрузка шаблона формы, а также асинхронное (без перезагрузки главной страницы) сохранение данных в 
   модель. Для этого в файле сценария должны быть реализованы две функции. Первая отвечает за загрузку формы, 
   вторая — за сохранение введенных в форму данных. Для запуска первой функции необходимо выполнить ее привязку к 
   событию нажатия на кнопку добавления товара. Для запуска второй привязка должна быть выполнена к событию отправки 
   формы. И функции, и инструкции их вызова должны быть сохранены в функции-обертке 
   `$(function(){....программный код….});`, чтобы решить всю задачу средствами библиотеки jQuery.
      