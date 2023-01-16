#  python-holidays
#  ---------------
#  A fast, efficient Python library for generating country, province and state
#  specific sets of holidays on the fly. It aims to make determining whether a
#  specific date is a holiday as fast and flexible as possible.
#
#  Authors: dr-prodigy <dr.prodigy.github@gmail.com> (c) 2017-2023
#           ryanss <ryanssdev@icloud.com> (c) 2014-2017
#  Website: https://github.com/dr-prodigy/python-holidays
#  License: MIT (see LICENSE file)

from datetime import date

from dateutil.easter import easter
from dateutil.relativedelta import relativedelta as rd

from holidays.constants import JAN, MAR, APR, MAY, AUG, OCT, NOV, DEC, MON
from holidays.constants import TUE, THU
from holidays.holiday_base import HolidayBase


class Hungary(HolidayBase):
    """
    https://en.wikipedia.org/wiki/Public_holidays_in_Hungary
    Codification dates:
      - https://hvg.hu/gazdasag/20170307_Megszavaztak_munkaszuneti_nap_lett_a_nagypentek  # noqa
      - https://www.tankonyvtar.hu/hu/tartalom/historia/92-10/ch01.html#id496839
    """

    country = "HU"

    def _populate(self, year: int) -> None:
        super()._populate(year)

        # New year
        self._add_with_observed_day_off(
            date(year, JAN, 1), "Újév", before=False, since=2014
        )

        # National Day
        if 1945 <= year <= 1950 or 1989 <= year:
            self._add_with_observed_day_off(
                date(year, MAR, 15), "Nemzeti ünnep"
            )

        # Soviet era
        if 1950 <= year <= 1989:
            # Proclamation of Soviet socialist governing system
            self[
                date(year, MAR, 21)
            ] = "A Tanácsköztársaság kikiáltásának ünnepe"
            # Liberation Day
            self[date(year, APR, 4)] = "A felszabadulás ünnepe"
            # Memorial day of The Great October Soviet Socialist Revolution
            if year not in {1956, 1989}:
                self[
                    date(year, NOV, 7)
                ] = "A nagy októberi szocialista forradalom ünnepe"

        easter_date = easter(year)

        # Good Friday
        if 2017 <= year:
            self[easter_date + rd(days=-2)] = "Nagypéntek"

        # Easter
        self[easter_date] = "Húsvét"

        # Second easter day
        if 1955 != year:
            self[easter_date + rd(days=+1)] = "Húsvét Hétfő"

        # Pentecost
        self[easter_date + rd(days=+49)] = "Pünkösd"

        # Pentecost monday
        if year <= 1952 or 1992 <= year:
            self[easter_date + rd(days=+50)] = "Pünkösdhétfő"

        # International Workers' Day
        if 1946 <= year:
            self._add_with_observed_day_off(
                date(year, MAY, 1), "A Munka ünnepe"
            )
        if 1950 <= year <= 1953:
            self[date(year, MAY, 2)] = "A Munka ünnepe"

        # State Foundation Day (1771-????, 1891-)
        if 1950 <= year <= 1989:
            self[date(year, AUG, 20)] = "A kenyér ünnepe"
        else:
            self._add_with_observed_day_off(
                date(year, AUG, 20), "Az államalapítás ünnepe"
            )

        # National Day
        if 1991 <= year:
            self._add_with_observed_day_off(
                date(year, OCT, 23), "Nemzeti ünnep"
            )

        # All Saints' Day
        if 1999 <= year:
            self._add_with_observed_day_off(
                date(year, NOV, 1), "Mindenszentek"
            )

        # Christmas Eve is not endorsed officially
        # but nowadays it is usually a day off work
        if (
            self.observed
            and 2010 <= year
            and not self._is_weekend(year, DEC, 24)
        ):
            self[date(year, DEC, 24)] = "Szenteste"

        # First christmas
        self[date(year, DEC, 25)] = "Karácsony"

        # Second christmas
        if 1955 != year:
            self._add_with_observed_day_off(
                date(year, DEC, 26),
                "Karácsony másnapja",
                since=2013,
                before=False,
            )

        # New Year's Eve
        # Since 2014, the last day of the year is an observed day off if New
        # Year's Day falls on a Tuesday.
        if (
            self.observed
            and 2014 <= year
            and date(year, DEC, 31).weekday() == MON
        ):
            self[date(year, DEC, 31)] = "Szilveszter"

    def _add_with_observed_day_off(
        self,
        day: date,
        desc: str,
        since: int = 2010,
        before: bool = True,
        after: bool = True,
    ) -> None:
        # Swapped days off were in place earlier but
        # I haven't found official record yet.
        self[day] = desc
        # TODO: should it be a separate flag?
        if self.observed and since <= day.year:
            if day.weekday() == TUE and before:
                self[day + rd(days=-1)] = desc + " előtti pihenőnap"
            elif day.weekday() == THU and after:
                self[day + rd(days=+1)] = desc + " utáni pihenőnap"


class HU(Hungary):
    pass


class HUN(Hungary):
    pass
