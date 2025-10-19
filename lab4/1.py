from abc import ABC, abstractmethod

#Інтерфейс 
class Notification(ABC):
    @abstractmethod
    def send(self, title: str, message: str):
        pass


# Реалізація EmailNotification
class EmailNotification(Notification):
    def __init__(self, admin_email: str):
        self.admin_email = admin_email

    def send(self, title: str, message: str):
        print(f"Sent email with title '{title}' to '{self.admin_email}' that says '{message}'")
        

#Зовнішні сервіси
class SlackAPI:
    def __init__(self, login: str, api_key: str):
        self.login = login
        self.api_key = api_key

    def send_message(self, chat_id: str, text: str):
        print(f"Slack message sent to chat '{chat_id}': {text}")


class SMSService:
    def send_sms(self, phone: str, sender: str, text: str):
        print(f"SMS sent to {phone} from '{sender}': {text}")


#Адаптери
class SlackNotificationAdapter(Notification):
    def __init__(self, slack_api: SlackAPI, chat_id: str):
        self.slack_api = slack_api
        self.chat_id = chat_id

    def send(self, title: str, message: str):
        text = f"[{title}] {message}"
        self.slack_api.send_message(self.chat_id, text)


class SMSNotificationAdapter(Notification):
    def __init__(self, sms_service: SMSService, phone: str, sender: str):
        self.sms_service = sms_service
        self.phone = phone
        self.sender = sender

    def send(self, title: str, message: str):
        text = f"{title}: {message}"
        self.sms_service.send_sms(self.phone, self.sender, text)


#Клієнтський код 
def client_code(notifier: Notification):
    notifier.send("Notification", "This is a message")



if __name__ == "__main__":
    email = EmailNotification("doNotWrite@please.com")
    slack = SlackNotificationAdapter(SlackAPI("My", "api-key-XYZ"), "chat-001")
    sms = SMSNotificationAdapter(SMSService(), "+3806611111111", "MyApp")

    client_code(email)
    client_code(slack)
    client_code(sms)
