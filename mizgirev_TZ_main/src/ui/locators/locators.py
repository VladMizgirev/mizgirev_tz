class CustomBasePageLocators:
    CATEGORY_CARD_ALL = "//div[@data-meta-name='CategoryTilesLayout__category-tiles']//div[2]//span[text()]"
    CATEGORY_CARD_BY_NAME = "//div[@data-meta-name='CategoryTilesLayout__category-tiles']//div[2]//span[text() = '{}']"
    COOKIE_CONFORME_BUTTON = "//span[text() = 'Я согласен']"
    LOG_IN_BUTTON = '//*[@id="__next"]/div/div[2]/div/div[2]/div/div/div[2]/div[2]/div[1]/div'
    HEADER_NAV = "//header/div[3]/div/div/div[2]/div[2]/a/span"
    CHANGE_CITY_BUTTON = "//button[@data-meta-name='CityChangeButton']"
    CART_BUTTON = "//div/div[2]/div/div/div[2]/div[2]/a[2]/div/div"


class ProductListingPage:
    LISTING_TITLE = "//div[1]/div[1]/div[2]/h1"


class LoginPageLocators:
    LOGIN_INPUT = "//input[@name='login']"
    ENTER_TO_PASS = "/html/body/div[4]/div/div/div/div/form/div/div[2]"
    PASSWORD_INPUT = "//input[@name='pass']"
    SUBMIT_BUTTON = "/html/body/div[4]/div/div/div/div/form/div/div[2]/button[1]"
    ERRORE_TITLE = '//*[@id="__next"]/div/div[3]/div/div/div'


class ChangeCityPageLocators:
    SEARCH_INPUT = "//input[@name='search-city']"
    CLEAR_TEXT = "//div/div/div/div/div/div/div[2]/div[2]/div/label/div/button[1]"


class CartPageLocators:
    CART_TITLE = "//main/div[1]/div[1]/div/div/span[text()='Корзина']"

