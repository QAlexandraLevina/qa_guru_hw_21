import allure


@allure.id("40626")
@allure.title("My first Test-Case")
@allure.label("owner", "allure8")
def test_example():
    with allure.step("Зайти на сайт"):
        pass
    with allure.step("Кликнуть по элементу"):
        with allure.step("Навести курсор мыши"):
            pass