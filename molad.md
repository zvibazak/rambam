# רמב"ם הלכות קידוש החודש פרק שישי

* See full Python code [here](molad.py).

* The text is from [wikisource](https://he.wikisource.org/wiki/%D7%A8%D7%9E%D7%91%22%D7%9D_%D7%94%D7%9C%D7%9B%D7%95%D7%AA_%D7%A7%D7%99%D7%93%D7%95%D7%A9_%D7%94%D7%97%D7%95%D7%93%D7%A9_%D7%95)

* ראה להלן הגדרת המחלקה `Molad_date`.

## הלכה א
<p dir='rtl' align='right'>
בזמן שעושין על הראייה היו מחשבין ויודעין שעה שיתקבץ בו הירח עם החמה בדקדוק הרבה כדרך שהאיצטגנינין עושין. כדי לידע אם יראה הירח או לא יראה. ותחלת אותו החשבון הוא החשבון שמחשבין אותו בקירוב ויודעין שעת קיבוצן בלא דקדוק אלא במהלכם האמצעי הוא הנקרא מולד. ועיקרי החשבון שמחשבין בזמן שאין שם בית דין שיקבעו בו על הראייה והוא חשבון שאנו מחשבין היום הוא הנקרא עיבור.
</p>

## הלכה ב
<p dir='rtl' align='right'>
היום והלילה ארבע ועשרים שעות בכל זמן. שתים עשרה ביום ושתים עשרה בלילה. והשעה מחולקת לאלף ושמנים חלקים.
</p>

```python
HOURS_IN_DAY = 24
PARTS_IN_HOUR = 1080
```

<p dir='rtl' align='right'>
ולמה חלקו השעה למנין זה. לפי שמנין זה יש בו חצי ורביע ושמינית ושליש ושתות ותשע וחומש ועישור. והרבה חלקים יש לכל אלו השמות.
</p>

```python
import math

def divisorGenerator(n):
    res = []
    for i in range(1, int(math.sqrt(n) + 1)):
        if n % i == 0:
            res.append(i)
    return res 

print(divisorGenerator(1080))

# Output:
# [1, 2, 3, 4, 5, 6, 8, 9, 10, 12, 15, 18, 20, 24, 27, 30]
```

* ואגב, צ"ע הסדר שנקט הרמב"ם:

  `1/2, 1/4, 1/8, 1/3, 1/6, 1/9, 1/5, 1/10`


## הלכה ג
<p dir='rtl' align='right'>
משיתקבץ הירח והחמה לפי חשבון זה עד שיתקבצו פעם שנייה במהלכם האמצעי. תשעה ועשרים יום ושתים עשרה שעות מיום שלשים מתחלת לילו. ושבע מאות ושלשה ותשעים חלקים משעת שלש עשרה. וזה הוא הזמן שבין כל מולד ומולד וזה הוא חדשה של לבנה.
</p>

```python
moon_month = Molad_date(29,12,793, remove_days=False) #remove_days - to leave only the reminder from seven days or not.
print(f'Moon month is {moon_month}')

# Output:
# Moon month is 29 days, 12 hours and 793 parts
```
* עיין עוד: https://en.wikipedia.org/wiki/Lunar_month

## הלכה ד
<p dir='rtl' align='right'>
שנה של לבנה אם תהיה שנים עשר חדש מחדשים אלו יהיה כללה שלש מאות יום וארבעה וחמשים יום ושמנה שעות ושמנה מאות וששה ושבעים חלקים. 
</p>

```python
moon_year_regular = moon_month * 12
print(f'Moon year is {moon_year_regular}')

# Output:
# Moon year is 354 days, 8 hours and 876 parts
```

<p dir='rtl' align='right'>
ואם תהיה מעוברת ותהיה השנה שלשה עשר חדש יהיה כללה שלש מאות ושמנים ושלשה יום ואחת ועשרים שעות וחמש מאות ותשעה ושמנים חלקים. 
</p>

```python
moon_year_leap = moon_month * 13
print(f'Moon leap year is {moon_year_leap}')

# Output:
# Moon leap year is 383 days, 21 hours and 589 parts
```
<p dir='rtl' align='right'>
ושנת החמה היא שלש מאות חמשה וששים יום ושש שעות. 
</p>

```python
sun_year = Molad_date(365,6,0,remove_days=False)
print(f'Sun year is {sun_year}')

# Output:
# Sun year is 365 days, 6 hours and 0 parts
```
<p dir='rtl' align='right'>
נמצא תוספת שנת החמה על שנת הלבנה עשרה ימים ואחת ועשרים שעות ומאתים וארבעה חלקים.
</p>

```python
print(f'The diff between sun_year and moon_year is {sun_year-moon_year_regular}')

# Output:
# The diff between sun_year and moon_year is 10 days, 21 hours and 204 parts
```

## הלכה ה
<p dir='rtl' align='right'>
כשתשליך ימי חדש הלבנה שבעה שבעה שהן ימי השבוע. ישאר יום אחד ושתים עשרה שעות ושבע מאות ושלשה ותשעים חלקים. סימן להם אי"ב תשצ"ג. וזו היא שארית חדש הלבנה. 
</p>

```python
moon_month = Molad_date(29,12,793)
four_weeks = Molad_date(7*4, 0, 0)
print(f'Moon month reminder is {moon_month - four_weeks}')

# Output:
# Moon month reminder is 1 days, 12 hours and 793 parts
```
<p dir='rtl' align='right'>
וכן כשתשליך ימי שנת הלבנה שבעה שבעה. אם שנה פשוטה היא ישאר ממנה ארבעה ימים ושמנה שעות ושמנה מאות וששה ושבעים חלקים. סימן לה ד"ח תתע"ו. וזו היא שארית שנה פשוטה. 
</p>

```python
moon_year = moon_month * 12
print(f'Moon year reminder is {moon_year}')

# Output:
# Moon year reminder is 4 days, 8 hours and 876 parts
```
<p dir='rtl' align='right'>
ואם שנה מעוברת היא תהיה שאריתה חמשה ימים ואחת ועשרים שעות וחמש מאות ותשעה ושמנים חלקים. סימן להם הכ"א תקפ"ט.
</p>

```python
moon_year_leap = moon_month * 13
print(f'Moon leap year reminder is {moon_year_leap}')

# Output:
# Moon leap year reminder is 5 days, 21 hours and 589 parts
```

## הלכה ו
<p dir='rtl' align='right'>
כשיהיה עמך ידוע מולד חדש מן החדשים ותוסיף עליו אי"ב תשצ"ג יצא מולד שאחריו. ותדע באי זה יום מימי השבוע ובאי זו שעה ובכמה חלקים יהיה.
</p>

## הלכה ז
<p dir='rtl' align='right'>
כיצד הרי שהיה מולד ניסן באחד בשבת בחמש שעות ביום ומאה ושבעה חלקים סימן להם אהק"ז. כשתוסיף עליו שארית חדש הלבנה והוא אי"ב תשצ"ג. יצא מולד אייר בליל שלישי חמש שעות בלילה ותשע מאות חלקים. סימן להם ג"ה תת"ק. ועל דרך זו עד סוף העולם חדש אחר חדש.
</p>

* שימו לב: "חמש שעות ביום" זו היא השעה ה-17
```python
MOLAD_DIFF = Molad_date(1,12,793)
MOLAD_NISAN = Molad_date(1,5+12,107)
print(f'Iyar Molad is {MOLAD_NISAN + MOLAD_DIFF}')

# Output:
# Iyar Molad is 3 days, 5 hours and 900 parts
```

## הלכה ח
<p dir='rtl' align='right'>
וכן כשיהיה עמך ידוע מולד שנה זו ותוסיף שאריתה על ימי המולד. אם פשוטה היא שארית הפשוטה ואם מעוברת היא שארית המעוברת. יצא לך מולד שנה שלאחריה. וכן שנה אחר שנה עד סוף העולם. והמולד הראשון שממנו תתחיל הוא מולד שהיה בשנה הראשונה של יצירה.והוא היה בליל שני חמש שעות בלילה ומאתים וארבעה חלקים. סימן להם בהר"ד וממנו הוא תחלת החשבון.
</p>

```python
FIRST_MOLAD = Molad_date(2,5,204)
```

## הלכה ט
<p dir='rtl' align='right'>
בכל החשבונות האלו שתדע מהן המולד. כשתוסיף שארית עם שארית כשיתקבץ מן החלקים אלף ושמנים תשליך שעה אחת ותוסיף אותו למנין השעות. 
</p>

```python
if new_parts > PARTS_IN_HOUR:
	new_hours += new_parts // PARTS_IN_HOUR
	new_parts = new_parts % PARTS_IN_HOUR
```


<p dir='rtl' align='right'>
וכשיתקבץ מן השעות ארבע ועשרים תשליך יום ותוסיף ממנו למנין הימים. וכשיתקבץ מן הימים יותר על שבעה תשליך שבעה מן המנין ותניח השאר. 
</p>

```python
if new_hours > HOURS_IN_DAY: 
	new_days += new_hours // HOURS_IN_DAY
	new_hours = new_hours % HOURS_IN_DAY

if self.remove_days:
	new_days = new_days % DAYS
```

<p dir='rtl' align='right'>
שאין אנו מחשבין לידע מניין הימים אלא לידע באי זה יום מימי השבוע ובאי זה שעה ואי זה חלק יהיה המולד.
</p>

## הלכה י
<p dir='rtl' align='right'>
כל תשע עשרה שנה שיהיו מהן שבע שנים מעוברות ושתים עשרה פשוטות נקרא מחזור. ולמה סמכנו על מנין זה. שבזמן שאתה מקבץ מנין ימי שתים עשרה שנה פשוטות ושבע מעוברות ושעותיהן וחלקיהן ותשליך כל אלף ושמנים חלקים שעה. וכל ארבע ועשרים שעות יום. ותוסיף למנין הימים תמצא הכל תשע עשרה שנה משני החמה שכל שנה מהן שלש מאות וחמשה וששים יום ושש שעות בשוה. ולא ישאר ממנין ימי החמה בכל תשע עשרה שנה חוץ משעה אחת וארבע מאות ושמנים וחמשה חלקים. סימן להם אתפ"ה.
</p>

```python
CYCLE = 19
REGULAR_YEARS_IN_CYCLE = 12
LEAP_YEARS_IN_CYCLE = 7 

full_cycle_moon = moon_year * REGULAR_YEARS_IN_CYCLE + moon_year_leap * LEAP_YEARS_IN_CYCLE
sun_year = Molad_date(365,6,0)
full_cycle_sun = sun_year*CYCLE
print(f'Full cycle reminder is {full_cycle_sun-full_cycle_moon}')


# Output:
#Full cycle reminder is 0 days, 1 hours and 485 parts
```
* צ"ע למה צריך את זה? ראה לקמן פרק ט, ד

## הלכה יא
<p dir='rtl' align='right'>
נמצא במחזור שהוא כזה החדשים כולם חדשי הלבנה והשנים שני החמה. והשבע שנים המעוברות שבכל מחזור ומחזור לפי חשבון זה. הם שנה שלישית מן המחזור וששית ושמינית ושנת אחת עשרה ושנת ארבע עשרה ושנת שבע עשרה ושנת י"ט. סימן להם גו"ח י"א י"ד י"ז י"ט.
</p>

```python
is_leap = [False, False, True, False, False, True, False, True, False, False, True, False, False, True, False, False, True, False, True]
```

## הלכה יב
<p dir='rtl' align='right'>
כשתקבץ שארית כל שנה משתים עשרה שנה הפשוטות שהיא ד"ח תתע"ו. ושארית כל שנה משבע שנים המעוברות שהיא הכ"א תקפ"ט. ותשליך הכל שבעה שבעה ישאר שני ימים ושש עשרה שעות וחמש מאות וחמשה ותשעים חלקים. סימן להם בי"ו תקצ"ה. וזה הוא שארית המחזור.
</p>

```python
regular_reminder = Molad_date(4, 8,876)
leap_reminder = Molad_date(5, 21, 589)

full_cycle_reminder = regular_reminder*REGULAR_YEARS_IN_CYCLE + leap_reminder*LEAP_YEARS_IN_CYCLE
print(full_cycle_reminder)

# Output:
# 2 days, 16 hours and 595 parts
```

* אפשר לעשות את זה גם ככה, כנראה לרמב"ם לא היה מחשב אז הוא לא עשה ככה...
```python
full_cycle_reminder = moon_year * REGULAR_YEARS_IN_CYCLE + moon_year_leap * LEAP_YEARS_IN_CYCLE

print(full_cycle_reminder)

# Output:
# 2 days, 16 hours and 595 parts
```

## הלכה יג
<p dir='rtl' align='right'>
כשיהיה לך ידוע מולד תחלת מחזור ותוסיף עליו בי"ו תקצ"ה. יצא לך תחלת המחזור שאחריו. וכן מולד כל מחזור ומחזור עד סוף העולם. וכבר אמרנו שמולד תחלת המחזור הראשון היה לבהר"ד. ומולד השנה הוא מולד תשרי של אותה השנה.
</p>

* ראה דוגמא להלן

## הלכה יד
<p dir='rtl' align='right'>
ובדרך הזאת תדע מולד כל שנה ושנה שתרצה ומולד כל חדש וחדש שתרצה. משנים שעברו או משנים שעתידים לבא. כיצד תקח שני יצירה שעברו וגמרו ותעשה אותם מחזורין של תשע עשרה תשע עשרה שנה עד תשרי של אותה השנה. ותדע מנין המחזורין שעברו ומנין השנים שעברו ממחזור שעדיין לא נשלם. ותקח לכל מחזור ומחזור בי"ו תקצ"ה. ולכל שנה ושנה פשוטה משני המחזור שלא נשלם ד"ח תתע"ו. ולכל שנה מעוברת הכ"א תקפ"ט. ותקבץ הכל ותשליך החלקים שעות. ותשליך השעות ימים. והימים תשליכם שבעה שבעה. והנשאר מן הימים ומן השעות והחלקים הוא מולד שנה הבאה שתרצה לידע מולדה.
</p>

## הלכה טו
<p dir='rtl' align='right'>
מולד השנה שיצא בחשבון זה הוא מולד ראש חדש תשרי. וכשתוסיף עליו אי"ב תשצ"ג יצא מולד מרחשון. וכשתוסיף על מרחשון אי"ב תשצ"ג יצא מולד כסליו. וכן לכל חדש וחדש זה אחר זה עד סוף העולם
</p>

* דוגמא: "מולד חודש תשרי יהיה בליל שלישי 5 שעות ו 497 חלקים"
```python
FIRST_MOLAD = Molad_date(2,5,204)
full_cycle_reminder = Molad_date(2, 16, 595)
is_leap = [False, False, True, False, False, True, False, True, False, False, True, False, False, True, False, False, True, False, True]
regular_reminder = Molad_date(4, 8,876)
leap_reminder = Molad_date(5, 21, 589)
def get_molad(year):    
        full_cycles = year//CYCLE
        res = full_cycle_reminder * full_cycles
        print(res)

        for i in range(0,year%CYCLE-2):
                print (res)
                if is_leap[i]:
                        res = res + leap_reminder
                else:
                        res = res + regular_reminder
        return res 
correct_to_our_calender = Molad_date(0,6,0)
print(f'Tishri Molad will be on {get_molad(5782)+correct_to_our_calender}')
print(f'Heshvan Molad will be on {get_molad(5782)+Molad_date(1,12,793)-Molad_date(0,10,0)}')

# Output:
# Tishri Molad will be on 3 days, 5 hours and 497 parts
# Heshvan Molad will be on 4 days, 18 hours and 210 parts
```

## מחלקת עזר
```python
PARTS_IN_HOUR = 1080
HOURS_IN_DAY = 24
DAYS = 7

class Molad_date():
	def __init__(self, days, hours, parts, remove_days=True):
		self.days, self.hours, self.parts = days, hours, parts
		self.remove_days = remove_days

	def __add__(self, o):
		new_parts = self.parts + o.parts
		new_hours = self.hours + o.hours
		new_days = self.days + o.days

		if new_parts >= PARTS_IN_HOUR:
			new_hours += new_parts // PARTS_IN_HOUR
			new_parts = new_parts % PARTS_IN_HOUR

		if new_hours >= HOURS_IN_DAY: 
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
```
