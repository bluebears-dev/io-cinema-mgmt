from selenium.webdriver.common.by import By
from code import interact

go_to_models_list_locator = (By.PARTIAL_LINK_TEXT, "KAPPA")
add_model_locator = (By.PARTIAL_LINK_TEXT, "DODAJ")

delete_marked_models_select_locator = (By.CSS_SELECTOR, "select[name='action']")
"""To use this use e.find_elements_by_tag_name("option")
you can also use Select class
then just submit"""

mark_all_checkbox_locator = (By.ID, "action-toggle")


def get_list_of_every_model_checkbox_locator(w):
  list_of_elements = w.find_element_by_id("result_list")
  return list_of_elements.find_elements_by_css_selector("td[class='action-checkbox'] input[type='checkbox']")


def get_list_of_every_model_link_locator(w):
  list_of_elements = w.find_element_by_id("result_list")
  return list_of_elements.find_elements_by_css_selector("tbody tr th a")

add_new_element_locator = (By.NAME, "_save")
add_new_element_and_again_locator = (By.NAME, "_addanother")
add_new_element_and_edit_locator = (By.NAME, "_continue")
delete_from_element_site_locator = (By.CLASS_NAME, "deletelink")

deletion_confirmation_locator = (By.CSS_SELECTOR, "input[value='Tak, na pewno']")
deletion_resignation_locator = (By.CSS_SELECTOR, "input[value='Tak, na pewno'] + a")

cinema_add_cinema_name_locator = (By.CSS_SELECTOR, "input[name='name']")
cinema_add_city_locator = (By.CSS_SELECTOR, "input[name='city']")
cinema_add_address_locator = (By.CSS_SELECTOR, "input[name='address']")
cinema_add_postal_code_locator = (By.CSS_SELECTOR, "input[name='postal_code']")
cinema_add_phone_number_locator = (By.CSS_SELECTOR, "input[name='phone_number']")

ticket_type_add_type_locator = (By.CSS_SELECTOR, "input[name='ticketType']")
ticket_type_add_price_locator = (By.CSS_SELECTOR, "input[name='price']")
ticket_type_add_description_locator = (By.CSS_SELECTOR, "textarea[name='description']")

movie_add_title_locator = (By.CSS_SELECTOR, "input[name='title']")
movie_add_release_date_locator = (By.CSS_SELECTOR, "input[name='releaseDate']")
movie_add_length_locator = (By.CSS_SELECTOR, "input[name='length']")
movie_add_producer_locator = (By.CSS_SELECTOR, "input[name='producer']")
movie_add_description_locator = (By.CSS_SELECTOR, "textarea[name='description']")
movie_add_genre_locator = (By.CSS_SELECTOR, "select[name='genre']")
movie_add_cover_locator = (By.CSS_SELECTOR, "input[name='cover']")
movie_set_date_today = (By.LINK_TEXT, "Dzisiaj")

movie_genre_add_genre_locator = (By.CSS_SELECTOR, "input[name='name']")

booking_add_user_locator = (By.CSS_SELECTOR, "select[name='user']")
booking_add_showing_locator = (By.CSS_SELECTOR, "select[name='showing']")
booking_add_state_locator = (By.CSS_SELECTOR, "select[name='state']")

room_add_name_locator = (By.CSS_SELECTOR, "input[name='name']")
room_add_cinema_locator = (By.CSS_SELECTOR, "select[name='cinema']")
room_add_rows_locator = (By.CSS_SELECTOR, "input[name='rows']")
room_add_cols_locator = (By.CSS_SELECTOR, "input[name='cols']")


# sprawdx, czy zadziala
def room_get_layout(w):
  el = w.find_element(By.ID, "id_layout")
  return el.find_elements_by_css_selector("tr td input[type='checkbox']")


showing_add_movie_locator = (By.CSS_SELECTOR, "select[name='movie'")
showing_add_date_locator = (By.CSS_SELECTOR, "input[name='date'")
showing_set_date_today = (By.LINK_TEXT, "Dzisiaj")
showing_add_hour_locator = (By.CSS_SELECTOR, "input[name='hour']")
showing_set_hour_now = (By.LINK_TEXT, "Teraz")
showing_add_room_locator = (By.CSS_SELECTOR, "select[name='room']")
showing_add_audio_type_locator = (By.CSS_SELECTOR, "select[name='audio_type']")
showing_add_picture_type_locator = (By.CSS_SELECTOR, "select[name='picture_type']")

# uzywane rowniez do admina, kierownika oraz redaktora (w wypadku tego ostatniego tylko login i haslo)
user_add_username_locator = (By.CSS_SELECTOR, "input[name='username']")
user_add_password_locator = (By.CSS_SELECTOR, "input[type='password'][name='password1']")
user_add_password_confirmation_locator = (By.CSS_SELECTOR, "input[type='password'][name='password2']")
user_add_place_locator = (By.NAME, "employee_profile-0-cinema")

group_add_name_locator = (By.CSS_SELECTOR, "input[name='name']")
group_add_permissions_locator = (By.CSS_SELECTOR, "select[name='permissions_old']")
group_set_all_permissions_locator = (By.ID, "id_permissions_add_all_link")

client_add_username_locator = (By.CSS_SELECTOR, "input[name='username']")
client_add_first_name_locator = (By.CSS_SELECTOR, "input[name='first_name']")
client_add_last_name_locator = (By.CSS_SELECTOR, "input[name='last_name']")
client_add_email_locator = (By.CSS_SELECTOR, "input[name='email']")
client_add_phone_locator = (By.NAME, "client_profile-0-phone_number")
