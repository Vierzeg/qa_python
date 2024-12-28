import pytest

from main import BooksCollector

# класс TestBooksCollector объединяет набор тестов, которыми мы покрываем наше приложение BooksCollector
# обязательно указывать префикс Test
class TestBooksCollector:

    # пример теста:
    # обязательно указывать префикс test_
    # дальше идет название метода, который тестируем add_new_book_
    # затем, что тестируем add_two_books - добавление двух книг
    def test_add_new_book_add_two_books(self):
        # создаем экземпляр (объект) класса BooksCollector
        collector = BooksCollector()

        # добавляем две книги
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')

        # проверяем, что добавилось именно две
        # словарь books_rating, который нам возвращает метод get_books_rating, имеет длину 2
        assert len(collector.get_books_genre()) == 2

    # напиши свои тесты ниже
    # чтобы тесты были независимыми в каждом из них создавай отдельный экземпляр класса BooksCollector()

    # 1. Тестирование добавления книг
    @pytest.mark.parametrize(
        "book_name, expected_result",
        [
            ('Гордость и предубеждение и зомби', True),  # книга должна быть добавлена
            ('Что делать, если ваш кот хочет вас убить', True),  # книга должна быть добавлена
            ('', False),  # пустое имя — книга не должна добавляться
            ('a' * 41, False),  # слишком длинное имя — книга не должна добавляться
        ]
    )
    def test_add_new_book(self, book_name, expected_result):
        collector = BooksCollector()

        # Пробуем добавить книгу
        collector.add_new_book(book_name)

        # Проверяем, была ли книга добавлена
        if expected_result:
            assert book_name in collector.get_books_genre()  # Книга должна быть в словаре
        else:
            assert book_name not in collector.get_books_genre()  # Книга не должна быть в словаре

    #2. Тест установки жанра для книг
    @pytest.mark.parametrize(
        "book_name, genre, expected_genre",
        [
            ('Гордость и предубеждение и зомби', 'Фантастика', 'Фантастика'),
            ('Что делать, если ваш кот хочет вас убить', 'Ужасы', 'Ужасы'),
            ('Тайное окно', 'Детективы', 'Детективы'),
            ('Рик и Морти', 'Мультфильмы', 'Мультфильмы'),
            ('Счастливчмк Гилмор', 'Комедии', 'Комедии'),
        ]
    )
    def test_set_book_genre(self, book_name, genre, expected_genre):
        collector = BooksCollector()
        collector.add_new_book(book_name)  # Добавляем книгу
        collector.set_book_genre(book_name, genre)  # Устанавливаем жанр

        # Проверяем, что жанр книги установлен правильно
        assert collector.get_book_genre(book_name) == expected_genre

    #3. Тест получения списка книг по жанру
    @pytest.mark.parametrize(
        "genre, expected_books",
        [
            ('Фантастика', ['Гордость и предубеждение и зомби']),  # ожидаем одну книгу в жанре фантастика
            ('Ужасы', ['Что делать, если ваш кот хочет вас убить']),  # ожидаем одну книгу в жанре ужасы
            ('Детективы', ['Тайное окно']),  # ожидаем одну книгу в жанре детективы
            ('Комедии', ['Счастливчмк Гилмор']),  # ожидаем одну книгу в жанре комедии
            ('Мультфильмы', ['Рик и Морти']),  # ожидаем одну книгу в жанре мультфильмы
        ]
    )
    def test_get_books_with_specific_genre(self, genre, expected_books):
        collector = BooksCollector()

        # Добавляем книги с разными жанрами
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.set_book_genre('Гордость и предубеждение и зомби', 'Фантастика')

        collector.add_new_book('Что делать, если ваш кот хочет вас убить')
        collector.set_book_genre('Что делать, если ваш кот хочет вас убить', 'Ужасы')

        collector.add_new_book('Тайное окно')
        collector.set_book_genre('Тайное окно', 'Детективы')

        collector.add_new_book('Рик и Морти')
        collector.set_book_genre('Рик и Морти', 'Мультфильмы')

        collector.add_new_book('Счастливчмк Гилмор')
        collector.set_book_genre('Счастливчмк Гилмор', 'Комедии')

        # Проверяем, что метод возвращает правильные книги по жанру
        books_in_genre = collector.get_books_with_specific_genre(genre)
        assert books_in_genre == expected_books

    #4. Тест фильтрации книг для детей
        def test_get_books_for_children(self):
            collector = BooksCollector()

        # Добавляем книги с разными жанрами
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.set_book_genre('Гордость и предубеждение и зомби', 'Фантастика')

        collector.add_new_book('Что делать, если ваш кот хочет вас убить')
        collector.set_book_genre('Что делать, если ваш кот хочет вас убить', 'Ужасы')  # не для детей

        collector.add_new_book('Тайное окно')
        collector.set_book_genre('Тайное окно', 'Детективы')  # не для детей

        collector.add_new_book('Рик и Морти')
        collector.set_book_genre('Рик и Морти', 'Мультфильмы')  # для детей

        collector.add_new_book('Счастливчмк Гилмор')
        collector.set_book_genre('Счастливчмк Гилмор', 'Комедии')  # для детей

        # Проверяем, что метод возвращает книги, которые подходят детям
        books_for_children = collector.get_books_for_children()
        assert 'Гордость и предубеждение и зомби' in books_for_children
        assert 'Рик и Морти' in books_for_children
        assert 'Счастливчмк Гилмор' in books_for_children
        assert 'Что делать, если ваш кот хочет вас убить' not in books_for_children
        assert 'Тайное окно' not in books_for_children

    #5. Тест на добавление книги в избранное
    @pytest.mark.parametrize(
        "book_name",
        [
            'Гордость и предубеждение и зомби',  # добавление книги в избранное
            'Что делать, если ваш кот хочет вас убить',  # добавление другой книги
            'Рик и Морти',  # добавление еще одной книги
        ]
    )
    def test_add_book_to_favorites(self, book_name):
        collector = BooksCollector()

        # Добавляем книги в коллекцию
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')
        collector.add_new_book('Рик и Морти')

        # Добавляем книгу в избранное
        collector.add_book_in_favorites(book_name)

        # Проверяем, что книга находится в избранном
        assert book_name in collector.get_list_of_favorites_books()

    #6. Тест на удаление книги из избранного
    @pytest.mark.parametrize(
        "book_name",
        [
            'Гордость и предубеждение и зомби',  # удаление книги из избранного
            'Что делать, если ваш кот хочет вас убить',  # удаление другой книги
            'Рик и Морти',  # удаление еще одной книги
        ]
    )
    def test_remove_book_from_favorites(self, book_name):
        collector = BooksCollector()

        # Добавляем книги в коллекцию и в избранное
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')
        collector.add_new_book('Тайное окно')
        collector.add_book_in_favorites('Гордость и предубеждение и зомби')  # Добавляем в избранное
        collector.add_book_in_favorites('Что делать, если ваш кот хочет вас убить')  # Добавляем в избранное

        # Удаляем книгу из избранного
        collector.delete_book_from_favorites(book_name)

        # Проверяем, что книга больше не в избранном
        assert book_name not in collector.get_list_of_favorites_books()

    #7. Тест получения жанра книги
    @pytest.mark.parametrize(
        "book_name, genre, expected_genre",
        [
            ('Гордость и предубеждение и зомби', 'Фантастика', 'Фантастика'),  # книга с жанром
            ('Что делать, если ваш кот хочет вас убить', 'Ужасы', 'Ужасы'),  # другая книга с жанром
            ('Выдуманная книга', None, None),  # книга, которая не существует
        ]
    )
    def test_get_book_genre(self, book_name, genre, expected_genre):
        collector = BooksCollector()

        # Если у нас есть жанр, то добавляем книгу с этим жанром
        if genre:
            collector.add_new_book(book_name)
            collector.set_book_genre(book_name, genre)

        # Проверяем, что метод get_book_genre возвращает ожидаемый жанр или None
        assert collector.get_book_genre(book_name) == expected_genre

    #8. Тест проверки лимита на название книги
    @pytest.mark.parametrize(
        "book_name, expected_count",
        [
            ('a' * 40, 1),  # допустимое название (40 символов)
            ('a' * 41, 0),  # недопустимое название (41 символ)
            ('', 0),         # пустое название
        ]
    )
    def test_book_name_length(self, book_name, expected_count):
        collector = BooksCollector()

        # Добавляем книгу с данным названием
        collector.add_new_book(book_name)

        # Если название валидно, устанавливаем жанр для книги
        if expected_count == 1:
            collector.set_book_genre(book_name, 'Фантастика')

        # Проверяем, что в коллекции количество книг соответствует ожидаемому
        assert len(collector.get_books_genre()) == expected_count

    # 9. Тест для проверки метода, что все добавляемые книги добалвены в список

    @pytest.mark.parametrize(
        "book_names, expected_count",
        [
            (['Гордость и предубеждение и зомби', 'Что делать, если ваш кот хочет вас убить',
              'Полет на луну', 'Сильмариллион'], 4),  # добавляем 4 книги
            (['Гордость и предубеждение и зомби', 'Что делать, если ваш кот хочет вас убить'], 2),  # добавляем 2 книги
            ([], 0),  # нет книг
        ]
    )
    def test_add_books_and_check_all(self, book_names, expected_count):
        collector = BooksCollector()

        # Добавляем книги из списка
        for book_name in book_names:
            collector.add_new_book(book_name)

        # Проверяем, что количество книг соответствует ожидаемому
        assert len(collector.get_books_genre()) == expected_count


