from pydantic import BaseModel, field_validator, computed_field

class Profile(BaseModel):
    age: int
    weight: float
    height: float

    @field_validator("age")
    def validate_age(cls, v: int):
        if v <= 0:
            return ValueError("Возраст должен быть больше нуля")
        return v
    
    @field_validator("weight")
    def validate_weight(cls, v: float):
        if v <= 0:
            return ValueError("Вес должен быть больше нуля")
        return v
    
    @field_validator("height")
    def validatge_height(cls, v: float):
        if v <= 0:
            return ValueError("Рост должен быть больше нуля")
        return v
    
    @computed_field
    def formatted_data(self) -> str:
        return "Возраст: %5d\nВес:    %6.2f\nРост:   %6.2f\n" % (self.age, self.weight, self.height)