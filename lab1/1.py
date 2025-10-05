from abc import ABC, abstractmethod

# Патерн Singleton
class SingletonMeta(type):
    _instances = {}
    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            instance = super().__call__(*args, **kwargs)
            cls._instances[cls] = instance
        return cls._instances[cls]

# Абстрактний клас сховища
class Storage(ABC):
    @abstractmethod
    def upload_file(self, file_name: str, data: str):
        pass

    @abstractmethod
    def download_file(self, file_name: str) -> str:
        pass

    @abstractmethod
    def list_files(self):
        pass

# Локальне сховище
class LocalStorage(Storage):
    def __init__(self):
        self.files = {}

    def upload_file(self, file_name: str, data: str):
        self.files[file_name] = data
        print(f"Файл '{file_name}' завантажено в локальне сховище")

    def download_file(self, file_name: str) -> str:
        return self.files.get(file_name, "Файл не знайдено")

    def list_files(self):
        return list(self.files.keys())

# Сховище Amazon S3 (демонстрація)
class S3Storage(Storage):
    def __init__(self):
        self.files = {}

    def upload_file(self, file_name: str, data: str):
        self.files[file_name] = data
        print(f"Файл '{file_name}' завантажено в S3")

    def download_file(self, file_name: str) -> str:
        return self.files.get(file_name, "Файл не знайдено в S3")

    def list_files(self):
        return list(self.files.keys())

# Менеджер файлів користувача (Singleton)
class UserFileManager(metaclass=SingletonMeta):
    def __init__(self, storage: Storage):
        self.storage = storage

    def upload(self, file_name: str, data: str):
        self.storage.upload_file(file_name, data)

    def download(self, file_name: str) -> str:
        return self.storage.download_file(file_name)

    def list_files(self):
        return self.storage.list_files()


if __name__ == "__main__":
    # Користувач обирає локальне сховище
    local_storage = LocalStorage()
    manager1 = UserFileManager(local_storage)
    manager1.upload("file1.txt", "Привіт, світ!")
    print(manager1.list_files())

    # Користувач змінює сховище на S3
    s3_storage = S3Storage()
    manager2 = UserFileManager(s3_storage)  
    manager2.upload("file2.txt", "Дані для S3")
    print(manager2.list_files())

    # Щоб змінити сховище, можна додати метод зміни storage
    manager1.storage = s3_storage
    manager1.upload("file2.txt", "Дані для S3")
    print(manager1.list_files())
