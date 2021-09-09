PARTS_IN_HOUR = 1080
HOURS_IN_DAY = 24
DAYS = 7

CYCLE = 19
REGULAR_YEARS_IN_CYCLE = 12
LEAP_YEARS_IN_CYCLE = 7
is_leap = [False, False, True, False, False, True, False, True, False, False, True, False, False, True, False, False, True, False, True]

class Molad_date():
	def __init__(self, days, hours, parts, remove_days=True):
		self.days, self.hours, self.parts = days, hours, parts
		self.remove_days = remove_days

	def __add__(self, o):
		new_parts = self.parts + o.parts
		new_hours = self.hours + o.hours
		new_days = self.days + o.days

		if new_parts > PARTS_IN_HOUR:
			new_hours += new_parts // PARTS_IN_HOUR
			new_parts = new_parts % PARTS_IN_HOUR

		if new_hours > HOURS_IN_DAY: 
			new_days += new_hours // HOURS_IN_DAY
			new_hours = new_hours % HOURS_IN_DAY

		if new_parts<0:
			new_hours -= 1
			new_parts += PARTS_IN_HOUR

		if new_hours<0:
			new_days -= 1
			new_hours += HOURS_IN_DAY

		if self.remove_days:
			new_days = new_days % DAYS

		return Molad_date(new_days, new_hours, new_parts)

	def __sub__(self, o):
		return self+Molad_date(-o.days,-o.hours,-o.parts)

	def __mul__(self,  times: int):
		new_res=self
		for x in range(1, times):
			new_res = self+new_res
		return new_res

	def __str__(self):
		return f'{self.days} days, {self.hours} hours and {self.parts} parts'

def get_molad(year):    
        full_cycles = year//CYCLE
        res = full_cycle_reminder * full_cycles

        for i in range(0,year%CYCLE-2):
                if is_leap[i]:
                        res = res + leap_reminder
                else:
                        res = res + regular_reminder
        return res 

FIRST_MOLAD = Molad_date(2,5,204)

moon_month = Molad_date(29,12,793, remove_days=False)
print(f'Moon month is {moon_month}')

moon_year_regular = moon_month * 12
print(f'Moon year is {moon_year_regular}')

moon_year_leap = moon_month * 13
print(f'Moon leap year is {moon_year_leap}')

sun_year = Molad_date(365,6,0,remove_days=False)
print(f'Sun year is {sun_year}')

print(f'The diff between sun_year and moon_year is {sun_year-moon_year_regular}')

moon_month = Molad_date(29,12,793)
four_weeks = Molad_date(7*4, 0, 0)
print(f'Moon month reminder is {moon_month - four_weeks}')

moon_year = moon_month * 12
print(f'Moon year reminder is {moon_year}')

moon_year_leap = moon_month * 13
print(f'Moon leap year reminder is {moon_year_leap}')

MOLAD_DIFF = Molad_date(1,12,793)
MOLAD_NISAN = Molad_date(1,5+12,107)
print(f'Iyar Molad is {MOLAD_NISAN + MOLAD_DIFF}')

full_cycle_moon = moon_year * REGULAR_YEARS_IN_CYCLE + moon_year_leap * LEAP_YEARS_IN_CYCLE
sun_year = Molad_date(365,6,0)
full_cycle_sun = sun_year*CYCLE
print(f'Full cycle reminder is {full_cycle_sun-full_cycle_moon}')

regular_reminder = Molad_date(4, 8,876)
leap_reminder = Molad_date(5, 21, 589)

full_cycle_reminder = regular_reminder*REGULAR_YEARS_IN_CYCLE + leap_reminder*LEAP_YEARS_IN_CYCLE
print(full_cycle_reminder)

full_cycle_reminder = moon_year * REGULAR_YEARS_IN_CYCLE + moon_year_leap * LEAP_YEARS_IN_CYCLE
print(full_cycle_reminder)

full_cycle_reminder = Molad_date(2, 16, 595)
regular_reminder = Molad_date(4, 8,876)
leap_reminder = Molad_date(5, 21, 589)

correct_to_our_calender = Molad_date(0,6,0)
print(f'Tishri Molad will be on {get_molad(5782)+correct_to_our_calender}')
print(f'Heshvan Molad will be on {get_molad(5782)+Molad_date(1,12,793)-Molad_date(0,10,0)}')
