from usergenerator import UserGenerator


class UserList:

    def __init__(self):
        self._user_list = []
        self._active_user = None

    def create_test_account(self):
        if self._active_user is None:
            self._active_user = UserGenerator.load_test_user()
        else:
            self._user_list.append(self._active_user)
            self._active_user = UserGenerator.load_test_user()

    def create_account(self):
        if self._active_user is None:
            self._active_user = UserGenerator.create_user()
        else:
            self._user_list.append(self._active_user)
            self._active_user = UserGenerator.create_user()

    def get_active_user(self):
        return self._active_user
