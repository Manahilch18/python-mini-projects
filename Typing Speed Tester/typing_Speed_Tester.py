import random
import time

sentences = [
    "Python is a powerful programming language.",
    "Practice makes perfect in coding.",
    "Artificial intelligence is changing the world.",
    "Learning Python is fun and useful.",
    "Consistency is the key to success."
]
sentence = random.choice(sentences)

print("\n===== Typing Speed Tester =====")
print("\nType the following sentence:\n")
print(sentence)
input("\nPress Enter when ready...")

start_time = time.time()
typed_text = input("\nStart typing:\n")
end_time = time.time()
time_taken = end_time - start_time
# Calculate WPM
words = len(typed_text.split())
wpm = (words / time_taken) * 60
# Count mistakes
mistakes = 0
for i in range(min(len(sentence), len(typed_text))):
    if sentence[i] != typed_text[i]:
        mistakes += 1
mistakes += abs(len(sentence) - len(typed_text))
accuracy = ((len(sentence) - mistakes) / len(sentence)) * 100
print("\n===== RESULTS =====")

print(f"Time Taken : {time_taken:.2f} seconds")
print(f"Words Per Minute (WPM): {wpm:.2f}")
print(f"Mistakes : {mistakes}")
print(f"Accuracy : {accuracy:.2f}%")