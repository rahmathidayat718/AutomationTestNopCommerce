import configparser

config = configparser.RawConfigParser()
config.read(".\\configurations\\config.ini")

class Read_config:

    @staticmethod
    def get_url_login():
        url = config.get('user login info', 'user_page_url')
        return url

    @staticmethod
    def get_user_id():
        user_id = config.get('user login info', 'user_id')
        return user_id

    @staticmethod
    def get_password():
        password = config.get('user login info', 'password')
        return password

    @staticmethod
    def get_invalid_user_id():
        invalid_user_id = config.get('user login info', 'invalid_user_id')
        return invalid_user_id

    @staticmethod
    def get_invalid_password():
        invalid_password = config.get('user login info', 'invalid_password')
        return invalid_password