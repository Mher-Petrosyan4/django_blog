from django.db.models import IntegerChoices


class GenderChoice(IntegerChoices):
    FEMALE = 0, "F"
    Male = 1, "M"


class StatusChoice(IntegerChoices):
    NEW = 0, "New"
    DOING = 1, "Doing"
    Done = 2, "Done"
