import pytest


# set_up - для каждого теста, будет писать в начале текст и в конце
@pytest.fixture()
def set_up():
    print("Старт теста")
    yield
    print("Конец теста")

# set_group - для всего файла и его тестов, будет писать в начале текст и в конце, по 1 разу на все тесты
@pytest.fixture(scope="module")
def set_group():
    print("ВХод в систему")
    yield
    print("Выход из системы")
