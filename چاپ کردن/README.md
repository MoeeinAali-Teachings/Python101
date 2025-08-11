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

# چاپ کردن در پایتون
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

