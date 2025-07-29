from dataclasses import dataclass


@dataclass
class User:
    email: str
    password: str

    def __post_init__(self):
        if not self.email:
            raise ValueError("Email is required")
        if not self.password:
            raise ValueError("Password is required")

        if "@" not in self.email:
            raise ValueError("Email Invalid")