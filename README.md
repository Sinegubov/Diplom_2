# Diplom_2
Вторая часть дипломной работы. Тестирование API для Stellar Burgers.

Проект состоит из файлов:

/tests - Папка с тестовыми классами и методами содержащими api-проверки. 
Для тестирования используется фреймворк pytest, используется параметризация входных данных. 
conftest.py - Содержит фикстуры
data.py - Файл со статичными данными для тестирования 
helpers - Сборник используемых методов 
/allure-results - папка для хранения отчета Allure




Установка необходимых модулей командой:
pip3 install -r requirements.txt 

Запустить тесты из терминала можно командой:
pytest -v --alluredir=allure-results 

Генерация отчета Allure командой:
allure serve allure_results 
