# Jenish's Mega Quiz - 8 Questions
print("--- Welcome to Jenish's 8-Question Challenge ---")
score = 0

# Questions ki list
questions = [
    ["Python kya hai?", "a) Programming Language", "b) Saanp ka naam", "a"],
    ["Website banane ke liye kya use kiya?", "a) Flask", "b) Instagram", "a"],
    ["Variable kya hota hai?", "a) Ek box", "b) Ek error", "a"],
    ["Print karne ke liye kya likhte hain?", "a) display()", "b) print()", "b"],
    ["User se puchne ke liye kya use hota hai?", "a) input()", "b) take()", "a"],
    ["Coding kahan likh rahe ho?", "a) Pydroid 3", "b) WhatsApp", "a"],
    ["Aapka naam kya hai?", "a) Jenish", "b) Rahul", "a"],
    ["Kya aap coder ban gaye ho?", "a) Haan", "b) Nahi", "a"]
]

# Loop jo har sawaal ko ek-ek karke puchega
for q in questions:
    print("\n" + q[0])
    print(q[1])
    print(q[2])
    ans = input("Jawab (a/b): ").lower()
    
    if ans == q[3]:
        print("Sahi! ✅")
        score += 1
    else:
        print("Galat! ❌")

print("\n--- Final Score ---")
print(f"Jenish, aapka score hai: {score}/8")

if score >= 6:
    print("Shabash! Aap pro ban rahe ho. 🏆")
else:
    print("Thodi aur mehnat karo Jenish! 💪")
