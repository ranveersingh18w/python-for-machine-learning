import numpy as np

marks = np.array([
    [80, 70, 90],
    [60, 85, 75],
    [90, 95, 85],
    [40, 50, 60]
])

# 1. Dataset shape
print(marks.shape)

# 2. Average of each student
print(np.mean(marks, axis=1))

# 3. Average of each subject
print(np.mean(marks, axis=0))

# 4. Highest mark
print(np.max(marks))

# 5. Students with average >= 75
avg = np.mean(marks, axis=1)
print(marks[avg >= 75])

# 6. Normalize marks to 0–1
normalized = marks / 100
print(normalized)