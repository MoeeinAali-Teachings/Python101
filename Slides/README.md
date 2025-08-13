---
marp: true
theme: beam
paginate: true
size: 16:9
header: مدرس: معین آعلی
footer: دوره‌ی آموزشی پایتون برای دانش‌آموزان
title: متغیرها در پایتون

---
<!-- _class: title -->

# Variables | متغیرها
<br/>

**مدرس: [معین آعلی](https://github.com/moeeinaali)**

**تابستان ۱۴۰۴**

---

# متغیر چیه؟


**ظرف‌هایی از جنس‌های مختلف برای نگه‌داری اطلاعات درون خودشان!**
<br/>

### چه جنس‌هایی؟

- اعداد
  - صحیح
  - اعشاری
  - مختلط
- رشته‌ها
- منطقی

---
# انواع متغیرها

![center](type-of-variables-in-python_thumbnail.webp)

---

# چطور متغیر تعریف کنیم؟


+ تو پایتون نیازی نیست از کلیدواژه‌ خاصی استفاده کنی!
+ می‌تونیم مثل ریاضی متغیرهاتو نامگذاری و تعریف کنی!

مثلا:

```Python
x = 5
y = 3.14
name = "moeein"
flag = True
```

---

# چطور متغیر تعریف کنیم؟


### نمیشه چندتایی تعریف کرد؟

```python
x, y, z = "Orange", "Banana", "Cherry"
print(x)
print(y)
print(z)
```

###### معلومه که میشه!

### نمیشه چندتارو همزمان یک مقدار داد؟

```python
x = y = z = "Orange"
print(x)
print(y)
print(z)
```

###### معلومه که میشه!

---

# نامگذاری متغیرها


### چیا مجازه؟

- حروف کوچک و بزرگ
- آندرلاین (ـ)
- اعداد

### چطور مجازه؟

```Python
a1 = 2
first_name = "moeein"
first_name1 = "mamad"
_name = "moeein"
_1 = 2
```

### چطور مجاز نیست؟
عدد اول اسم بیاد!

---

# نامگذاری متغیرها

#### حواستون به بزرگ و کوچیک بودن کارکترها باشه!

```Python
a = 2
A = 3
aA = 4
Aa = 5
```

```python
naMe = "moeein"
namE = "saeed"
NamE = "amir"
nAmE = "amirhossein"
```

---

# نامگذاری متغیرها

### چطور نامگذاری کنیم؟

![small](1651500050934.jpg)

---

# چاپ کردن

### چطور مقدار یک متغیر رو چاپ کنیم؟

```Python
name = "moeein"
print("moeein")

age = 22
print(age)

flag = True
print(flag)
```

---
<!-- _class: title -->

# Printing | چاپ کردن
<br/>

**مدرس: [معین آعلی](https://github.com/moeeinaali)**

**تابستان ۱۴۰۴**

---


# چاپ کردن

### چطور مقدار یک متغیر رو چاپ کنیم؟

```Python
name = "moeein"
print("moeein")

age = 22
print(age)

flag = True
print(flag)
```

---

# چاپ کردن

### فقط چاپ کردن متغیر مجازه؟

```Python
print("moeein")

print(-2)

print(True)
```

###### معلومه که نه!

---

# چاپ کردن

### حتما باید یدونه‌ای چاپ کنیم؟

```Python
print("moeein", "amirhossein", "saeed")

print(1, 2, 3)

print(True, False, True, False)
```

###### معلومه که نه!

---

# چاپ کردن

### نمیشه هم متغیر چاپ کرد هم مقدار؟

```Python
name = "moeein"
print(name, "amirhossein", "saeed")

age = 18
print(1, 2, 3, age)

flag = True
print(flag, False)
```

###### معلومه که میشه!

---

# کلیدهای خاص

## n\ : زدن یک enter (رفتن به خط بعد)
## t\ : زدن یک tab


#### مثال:

```python
print("moeein\naali")

print("1\n2\n3")

print("1\n\n2")
```


---

# پایان خاص برای چاپ کردن

پایان معمولی:

```python
print("moeein" , end="\n")
```

یک پایان خاص:

```python
print("moeein" , end="***\n")
```

یک پایان خیلی خاص:

```python
print("moeein" , end="\t***\t")
print("saeed" , end="\t***\t")
```

---
<!-- _class: title -->

# Comments | کامنت‌ها
<br/>

**مدرس: [معین آعلی](https://github.com/moeeinaali)**

**تابستان ۱۴۰۴**

---


# کامنت چیه؟

**در پایتون، کامنت (Comment) متنی است که داخل کد نوشته می‌شود ولی توسط مفسر اجرا نمی‌شود.**

<br/>
<br/>

### هدف اصلی کامنت‌ها:

- توضیح کد برای خودت یا دیگران

- خواناتر کردن برنامه

- غیرفعال کردن موقت یک بخش از کد برای تست یا اشکال‌زدایی

---

# چطور کامنت بذاریم؟

## کامنت تک خطی:

```python
# This is a comment

print("Hello, World!")
```

##### حتی میشه کامنت رو جلو یک کد نوشت:

```python
print("Hello, World!") # This is a comment 
```
---

# چطور کامنت بذاریم؟

## کامنت چند خطی:

```python
# This is a comment
# written in
# more than one line

print("Hello, World!")
```

```python
"""
This is a comment
written in
more than one line
"""

print("Hello, World!")
```
---

<!-- _class: title -->

# Casting | تبدیل نوع داده


<br/>

**مدرس: [معین آعلی](https://github.com/moeeinaali)**

**تابستان ۱۴۰۴**

---
# یادآوری: انواع داده‌ها در پایتون

- اعداد صحیح (int)
- اعداد اعشاری (float)
- متغیر منطقی (bool)
- رشته (str)

```python
a = 2 # int

b = 2.2 # float

c = "2" # str

d = "moeein" # str

e = "#$%@#$^%GVEARFHGBEA4534Cfwefgw" # str
```

---

# تبدیل به int

#### تبدیل int به int:

```python
x = int(1)   # x will be 1
```

#### تبدیل float به int:
```python
y = int(2.9999) # y will be 2

y = int(2.0) # y will be 2
```

#### تبدیل str به int:
```python
z = int("3") # z will be 3

z = int("123m") # Error!
```

---

# تبدیل به float

#### تبدیل int به float:

```python
x = float(1)     # x will be 1.0
```

#### تبدیل float به float:
```python
y = float(2.8)   # y will be 2.8
```

#### تبدیل str به float:
```python
z = float("3")   # z will be 3.0

w = float("4.2") # w will be 4.2

p = float("4.2m") # Error!
```
---

# تبدیل به str


#### تبدیل float به str:

```python
a = str(1.2)
```

#### تبدیل int به str:

```python
b = str(1)
```

#### تبدیل str به str:

```python
b = str("1") 
```

---

# تبدیل به bool

#### تبدیل str به bool:

```python
print(bool("")) # False
print(bool("others")) # True
```

#### تبدیل int به bool:

```python
print(bool(0)) # False
print(bool(1)) # True
print(bool(-1)) # True
```

#### تبدیل float به bool:

```python
print(bool(0.0)) # False
print(bool(1.1)) # True
print(bool(-2.1)) # True
```

---

# تبدیل از bool

#### تبدیل bool به int:

```python
print(int(True)) # 1
print(int(False)) # 0
```

#### تبدیل bool به float:

```python
print(float(True)) # 1.0
print(float(False)) # 0.0
```

#### تبدیل bool به str:

```python
print(str(True)) # "True"
print(str(False)) # "False"
```

---

<!-- _class: title -->

# Input | ورودی گرفتن
<br/>

**مدرس: [معین آعلی](https://github.com/moeeinaali)**

**تابستان ۱۴۰۴**

---

# ورودی گرفتن تکی

### رشته:

```python
name = input() # "moeein aali"
print(name) # "moeein aali"
```

### عدد صحیح:

```python
age = int(input()) # "18"
print(age) # 18
```

### عدد اعشاری:

```python
height = float(input()) # "12.3"
print(height) # 12.3
```

**نکته مهم: همه ورودی‌های کاربر به صورت `Str` هستند!**

---

# چاپ راهنما

### استفاده از `print`:

```python
print("please enter your name:")

name = input()

print("Hello",name,end="!\n")
```

### استفاده از آرگومان `input`:

```python
name = input("please enter your name:")

print("Hello",name,end="!\n")
```

---

# Split

**کاربرد: جداسازی یک Str توسط یک Str دیگر بر حسب یک الگوی مشخص**

###### مثال ۱:

```python
full_name = "moeein aali"
first_name, last_name = full_name.split(" ")
```

###### مثال ۲:

```python
names = "moeein amirhossein saeed"
name1 , name2 , name3 = names.split(" ")
```

###### مثال ۳:

```python
names = "moeein amirhossein saeed"
name1 , name2 , name3 = names.split()
```

---

# Split

###### مثال ۴:

```python
names = "moeein|amirhossein|saeed"
name1 , name2 , name3 = names.split("|")
```

###### مثال ۵:

```python
names = "moeein|amirhossein|saeed"
seperator = "|"
name1 , name2 , name3 = names.split(seperator)
```

---

# Split: جدا کردن به تعداد محدود

#### نمونه:
```python
txt = "apple#banana#cherry#orange"

a , b = txt.split("#", 1) # apple , banana#cherry#orange

m , n , p = txt.split("#", 2) # apple , banana , cherry#orange
```

---

# ورودی گرفتن چندتایی


### رشته:

```python
name1 , name = input().split()
```

### عدد صحیح:

```python
num1 , num2 = int(input().split()) # Error!
```

---

# Map

![center](map_function.png)

---

# Map



```python
num1 , num2 = map(int , input().split())

num3 , num4 = map(float , input().split())
```

نکات مهم:

- اگه ورودی‌ها عدد نباشن کد خطا میده!
- اگه به جای چند تا متغیر، یدونه متغیر قرار بدیم،‌همه ورودی‌ها در قالب یک **لیست** ذخیره می‌شن. در فصل‌های بعد با لیست و کاربردهای اون آشنا می‌شیم...

---

<!-- _class: title -->

# Operators | عملگر‌ها

<br/>

**مدرس: [معین آعلی](https://github.com/moeeinaali)**

**تابستان ۱۴۰۴**

---

# عملگرهای محاسباتی

![center2](image.png)

---

# عملگرهای انتسابی

![center2](assignment-operator-in-python.png)

---

# عملگرهای مقایسه‌ای

![center2](image-1.png)

---

# عملگرهای منطقی

![center](logical-operators.png)

---

# عملگرهای منطقی

![center2](nl0W8.jpg)

---

# عملگرهای هویت

![center](identity-operators.png)

---

# عملگرهای هویت

#### مثال:

```python
a = True 

print(a is True) # True
print(a is not False) # False
```

---

# عملگرهای عضویت


![center](membership-operators.png)


---

# عملگرهای عضویت


```python
good_numbers = [1,2,3,4]

print(1 in good_numbers) # True

print(5 not in good_numbers) # True

print(5 in good_numbers) # False

```

---

# عملگرهای بیتی (معرفی)

![center2](Bitwise-Operators-in-Python.webp)

---


<!-- _class: title -->

# Lists | لیست‌ها

<br/>

**مدرس: [معین آعلی](https://github.com/moeeinaali)**

**تابستان ۱۴۰۴**

---

# Lists

#### کاربرد:
- ذخیره‌ی تعدادی داده، داخل یک متغیر

```python
items = ["apple", "banana", "cherry"]
print(items)

items2 = ["moeein", 1, True, -1.1]
print(items2)
```

#### خصوصیات:

- ترتیب ثابت
- آیتم‌های قابل تغییر
- امکان وجود آیتم تکراری
- امکان وجود آیتم‌ها با تایپ‌های مختلف

---

# Lists

![center2](image-2.png)

---

# List Length

- به دست آوردن تعداد عضوهای یک لیست
- به دست آوردن طول یک لیست

```python
thislist = ["apple", "banana", "apple"]

print(len(thislist)) # 3
```

--- 

# Access List Items

- دسترسی به عضو `n`ام از یک لیست

**نکته: شروع `index`ها از 0 است.**

```python
thislist = ["apple", "banana", "cherry"]

print(thislist[0]) # banana
print(thislist[1]) # apple
print(thislist[2]) # cherry
```
---

# Negative Indexing
#### ایندکس منفی

- شروع از انتها
  - ایندکس `1-` یعنی عضو آخر لیست
  - ایندکس `2-` یعنی عضو یکی مانده به آخر لیست
  - ...

```python
thislist = ["apple", "banana", "cherry"]

print(thislist[-1]) # cherry
```

---


# Range of Indexes

- `list[start:end]`

```python
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]

print(thislist[2:5]) # ["cherry", "orange", "kiwi", "melon"]
```

- `list[start:end:index]`

```python
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]

print(thislist[2:5]) # ["cherry", "orange", "kiwi", "melon"]
```

---


# Change Item Value

- برای تغییر دادن یک آیتم‌ خاص از لیست، کافیه که مثل متغیرها به اون آیتم مقدار جدید `assign` کنیم.

```python
thislist = ["apple", "banana", "cherry"]

thislist[1] = "blackcurrant"

print(thislist)
```


---

# Change a Range of Item Values

- برای تغییر دادن یک رنج از لیست، نیازه که یک لیست جدید با طول برابر با رنج مورد نظر با مقادیر جدید ایجاد کنیم. سپس آن رنج را در لیست مد نظر `assign` کنیم.

<br/>

```python
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]

thislist[1:3] = ["blackcurrant", "watermelon"]

print(thislist)
```

- **دقت کنید که طول رنج انتخاب شده با طول لیست جدید یکی باشد!**


---

# Append Items

- این متد، مقدار جدید را به انتهای لیست اضافه می‌کند.

```python
thislist = ["apple", "banana", "cherry"]

thislist.append("orange")

print(thislist) # ['apple', 'banana', 'cherry', 'orange']
```

---

# Insert Items

- این متد، مقدار جدید را دقیقا در ایندکس مورد نظر قرار می‌دهد و باقی اعضای لیست را شیفت می‌دهد.


```python
thislist = ["apple", "banana", "cherry"]

thislist.insert(2, "watermelon")

print(thislist) # ['apple', 'banana', 'watermelon', 'cherry']
```

---

# Extend List

- این متد یک لیست دیگر را به انتهای لیست فعلی اضافه می‌کند. عملکرد مشابه به `append` دارد با این تفاوت که ورودی آن به یک مقدار، لیستی از مقادیر است.


```python
list1 = ["apple", "banana", "cherry"]

list2 = ["mango", "pineapple", "papaya"]

list1.extend(list2)

print(list1) # ['apple', 'banana', 'cherry', 'mango', 'pineapple', 'papaya']
```

---

# Extend List

- روش دوم:

```python
list1 = ["apple", "banana", "cherry"]

list2 = ["mango", "pineapple", "papaya"]

list3 = list1 + list2

print(list3) # ['apple', 'banana', 'cherry', 'mango', 'pineapple', 'papaya']
```

---

# Remove Specified Item

- برای این کار از متد `remove` استفاده می‌کنیم.

```python
thislist = ["apple", "banana", "cherry"]

thislist.remove("banana")

print(thislist)
```

- اگر بیشتر از یک مقدار وجود داشته باشد که با ورودی `remove`‌ یکی باشد، این متد فقط اولین عضو را عضو می‌کند.

```python
thislist = ["apple", "banana", "cherry", "banana", "kiwi"]

thislist.remove("banana")

print(thislist)
```

---

# Remove Specified Index

- برای این کار از متد `pop` استفاده می‌کنیم.
- این متد مقدار عضو شده را `return` هم می‌کند.

```python
thislist = ["apple", "banana", "cherry"]
a = thislist.pop(1)

print(thislist) # ["apple", "cherry"]
print(a) # banana
```

- اگر به این متد ورودی ندیم، آخرین عضو لیست را حذف می‌کند.

```python
thislist = ["apple", "banana", "cherry"]
a = thislist.pop()

print(a) # cherry
print(thislist) # ["apple", "banana"]
```

---

# Clear the List

- متد `clear` تمامی عضوهای لیست را عضو می‌کند.

```python
thislist = ["apple", "banana", "cherry"]

thislist.clear()

print(thislist) # []
```


---

# Sort Lists

- مرتب‌سازی برحسب حروف و اعداد (صعودی):

```python
thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]

thislist.sort()

print(thislist) # ['banana', 'kiwi', 'mango', 'orange', 'pineapple']
```

- برعکس(نزولی):
```python
thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]

thislist.sort(reverse = True)

print(thislist) # ['pineapple', 'orange', 'mango', 'kiwi', 'banana']
```

---

# Copy Lists

```python
thislist = ["apple", "banana", "cherry"]
```

- روش اول:

```python
mylist = thislist.copy()
print(mylist)
```
- روش دوم:
```python
mylist = list(thislist)
print(mylist)
```

- روش سوم:
```python
mylist = thislist[:]
print(mylist)
```
---

# another methods

- `count`
  - تعداد آیتم‌هایی که برابر با مقدار ورودی باشن.

- `index`
  - ایندکس اولین آیتمی که برابر باشه با مقدار ورودی

- `reverse`
  - لیست را برعکس می‌کند و روی همان ذخیره می‌کند

- `reversed()`
  - برعکس‌شده‌ی یک لیست را برمی‌گرداند.
