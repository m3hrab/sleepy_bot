import pyautogui
import time
import random
import webbrowser

# Ask the user how many tabs they want to open (1-3)
num_tabs = int(input("How many tabs do you want to open (1-3)? "))

urls = [
    'https://www.fiverr.com/inbox',
    'https://www.fiverr.com/mehrab_2435',
    'https://www.fiverr.com/users/mehrab_2435/manage_gigs'
]

for i in range(num_tabs):
    webbrowser.open(urls[i])
    time.sleep(2 + i * 3)  # Incremental sleep time: 2s, 5s, 8s

def move_mouse_randomly():
    """Move the mouse in a human-like manner."""
    screen_width, screen_height = pyautogui.size()
    # Randomly choose a point on the screen within a reasonable range
    x = random.randint(100, screen_width - 100)
    y = random.randint(100, screen_height - 100)
    duration = random.uniform(0.5, 2.5)  # Random speed of mouse movement
    pyautogui.moveTo(x, y, duration=duration)
    print(f"Moved mouse to ({x}, {y}) in {duration:.2f} seconds.")
    
def refresh_current_tab():
    """Refresh the current browser tab."""
    pyautogui.hotkey('ctrl', 'r')  # Simulate refresh
    print("Refreshed the current tab")

def switch_to_next_tab(tab_number):
    """Switch to the next browser tab."""
    if tab_number == 1:
        pyautogui.hotkey('ctrl', '2')  # Move to Tab 2
    elif tab_number == 2:
        pyautogui.hotkey('ctrl', '3')  # Move to Tab 3
    else:
        pyautogui.hotkey('ctrl', '1')  # Move back to Tab 1
        
    print("Switched to currect tab")

def random_scroll():
    """Scroll randomly up or down the page."""
    # Randomly choose the scroll amount (positive for down, negative for up)
    scroll_amount = random.randint(-200, 200)  # Scroll amount can be adjusted
    pyautogui.scroll(scroll_amount)
    print(f"Scrolled {'down' if scroll_amount > 0 else 'up'} by {abs(scroll_amount)} units.")

def run_auto_refresher():
    """Run the tab switching and refreshing logic."""
    current_tab = 1
    start_time = time.time()
    max_runtime = 5 * 60 * 60  # 5 hours in seconds

    while (time.time() - start_time) < max_runtime:
        
        move_mouse_randomly()  # Simulate natural cursor movement
        
        if random.random() > 0.7:
            refresh_current_tab()  # Refresh the current active tab
        
            # Randomized delay between 1 and 5 minutes
            delay = random.randint(60, 300)
            print(f"Waiting for {delay} seconds before next action...")
            time.sleep(delay)

        if random.random() > 0.3:
            # Perform random scrolling
            random_scroll()
            delay = random.randint(40, 150)
            print(f"Waiting for {delay} seconds before next action...")
            time.sleep(delay)
        
        if random.random() > 0.6:
            # Switch to the next tab in a cyclic manner
            switch_to_next_tab(current_tab)
            current_tab = random.randint(1,3) #(current_tab % 3) + 1  # Cycle between 1, 2, and 3
            delay = random.randint(20, 120)
            print(f"Waiting for {delay} seconds before next action...")
            time.sleep(delay)

if __name__ == "__main__":
    run_auto_refresher()
