class InvalidAgeError(Exception):
    pass



def check_age(age):
    if age<18:
        raise InvalidAgeError("Age must be 18 or above")
    return "Allowed"
print(check_age(15))
