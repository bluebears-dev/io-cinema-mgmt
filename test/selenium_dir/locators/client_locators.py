from selenium.webdriver.common.by import By
# todo przetestuj to wszystko

# musisz po prostu kliknac, wtedy wyswietli, co trzeba
first_page_select_locator = (By.CLASS_NAME, "v-select__selections")


# stad mozesz dla kazdego elementu wziac .text i na tej podstawie wybrac kino
# trzeba kliknac, zeby wybrac
def first_page_get_list_of_cinemas(w):
  return w.find_elements_by_class_name("v-list__tile__title")


# wystarczy klik i jestes na stronie kina
first_page_confirm_your_cinema = (By.CSS_SELECTOR, "button[type='button']")

programme_link_locator = (By.CSS_SELECTOR, "a[href='#/repertuar']")
prices_link_locator = (By.CSS_SELECTOR, "a[href='#/cennik']")
contact_link_locator = (By.CSS_SELECTOR, "a[href='#/kontakt']")

main_page_link_locator = (By.CSS_SELECTOR, "a[href='#/']")

# powinien zwrocic liste tych dni tygodnia w repertuarze, skad po .text mozna brac
def get_days_list_client(w):
  e = w.find_element_by_css_selector("main[class='v-content black'] div div div div div")
  e = e.find_element_by_css_selector("div + div")
  return e.find_elements_by_css_selector("button[type='button']")

movies_list_selector = (By.CSS_SELECTOR, ".alegreya-sc--light.movie--title")


cinema_selection_bar_locator = (By.CSS_SELECTOR, "div[class='v-select__selections'] div")
change_cinema_options_locator = (By.CLASS_NAME, "v-list__tile__title")
