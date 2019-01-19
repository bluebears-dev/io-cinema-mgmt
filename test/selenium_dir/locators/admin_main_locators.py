from selenium.webdriver.common.by import By

admin_username_input_locator = (By.CSS_SELECTOR, "input[name='username']")
admin_password_input_locator = (By.CSS_SELECTOR, "input[name='password']")

admin_panel_logout_locator = (By.CSS_SELECTOR, "#user-tools a:nth-of-type(3)")
admin_movies_link = (By.LINK_TEXT, "Filmy")
admin_genres_link = (By.LINK_TEXT, "Gatunki")
admin_cinemas_link = (By.LINK_TEXT, "Kina")
admin_bookings_link = (By.LINK_TEXT, "Rezerwacje")
admin_rooms_link = (By.LINK_TEXT, "Sale")
admin_showings_link = (By.LINK_TEXT, "Seanse")
admin_ticket_types_link = (By.LINK_TEXT, "Typy biletów")

admin_admins_link = (By.LINK_TEXT, "Administratorzy")
admin_groups_link = (By.LINK_TEXT, "Grupy")
admin_bosses_link = (By.LINK_TEXT, "Kierownictwo")
admin_clinets_link = (By.LINK_TEXT, "Klienci")
admin_redactors_link = (By.LINK_TEXT, "Redaktorzy")
admin_users_link = (By.LINK_TEXT, "Użytkownicy")

main_page_locator = (By.CSS_SELECTOR, "a[href='/admin/']")
