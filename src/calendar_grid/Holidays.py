# Sri Lanka Holidays
# https://www.cbsl.gov.lk/en/about/about-the-bank/bank-holidays-2025

from dataclasses import dataclass

from utils import Time, TimeFormat

HOLIDAYS = {
    2024: {
        12: {
            14: "Poya",
            25: "Christmas",
        }
    },
    2025: {
        1: {
            13: "Duruthu Poya",
            14: "Tamil Thai Pongal",
        },
        2: {
            4: "Independence",
            12: "Navam Poya",
            26: "Mahasivarathri",
        },
        3: {
            13: "Medin Poya",
            31: "Ramazan",
        },
        4: {
            12: "Bak Poya",
            13: "Prior to New Year",
            14: "New Year",
            18: "Good Friday",
        },
        5: {
            1: "May Day",
            12: "Vesak Poya",
            13: "After Vesak Poya",
        },
        6: {
            7: "Hadji",
            10: "Poson Poya",
        },
        7: {
            10: "Esala Poya",
        },
        8: {
            8: "Nikini Poya",
        },
        9: {
            5: "Prophet's Birthday",
            7: "Binara Poya",
        },
        10: {
            6: "Vap Poya",
            20: "Deepavali",
        },
        11: {
            5: "Ill Poya",
        },
        12: {
            4: "Unduvap Poya",
            25: "Christmas",
        },
    },
}


@dataclass
class Holidays:
    date: Time
    name: str

    @staticmethod
    def list():
        holidays = []
        for year, for_month in HOLIDAYS.items():
            for month, for_day in for_month.items():
                for day, name in for_day.items():
                    holidays.append(
                        Holidays(
                            date=TimeFormat.DATE.parse(
                                f"{year}-{month:02d}-{day:02d}"
                            ),
                            name=name,
                        )
                    )
        return holidays

    @staticmethod
    def idx():
        return {
            TimeFormat.DATE.format(h.date): h.name for h in Holidays.list()
        }

    @staticmethod
    def get_holiday(date: Time) -> str:
        return Holidays.idx().get(TimeFormat.DATE.format(date), None)
