from test.selenium_dir.base.selenium_base import SeleniumTest
from test.selenium_dir.locators.admin_main_locators import *
from test.selenium_dir.base.settings import *
from test.selenium_dir.locators.cinema_modify_locators import *
from app.settings import BASE_DIR
from time import sleep


class test_admin_creation_of_models(SeleniumTest):


  def test_b_adding_models(self):
    # cinema
    #
    #
    # make sure there's no element to collide with the model you want to create
    self.w.find_element(*admin_cinemas_link).click()
    sleep(1.5)

    for a in get_list_of_every_model_link_locator(self.w):
      if a.text == cinema_name:
        a.click()
        sleep(1.5)
        e = self.w.find_element(*delete_from_element_site_locator)
        e.click()
        sleep(1.5)

        e = self.w.find_element(*deletion_confirmation_locator)
        e.click()
        sleep(1.5)

        assert r"pomyślnie" in self.w.page_source
        break

    # add new cinema
    self.w.find_element(*add_model_locator).click()

    self.w.find_element(*cinema_add_cinema_name_locator).send_keys(cinema_name)
    self.w.find_element(*cinema_add_city_locator).send_keys(cinema_city)
    self.w.find_element(*cinema_add_address_locator).send_keys(cinema_address)
    self.w.find_element(*cinema_add_postal_code_locator).send_keys(cinema_postal)
    self.w.find_element(*cinema_add_phone_number_locator).send_keys(cinema_phone)

    self.w.find_element(*add_new_element_locator).click()
    assert r"pomyślnie" in self.w.page_source

    self.w.find_element(*go_to_models_list_locator).click()

    # room
    #
    #
    # make sure there's no element to collide with the model you want to create
    self.w.find_element(*admin_rooms_link).click()

    for a in get_list_of_every_model_link_locator(self.w):
      if a.text == room_name + " (" + cinema_name + ")":
        a.click()
        e = self.w.find_element(*delete_from_element_site_locator)
        e.click()

        e = self.w.find_element(*deletion_confirmation_locator)
        e.click()

        assert r"pomyślnie" in self.w.page_source
        break

    # add new room
    self.w.find_element(*add_model_locator).click()

    self.w.find_element(*room_add_name_locator).send_keys(room_name)
    e = self.w.find_element(*room_add_cinema_locator)
    e = e.find_elements_by_css_selector("option")
    for a in e:
      if a.text == cinema_name:
        a.click()
        break

    e = self.w.find_element(*room_add_rows_locator)
    e.clear()
    e.send_keys(room_rows)
    e = self.w.find_element(*room_add_cols_locator)
    e.clear()
    e.send_keys(room_cols)

    self.w.find_element(*add_new_element_locator).click()
    sleep(1.5)
    assert r"pomyślnie" in self.w.page_source

    self.w.find_element(*go_to_models_list_locator).click()

    # ticket_type
    #
    #
    # make sure there's no element to collide with the model you want to create
    self.w.find_element(*admin_ticket_types_link).click()

    for a in get_list_of_every_model_link_locator(self.w):
      if a.text == ticket_name:
        a.click()
        e = self.w.find_element(*delete_from_element_site_locator)
        e.click()

        e = self.w.find_element(*deletion_confirmation_locator)
        e.click()

        assert r"pomyślnie" in self.w.page_source
        break

    # add new ticket type
    self.w.find_element(*add_model_locator).click()

    self.w.find_element(*ticket_type_add_type_locator).send_keys(ticket_name)
    self.w.find_element(*ticket_type_add_price_locator).send_keys(ticket_price)
    self.w.find_element(*ticket_type_add_description_locator).send_keys(ticket_description)

    self.w.find_element(*add_new_element_locator).click()
    assert r"pomyślnie" in self.w.page_source

    self.w.find_element(*go_to_models_list_locator).click()

    # genre
    #
    #
    # make sure there's no element to collide with the model you want to create
    self.w.find_element(*admin_genres_link).click()

    for a in get_list_of_every_model_link_locator(self.w):
      if a.text == genre_name:
        a.click()
        e = self.w.find_element(*delete_from_element_site_locator)
        e.click()

        e = self.w.find_element(*deletion_confirmation_locator)
        e.click()

        assert r"pomyślnie" in self.w.page_source
        break

    # add new genre
    self.w.find_element(*add_model_locator).click()

    self.w.find_element(*movie_genre_add_genre_locator).send_keys(genre_name)

    self.w.find_element(*add_new_element_locator).click()
    assert r"pomyślnie" in self.w.page_source

    self.w.find_element(*go_to_models_list_locator).click()

    # movie
    #
    #
    # make sure there's no element to collide with the model you want to create
    self.w.find_element(*admin_movies_link).click()

    for a in get_list_of_every_model_link_locator(self.w):
      if a.text == movie_title:
        a.click()
        e = self.w.find_element(*delete_from_element_site_locator)
        e.click()

        e = self.w.find_element(*deletion_confirmation_locator)
        e.click()

        assert r"pomyślnie" in self.w.page_source
        break

    # add new movie
    self.w.find_element(*add_model_locator).click()

    self.w.find_element(*movie_add_title_locator).send_keys(movie_title)
    self.w.find_element(*movie_add_release_date_locator).send_keys(movie_date)
    self.w.find_element(*movie_add_length_locator).send_keys(movie_length)
    self.w.find_element(*movie_add_producer_locator).send_keys(movie_producer)
    self.w.find_element(*movie_add_description_locator).send_keys(movie_description)
    e = self.w.find_element(*movie_add_genre_locator)
    for a in e.find_elements_by_css_selector("option"):
      if a.text == genre_name:
        a.click()
        break

    self.w.find_element(*movie_add_cover_locator).send_keys(BASE_DIR + "/test/static/blood.jpeg")

    self.w.find_element(*add_new_element_locator).click()
    assert r"pomyślnie" in self.w.page_source

    self.w.find_element(*go_to_models_list_locator).click()

    # showing
    #
    #
    # make sure there's no element to collide with the model you want to create
    self.w.find_element(*admin_showings_link).click()

    for a in get_list_of_every_model_link_locator(self.w):
      if a.text == movie_title:
        a.click()
        e = self.w.find_element(*delete_from_element_site_locator)
        e.click()

        e = self.w.find_element(*deletion_confirmation_locator)
        e.click()

        assert r"pomyślnie" in self.w.page_source
        break

    # add new showing
    self.w.find_element(*add_model_locator).click()

    e = self.w.find_element(*showing_add_movie_locator).find_elements_by_css_selector("option")
    for a in e:
      if a.text == movie_title:
        a.click()
        break

    self.w.find_element(*showing_add_date_locator).send_keys(showing_date)
    self.w.find_element(*showing_add_hour_locator).send_keys(showing_hour)
    e = self.w.find_element(*showing_add_room_locator).find_elements_by_css_selector("option")
    for a in e:
      if a.text == room_name + " (" + cinema_name + ")":
        a.click()
        break

    e = self.w.find_element(*showing_add_audio_type_locator).find_elements_by_css_selector("option")
    for a in e:
      if a.text == showing_sound:
        a.click()
        break

    e = self.w.find_element(*showing_add_picture_type_locator).find_elements_by_css_selector("option")
    for a in e:
      if a.text == showing_picture:
        a.click()
        break

    self.w.find_element(*add_new_element_locator).click()
    assert r"pomyślnie" in self.w.page_source

