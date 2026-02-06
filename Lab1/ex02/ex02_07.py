print("Nhập các dòng văn bản (nhập 'done' để kt): ")
lines = []
while True:
    line = input ()
    if line.lower() == 'done':
        break
    lines.append(line)
print("\nCac dòng đã nhập sẽ thành in hoa: ")
for line in lines:
    print(line.upper())