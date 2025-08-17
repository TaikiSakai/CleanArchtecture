class UserNotFoundError(Exception):
    
    meessage = "User not found."

    def __init__(self, user_id: int):
        super().__init__(f"{self.meessage} User ID: {user_id}")
        self.user_id = user_id