from abc import ABC, abstractmethod

# Абстрактна соціальна мережа
class SocialNetwork(ABC):
    @abstractmethod
    def post_message(self, message: str):
        pass

# Facebook
class FacebookNetwork(SocialNetwork):
    def __init__(self, login: str, password: str):
        self.login = login
        self.password = password
        self.connect()

    def connect(self):
        print(f"Підключення до Facebook з login={self.login}")

    def post_message(self, message: str):
        print(f"Публікація у Facebook: {message}")

# LinkedIn
class LinkedInNetwork(SocialNetwork):
    def __init__(self, email: str, password: str):
        self.email = email
        self.password = password
        self.connect()

    def connect(self):
        print(f"Підключення до LinkedIn з email={self.email}")

    def post_message(self, message: str):
        print(f"Публікація у LinkedIn: {message}")

# Абстрактна фабрика
class SocialNetworkFactory(ABC):
    @abstractmethod
    def create_network(self) -> SocialNetwork:
        pass

# Фабрика для Facebook
class FacebookFactory(SocialNetworkFactory):
    def __init__(self, login: str, password: str):
        self.login = login
        self.password = password

    def create_network(self) -> SocialNetwork:
        return FacebookNetwork(self.login, self.password)

# Фабрика для LinkedIn
class LinkedInFactory(SocialNetworkFactory):
    def __init__(self, email: str, password: str):
        self.email = email
        self.password = password

    def create_network(self) -> SocialNetwork:
        return LinkedInNetwork(self.email, self.password)

# --- Демонстрація роботи ---
if __name__ == "__main__":
    # Публікація у Facebook
    fb_factory = FacebookFactory(login="user_fb", password="pass123")
    fb_network = fb_factory.create_network()
    fb_network.post_message("Привіт, Facebook!")

    # Публікація у LinkedIn
    li_factory = LinkedInFactory(email="user_li@example.com", password="pass456")
    li_network = li_factory.create_network()
    li_network.post_message("Привіт, LinkedIn!")
