import random

# ১. অবজেক্টিভ ফাংশন (আমরা চাই এই ফাংশনের ম্যাক্সিমাম ভ্যালু বের করতে)
# উদাহরণ: f(x) = -x^2 + 4 (একটি উল্টানো প্যারাবোলা, যার পিক হলো x=0 তে)
def objective_function(x):
    return - (x ** 2) + 4

# ২. হিল ক্লাম্বিং অ্যালগরিদম
def hill_climbing(start_x, step_size, max_iterations):
    current_x = start_x
    current_val = objective_function(current_x)
    
    print(f"Starting at x = {current_x}, Value = {current_val}")

    for i in range(max_iterations):
        # নেইবার বা প্রতিবেশী তৈরি করা (বামে এবং ডানে)
        neighbor_left = current_x - step_size
        neighbor_right = current_x + step_size
        
        val_left = objective_function(neighbor_left)
        val_right = objective_function(neighbor_right)
        
        # চেক করা: কোনো প্রতিবেশী কি বর্তমানের চেয়ে ভালো?
        if val_left > current_val and val_left > val_right:
            current_x = neighbor_left
            current_val = val_left
            print(f"Iter {i+1}: Moving Left -> x = {current_x:.4f}, Value = {current_val:.4f}")
            
        elif val_right > current_val and val_right > val_left:
            current_x = neighbor_right
            current_val = val_right
            print(f"Iter {i+1}: Moving Right -> x = {current_x:.4f}, Value = {current_val:.4f}")
            
        else:
            # যদি কোনো প্রতিবেশীই ভালো না হয়, তার মানে আমরা পিকে (Peak) পৌঁছে গেছি
            print("Found Peak (Local Maxima). Stopping.")
            break
            
    return current_x, current_val

# ৩. ড্রাইভার কোড
start_solution = random.randint(-10, 10) # র‍্যান্ডমলি শুরু করা
final_x, final_val = hill_climbing(start_x=start_solution, step_size=0.5, max_iterations=50)

print(f"\nFinal Solution: Best x = {final_x:.4f}, Maximum Value = {final_val:.4f}")