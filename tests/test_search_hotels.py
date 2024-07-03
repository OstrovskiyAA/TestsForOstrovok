from pages.main_page import SearchHotels
import allure
search_hotel=SearchHotels()
@allure.step('first test')
@allure.link("https://ostrovok.ru/", name="Testing")
def test_search_hotels_on_2025(open_selenoid):
    search_hotel.choose_destination()
    search_hotel.choose_dates()
    search_hotel.choose_amount_of_guests()
    search_hotel.should_have_wroten_text()