text = input("текст: ")
print(f"длина: {len(text)}")
lower_text = text.lower()
print(f"в ниж рег: {lower_text}")
count = 0
vow = "aeiou"
for vow in lower_text:
    if vow in vow:
        count += 1
print("кол-во гласных: ", count)
print("замена: ", lower_text.replace("ugly", "beauty"))
print("'The': ", text.startswith("The"))
print("'End': ", text.endswith("end"))
