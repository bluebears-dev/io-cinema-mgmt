from cinema.tests.models.base_for_tests import CinemaModelTest, check_adding_model_instance_with_wrong_fields, NoTestOccuredException
from cinema.tests.models.base_for_tests import User, ClientProfile, EmployeeProfile


class UserTest(CinemaModelTest):
    def test_str_for_every_model(self):

        self.assertEqual(self.user_elemelek.__str__(), "elemelek")
        self.assertEqual(self.user_profile_elemelek.__str__(), "Dane kontaktowe")
        self.assertEqual(self.user_profile_tabaluga.__str__(), "Lato")

    def test_create_wrong_values(self):

        User.objects.create(username='okon', password='noko')

        ClientProfile.objects.create(user=User.objects.get(username='okon', password='noko'), phone_number=None)

        # try adding a client profile without the phone number
        check_adding_model_instance_with_wrong_fields(ClientProfile,
                                                      "Exception should occur but it "
                                                      "hadn't when creating user profile "
                                                      "without phone number", user=User.objects.get(username='okon',
                                                                                                    password='noko'),
                                                      phone_number=None)

        ###
        try:

            ClientProfile.objects.create(user=None, phone_number="1213897009")

            raise NoTestOccuredException()
        except NoTestOccuredException as e:
            print("Exception should occur but it hadn't when creating user profile without corresponding user")
            raise e
        except Exception as e:
            print("Info: " + e.__str__())

        # create user with the most critical phone_number
        User.objects.create(username='alalalalj', password='passwd')
        ClientProfile.objects.create(user=User.objects.get(username='alalalalj', password='passwd'),
                                     phone_number="999999999999")

        ###
        try:

            ClientProfile.objects.create(user=User.objects.get(username='okon', password='noko'),
                                         phone_number="12138970090887899786434")

            raise NoTestOccuredException()
        except NoTestOccuredException as e:
            print("Exception should occur but it hadn't when creating user profile with too long phone number")
            raise e
        except Exception as e:
            print("Info: " + e.__str__())

        # todo when this is done, uncomment the test
        ###
        # try:
        #
        #   ClientProfile.objects.create(user=User.objects.get(username='okon', password='noko'),
        #                              phone_number="112")
        #
        #   raise NoTestOccuredException()
        # except NoTestOccuredException as e:
        #   print("Exception should have occured but it hadn't when creating user profile with 112 phone number")
        #   raise e
        # except Exception as e:
        #   print("Info: " + e.__str__())

        ###
        try:

            ClientProfile.objects.create(user=User.objects.get(username='okon', password='noko'),
                                         phone_number="1234567")
            ClientProfile.objects.create(user=User.objects.get(username='okon', password='noko'),
                                         phone_number="12345678")

            raise NoTestOccuredException()
        except NoTestOccuredException as e:
            print("Exception should occur but it hadn't when creating user profile for already used user")
            raise e
        except Exception as e:
            print("Info: " + e.__str__())

        User.objects.create(username='arctos', password='Jakubie!')
        User.objects.create(username='hamsin', password='Key!')

        # creation of many employees in one cinema should be fully possible
        EmployeeProfile.objects.create(user=User.objects.get(username='arctos', password='Jakubie!'),
                                       cinema=self.cinema_lato)
        EmployeeProfile.objects.create(user=User.objects.get(username='hamsin', password='Key!'),
                                       cinema=self.cinema_lato)
