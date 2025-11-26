class notification:
	def get_notification(self):


class instagram(notification):
    def get_notification(self):
        print("Instagram")

class facebook(notification):
    def get_notification(self):
        print("Facebook")

instagram = instagram()
instagram.get_notification()

