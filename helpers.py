from faker import Faker


fake = Faker()


class UserGenerator:
    @staticmethod
    def generate_user_email():
        email = fake.email()
        return email

    @staticmethod
    def generate_user_password():
        password = fake.password(length=6, special_chars=False, digits=True, upper_case=True, lower_case=True)
        return password

    @staticmethod
    def generate_user_name():
        name = fake.name()
        return name

    def generate_user_info(self):
        return {
            "email": self.generate_user_email(),
            "password": self.generate_user_password(),
            "name": self.generate_user_name()
        }

    @staticmethod
    def generate_user_bad_info():
        password = fake.password(length=6, special_chars=False, digits=True, upper_case=True, lower_case=True)
        name = fake.name()
        return {
            "password": password,
            "name": name
        }
