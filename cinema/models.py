from django.db import models

# Create your models here.


class Movie(models.Model):
    """One set of values represents one movie"""

    title = models.TextField()
    releaseDate = models.DateField()
    length = models.IntegerField()
    producer = models.TextField()
    description = models.TextField(null=True, blank=True, unique=True)
    cover = models.ImageField(unique=True)

    class Meta:
        # this means that the pair of those below must be unique
        unique_together = (("title", "releaseDate"),)


class MovieGenre(models.Model):
    """One movie can have more than one movie_genre but they should not be repeated"""
    movie = models.ForeignKey(Movie, models.CASCADE)
    genre = models.CharField(20, choices=(
      ('gat1', 'gatunek pierwszy'),
      ('gat2', 'gatunek drugi'),
      ('wiz', "you're a wizard, Harry"),
      ('lotr', 'you shall not pass'),
      ('hor', 'sikasz ze strachu'),
      ('kom', 'sikasz ze smiechu'),
      ('gat', 'ostatni gatunek'),
      ('ext', 'extinction'),
    ))


class TicketType(models.Model):
    """Represents kind of ticket

    One can consider changing the price to movie dependent version assuming there is time for that"""

    typo = models.CharField(20, primary_key=True, verbose_name="type")
    price = models.DecimalField()
    description = models.TextField(unique=True)


class Cinema(models.Model):
    """Represents a single cinema unit"""

    name = models.CharField(50, primary_key=True)
    city = models.TextField()
    postalCode = PostalCodeField()    # todo trzeba zrobić, not null, no default, no unique
    address = models.TextField(unique=True)      # todo not null, no default, de facto unique, ale czy uwzględniamy miasto?
    phoneNumber = PhoneField()        # todo trzeba zrobić, not null, no default, unique


class Room(models.Model):
    """Represents a single room in some specified cinema"""

    name = models.CharField(2)
    cinema = models.ForeignKey(Cinema, models.CASCADE)

    class Meta:
        unique_together = (('name', 'cinema'),)


class Showing(models.Model):
    """Represents a single spextacle"""
    date = models.DateField()
    hour = models.TimeField()
    room = models.ForeignKey(Room, models.CASCADE)
    movie = models.ForeignKey(Movie, models.CASCADE)
    audioType = models.CharField(10, choices=(
      ('one', 'quiet'),
      ('two', 'loud'),
      ('thr', 'hard-bass'),
      ('czt', 'louder'),
      ('piat', 'LOUDER!!!!!1!1!!111!!1!!!1111'),
      ('inf', 'the branch from "We Are Number One"'),
    ))
    pictureType = models.CharField(2, choices=(
      ('no', 'black & white with gaussian distortion'),
      ('nn', 'black & white with less gaussian distortion'),
      ('bw', 'black & white'),
      ('go', 'colorful and dim'),
      ('gd', 'colorful in hd'),
      ('3d', 'colorful in 3D'),
    ))

    class Meta:
        unique_together = ('room', 'hour', 'date')


class User(models.Model):
    email = models.EmailField(primary_key=True)
    password = models.CharField(100)  # todo Ale to ma być hash jak coś, a ten komentarz tutaj to tylko tak żeby był
    firstname = models.CharField(20)
    surname = models.CharField(50)
    phoneNumber = PhoneField()          # todo trzeba napisać, chyba null, no default, no unique
    role = models.CharField(20, choices=(
      ('admin', 'admin'),
      ('kierownik', 'kierownik'),
      ('redaktor', 'redaktor'),
    ))


class Booking(models.Model):
    user = models.ForeignKey(User, models.CASCADE)
    showing = models.ForeignKey(Showing, models.CASCADE)
    state = models.CharField(20, choices=(
      ('first_state', 'first_state'),
      ('second_state', 'second_state'),
      ('stety', 'niestety'),
    ), default='first_state')


class Seat(models.Model):
    room = models.ForeignKey(Room, models.CASCADE)
    row = models.SmallIntegerField()        # not null, no default, unique tylko w tym samym room
    column = models.SmallIntegerField()
    realRow = models.SmallIntegerField()
    realColumn = models.CharField(2)

    class Meta:
        unique_together = ()   # todo ale jak to to jak toto


class Ticket(models.Model):
    booking = models.ForeignKey(Booking, models.CASCADE)
    seat = models.ForeignKey(Seat, models.CASCADE)
    typo = models.ForeignKey(TicketType, models.CASCADE, verbose_name="type")  # todo upewnij się, że z tym verbose w foreign nie bedzie problemu

    class Meta:
        unique_together = ('booking', 'seat')
