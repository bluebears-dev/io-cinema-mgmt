import datetime

password = "okon1234"
username = "root"
admin_address = "http://192.168.99.100/admin"
client_address = "http://192.168.99.100"

# parameters of models to be created
cinema_name = "Wojenka"
cinema_city = "Warszawa"
cinema_address = "ul. Marszałkowska 7"
cinema_postal = "00-590"
cinema_phone = "889001223"


room_name = "AK47"
room_rows = "5"
room_cols = "5"


ticket_name = "Testowy"
ticket_price = "50"
ticket_description = "Expensive for I want to test whether you're keen to pay so much"


genre_name = r"Zagrożony"


movie_title = "Elemelek"
movie_date = "12.12.2012"
movie_length = "144"
movie_producer = "Ancient Inca"
movie_description = "Elemelek is just a little elemelek. One day he faces great danger but" \
                    " manages to survive and goes home for breakfast. But the real problem " \
                    "appears when it turns out some ancient, brutal tribe doesn't have an actual " \
                    "calendar. Because of that they want to offer heart of Elemelek to the sun." \
                    "Will Elemelek be able to eat breakfast again?"

movie_cover_suffix = "/test/static/blood.jpeg"

showing_date = datetime.datetime.now().day.__str__() + "." + datetime.datetime.now().month.__str__()\
               + "." + datetime.datetime.now().year.__str__()
showing_hour = "23:59:55"
showing_sound = "Napisy"
showing_picture = "2D"
