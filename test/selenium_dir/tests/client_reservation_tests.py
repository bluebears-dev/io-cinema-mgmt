from test.selenium_dir.base.selenium_base import SeleniumClientTest
from test.selenium_dir.locators.client_locators import *
from test.selenium_dir.base.settings import *
from app.settings import BASE_DIR
from time import sleep

# for the test to run correctly run admin_creation_tests.py beforehand
class test_client_reservation(SeleniumClientTest):
  def test_client_buying_a_ticket_without_online_payment(self):

    # if the page asks for the cinema, choose it
    if "Repertuar" not in self.w.page_source:
      e = self.w.find_element(*first_page_select_locator)
      e.click()
      sleep(1.5)

      for a in first_page_get_list_of_cinemas(self.w):
        if a.text == cinema_name:
          a.click()
          sleep(1.5)
          break

      e = self.w.find_element(*first_page_confirm_your_cinema)
      e.click()
      sleep(1.5)

    else:
      # still choose it
      e = self.w.find_element(*cinema_selection_bar_locator)
      e.click()
      sleep(1.5)

      for a in self.w.find_elements(*change_cinema_options_locator):
        if a.text == cinema_name:
          a.click()
          sleep(1.5)
          break


    # check cennik and kontakt
    self.w.find_element(*contact_link_locator).click()
    sleep(1.5)
    assert "Adres" in self.w.page_source
    assert "Numer telefonu" in self.w.page_source
    assert cinema_address in self.w.page_source
    assert cinema_postal in self.w.page_source
    assert cinema_city in self.w.page_source
    assert cinema_phone in self.w.page_source

    self.w.find_element(*prices_link_locator).click()
    sleep(1.5)
    assert ticket_description in self.w.page_source
    assert ticket_name in self.w.page_source

    # find the showing added by admin tests
    self.w.find_element(*programme_link_locator).click()
    sleep(1.5)

    day = datetime.date(int(showing_date[6:]), int(showing_date[3:5]), int(showing_date[0:2])).weekday()
    if day == 0:
      day = "Pn"
    elif day == 1:
      day = "Wt"
    elif day == 2:
      day = r"Śr"
    elif day == 3:
      day = "Cz"
    elif day == 4:
      day = "Pt"
    elif day == 5:
      day = "So"
    else:
      day = "Nd"

    for a in get_days_list_client(self.w):
      if a.text == day:
        a.click()
        sleep(1.5)
        break

    e = self.w.find_elements(*movies_list_selector)
    for a in e:
      if a.text == movie_title:
        a.click()
        sleep(1.5)
        break

    assert movie_producer in self.w.page_source
    assert movie_length in self.w.page_source
    assert genre_name in self.w.page_source
    assert movie_description in self.w.page_source
    assert showing_hour[0:5] in self.w.page_source

    # make the reservation without online payment

    e = self.w.find_elements(*movie_hour_for_making_reservation_locator)
    for a in e:
      if showing_hour[0:5] in a.text:
        a.click()
        sleep(1.5)
        break

    assert "Wybierz Miejsca" in self.w.page_source

    self.w.find_element(*making_booking_first_seat_locator).click()
    sleep(1.5)

    e = self.w.find_elements(*making_booking_choosing_seat_next_locator)
    for a in e:
      if a.text == "Dalej":
        a.click()
        sleep(1.5)
        break

    e = self.w.find_elements(*booking_choosing_tickets_input_locator)
    for a in e:
      b = a.find_element_by_css_selector("div div div")
      if ticket_name in b.text:
        e = a.find_element_by_css_selector("div div + div")
        break
    e = e.find_element_by_css_selector("div div div div input")
    e.clear()
    e.send_keys("1")
    sleep(1.5)

    e = self.w.find_elements(*making_booking_choosing_seat_next_locator)
    for a in e:
      if a.text == "Dalej":
        a.click()
        sleep(1.5)
        break

    e = self.w.find_element(*booking_person_name_locator)
    e.clear()
    e.send_keys(reservation_name)

    e = self.w.find_element(*booking_person_surname_locator)
    e.clear()
    e.send_keys(reservation_surname)

    e = self.w.find_element(*booking_person_email_locator)
    e.clear()
    e.send_keys(reservation_email)

    e = self.w.find_element(*booking_person_phone_locator)
    e.clear()
    e.send_keys(reservation_phone)

    e = self.w.find_elements(*making_booking_choosing_seat_next_locator)
    for a in e:
      if a.text == "Dalej":
        a.click()
        sleep(1.5)
        break

    e = self.w.find_elements(*booking_get_checking_list_for_kind_of_payment_locator)
    a = e[0]
    a.click()
    sleep(1.5)

    e = self.w.find_elements(*making_booking_choosing_seat_next_locator)
    for a in e:
      if a.text == "Zakończ":
        a.click()
        sleep(1.5)
        break

    assert "Zakończ" not in self.w.page_source

    # make the reservation with online payment
    # find the showing added by admin tests
    self.w.find_element(*programme_link_locator).click()
    sleep(1.5)

    day = datetime.date(int(showing_date[6:]), int(showing_date[3:5]), int(showing_date[0:2])).weekday()
    if day == 0:
      day = "Pn"
    elif day == 1:
      day = "Wt"
    elif day == 2:
      day = r"Śr"
    elif day == 3:
      day = "Cz"
    elif day == 4:
      day = "Pt"
    elif day == 5:
      day = "So"
    else:
      day = "Nd"

    for a in get_days_list_client(self.w):
      if a.text == day:
        a.click()
        sleep(1.5)
        break

    e = self.w.find_elements(*movies_list_selector)
    for a in e:
      if a.text == movie_title:
        a.click()
        sleep(1.5)
        break

    assert movie_producer in self.w.page_source
    assert movie_length in self.w.page_source
    assert genre_name in self.w.page_source
    assert movie_description in self.w.page_source
    assert showing_hour[0:5] in self.w.page_source

    e = self.w.find_elements(*movie_hour_for_making_reservation_locator)
    for a in e:
      if showing_hour[0:5] in a.text:
        a.click()
        sleep(1.5)
        break

    assert "Wybierz Miejsca" in self.w.page_source

    self.w.find_element(*making_booking_second_seat_locator).click()
    sleep(1.5)

    e = self.w.find_elements(*making_booking_choosing_seat_next_locator)
    for a in e:
      if a.text == "Dalej":
        a.click()
        sleep(1.5)
        break

    e = self.w.find_elements(*booking_choosing_tickets_input_locator)
    for a in e:
      b = a.find_element_by_css_selector("div div div")
      if ticket_name in b.text:
        e = a.find_element_by_css_selector("div div + div")
        break
    e = e.find_element_by_css_selector("div div div div input")
    e.clear()
    e.send_keys("1")
    sleep(1.5)

    e = self.w.find_elements(*making_booking_choosing_seat_next_locator)
    for a in e:
      if a.text == "Dalej":
        a.click()
        sleep(1.5)
        break

    e = self.w.find_element(*booking_person_name_locator)
    e.clear()
    e.send_keys(reservation_name)

    e = self.w.find_element(*booking_person_surname_locator)
    e.clear()
    e.send_keys(reservation_surname)

    e = self.w.find_element(*booking_person_email_locator)
    e.clear()
    e.send_keys(reservation_email)

    e = self.w.find_element(*booking_person_phone_locator)
    e.clear()
    e.send_keys(reservation_phone)

    e = self.w.find_elements(*making_booking_choosing_seat_next_locator)
    for a in e:
      if a.text == "Dalej":
        a.click()
        sleep(1.5)
        break

    e = self.w.find_elements(*booking_get_checking_list_for_kind_of_payment_locator)
    a = e[2]
    a.click()
    sleep(1.5)

    e = self.w.find_elements(*making_booking_choosing_seat_next_locator)
    for a in e:
      if a.text == "Płać":
        a.click()
        sleep(5)
        break

    e = self.w.find_element(*confirm_payment_locator)
    e.click()
    sleep(5)

    e = self.w.find_element(*confirm_payment_locator)
    e.click()
    sleep(7)

    e = self.w.find_element(*programme_link_locator)
    e.click()
    sleep(2.5)

    assert "Pobierz" not in self.w.page_source
