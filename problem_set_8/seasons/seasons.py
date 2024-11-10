from datetime import date
import re
import sys
import inflect

p = inflect.engine()


class Season:
    def __init__(self, date_of_birth):
        self.date_of_birth = date_of_birth

    @property
    def date_of_birth(self):
        return self._date_of_birth

    @date_of_birth.setter
    def date_of_birth(self, date_of_birth):
        if not self.is_valid_date(date_of_birth):
            sys.exit("Invalid date")
        self._date_of_birth = date_of_birth

    def is_valid_date(self, date_string):
        pattern = r"^\d{4}-(0[1-9]|1[0-2])-(0[1-9]|[12][0-9]|3[01])$"
        return bool(re.match(pattern, date_string))

    def get_age_in_minutes(self):
        today = date.today()
        birth_day = date.fromisoformat(self.date_of_birth)
        age = today - birth_day
        return round(age.total_seconds() / 60)

    def seasons_of_love(self):
        minutes = self.get_age_in_minutes()
        words = p.number_to_words(minutes, andword="")
        text = f"{words.capitalize()} minutes"
        return text


def main():
    date_of_birth = input("Date of Birth: ")
    season = Season(date_of_birth)
    print(season.seasons_of_love())


if __name__ == "__main__":
    main()
