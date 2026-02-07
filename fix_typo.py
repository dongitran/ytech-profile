# -*- coding: utf-8 -*-
import sys

# Read file
with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# The wrong character sequence: ở (o with horn and hook) + i
# The correct character sequence: ơ (o with horn) + ỉ (i with hook)

wrong_char = 'ở'  # This is o + horn + hook
correct_char = 'ơ'  # This is o + horn

# Also need to fix the i
wrong_i = 'i'  # regular i after ở
correct_i = 'ỉ'  # i with hook

# The pattern we want to replace: "Ngưởi" -> "Ngưởi"
# This means: N-g-ư-ở-i -> N-g-ư-ơ-ỉ

old_pattern = 'Ngưởi'  # ở (U+1EDF) + i
new_pattern = 'Ngưởi'  # ơ (U+01A1) + ỉ (U+1EC9)

print(f"Looking for: {old_pattern}")
print(f"Unicode: {[hex(ord(c)) for c in old_pattern]}")

print(f"\nReplacing with: {new_pattern}")
print(f"Unicode: {[hex(ord(c)) for c in new_pattern]}")

if old_pattern in content:
    content = content.replace(old_pattern, new_pattern)
    print("\nReplacement done!")
else:
    print("\nPattern not found!")

# Write back
with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)

# Verify
with open('index.html', 'r', encoding='utf-8') as f:
    verify = f.read()
    if new_pattern in verify:
        print("✓ Verified: New pattern is in file")
    else:
        print("✗ New pattern not found")
        
    if old_pattern in verify:
        print("✗ Old pattern still in file")
    else:
        print("✓ Old pattern removed")
