from abc import ABC, abstractmethod

from models.profile import Profile


class ProfileRepository(ABC):
    @abstractmethod
    def get_profile(self, user_id: int) -> Profile | None:
        pass

    @abstractmethod
    def create_profile(self):
        pass


class ProfileService:
    def __init__(self, repository: ProfileRepository):
        self.__repository = repository

    def create_profile(self, user_id: int):
        pass
