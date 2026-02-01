scores = [78, 92, 85, 60, 88]

passed = []

for s in scores:
    if s >= 80:
        passed.append(s)

print("80点以上:", passed)