import time

import allure
from selene import browser, by, have
from selene.core.command import js
from data.params_for_searching_hotel import Search

search=Search('Saint Petersburg', 'Март', 2, 4, 2, 'Работа')
class SearchHotels:
    def __init__(self):
        pass

    def choose_destination(self, destination: str = search.destination):
        with allure.step("choose destination"):
            browser.element(".Input-module__control--tqFEn").type(destination).press_enter()
         #    browser.all(".Suggest-module__destinationTitle--FrP_e").element_by(
         #        have.exact_text(
         #            "Saint Petersburg-"
         #     )
         # ).click()
        # browser.all(
        #     "[class=Popup-module__popup--1hfCp .Suggest-module__region--1KGe9]").element('title="Санкт-Петербург-Главный, Россия"').click()

    def choose_dates(
        self, month: str = search.month, date_of_start: int = search.date_of_start, date_of_finish: int = search.date_of_finish
    ):
        with allure.step("choose dates"):
            browser.element("[data-testid=date-start-input]").click()
            browser.all(".Month-module__wrapper--R5qge").element_by(
                have.exact_text(month)
            ).click()

            browser.all(
                ".Month-module__wrapper--1pwkA>.Month-module__title--1ZWbq"
            ).element_by(have.exact_text(month)).element("..").all(
                ".Day-module__inner--y2nlD"
            ).element_by(
                have.exact_text(f"{date_of_start}")
            ).perform(
                command=js.click
            )
            browser.all(
                ".Month-module__wrapper--1pwkA>.Month-module__title--1ZWbq"
            ).element_by(have.exact_text(month)).element("..").all(
                ".Week-module__week--3RmiM>.Day-module__wrapper--193jI>.Day-module__inner--y2nlD"
            ).element_by(
                have.exact_text(f"{date_of_finish}")
            ).perform(
                command=js.click
            )
    def choose_amount_of_guests(self,number:int=search.amount_of_int, goal_of_trip:str=search.aim_of_trip):
        with allure.step("choose amount of guests"):
            browser.element('.Guests-module__input--3qYEB').click()
            browser.all(".Counter-module__countButton--3e2-F").element_by(have.exact_text('+')).click()
            browser.element(".NativeSelect-module__select--1PIS7").click()
            browser.all("option").element_by(have.value(f'{number}')).click()
            browser.all('.Button-module__button--MR2Ly')[1].click()
            browser.all(".InputRadio-module__text--1AvJl").element_by(have.exact_text(f'{goal_of_trip}')).click()
            browser.all(".Button-module__content--2FF16")[0].click()
            time.sleep(1)

    def should_have_wroten_text(self):
        with allure.step('Assertion'):
            browser.element('.zenregioninfo-dates').should(have.exact_text(
                f'{search.date_of_start} {search.month[:3].lower()} 2025 — {search.date_of_finish} {search.month[:3].lower()} 2025'))
            browser.element('.zenregioninfo-region').should(have.text(f'{search.destination}'))