items = input("")
batch = input("")

if not batch.isdigit():
    raise Exception("Batch must be number")
else:
    batch = int(batch)

vowels = "aeiou"
items_length = len(items)

if items_length < batch:
    raise Exception("Batch must be less than no of items")

counter = 0
devices = 0
total_devices = 0
while (counter + batch) <= items_length:
    for i in range(counter, counter + batch):
        if items[i] in vowels:
            devices += 1
    if total_devices < devices:
        total_devices = devices

    devices = 0
    counter += 1

print(total_devices)
