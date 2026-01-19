from abc import ABC, abstractmethod

class NotificationsSender(ABC):
    @abstractmethod
    def send_notificarion(self, message: str) -> None: pass

class EmailNotificationSender(NotificationsSender):    
    def send_notificarion(self, message: str) -> None:
        print(f"Email message: {message}")

class SMSNotificationSender(NotificationsSender):    
    def send_notificarion(self, message: str) -> None:
        print(f"SMS message: {message}")  

obj = SMSNotificationSender()
obj.send_notificarion("olá mundo")    

class Notificator:
    def __init__(self, notification_sender: NotificationsSender):
        self.__notificarion_sender = notification_sender

    def send(self, message: str) -> None:
        #validação de dados
        self.__notificarion_sender.send_notificarion(message)

obj = Notificator(EmailNotificationSender())
obj.send("Ola mundo")