text ="HelloWorld"
chunk_size = 5

for i in range(0, len(text), chunk_size):
    chunk = text[i:i + chunk_size]
    print(f"Index {i}: {chunk}")


