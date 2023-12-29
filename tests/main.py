from test_ import FindAndClick


class RegisterAccount(FindAndClick):

    def __init__(self):
        super().__init__()

    def input_user_name(self):
        self.timeout_wait_input(self.generate_email().new_email)

    def input_user_pas(self):
        self.timeout_wait_input(self.generate_pas().new_pas, self.lc.field_pas)

    def click_register_btn(self):
         self.timeout_wait_click(self.lc.register_btn)


