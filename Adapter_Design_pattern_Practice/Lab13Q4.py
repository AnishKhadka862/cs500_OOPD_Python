# Lab13Q4.py
# Adapter Design Pattern Example for Notification Systems
from abc import ABC, abstractmethod

class LegacyNotificationSystem:
    # Adaptee class with existing functionality
    def send_sms_notification(self, phoneNumber: str, message: str) -> None:
        print("sending an SMS notification")


class NewNotificationSystem(ABC):
    @abstractmethod
    # Target interface for the new notification system 
    def send_email_notification(self, emailAddress: str, subject: str, body: str) -> None:
        pass

    @abstractmethod
    # Method to send push notifications
    def sendPushNotification(self, deviceToken: str, title: str, message: str) -> None:
        pass

    @abstractmethod
    # Method to send social media updates
    def send_social_media_update(self, social_media_platform: str, postContent: str) -> None:
        pass


class NotificationAdapter(NewNotificationSystem):
    # Adapter class to adapt LegacyNotificationSystem to NewNotificationSystem
    def __init__(self, legacy_system: LegacyNotificationSystem) -> None:
        self.__legacy = legacy_system
    # Implementing the target interface methods using the adaptee's functionality
    def send_email_notification(self, emailAddress: str, subject: str, body: str) -> None:
        self.__legacy.send_sms_notification(emailAddress, subject + " - " + body)
    # Implementing push notification method
    def sendPushNotification(self, deviceToken: str, title: str, message: str) -> None:
        self.__legacy.send_sms_notification(deviceToken, title + " - " + message)
    # Implementing social media update method
    def send_social_media_update(self, social_media_platform: str, postContent: str) -> None:
        self.__legacy.send_sms_notification(social_media_platform, postContent)


def main():
    system = NotificationAdapter(LegacyNotificationSystem())

    system.send_email_notification("anishkhadka@gmail.com", "Subject", "Body")
    system.sendPushNotification("demo_device", "Push Title", "Push Message")
    system.send_social_media_update("Twitter", "New post content")


if __name__ == "__main__":
    main()