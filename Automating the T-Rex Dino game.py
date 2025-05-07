import pyautogui
import time
from PIL import ImageGrab
import numpy as np

# Define the area where the game is being displayed (you may need to adjust these values)
GAME_AREA = (100, 300, 700, 400)  # x1, y1, x2, y2 coordinates of the area to capture

# Color range of obstacles (cactus in the game is usually dark green)
OBSTACLE_COLOR = (83, 83, 83)  # RGB value of the color representing the cactus

# Time interval between screenshots and actions
SLEEP_INTERVAL = 0.1

def check_for_obstacle():
    # Capture a screenshot of the defined game area
    screenshot = ImageGrab.grab(bbox=GAME_AREA)
    
    # Convert the screenshot to a numpy array
    img = np.array(screenshot)
    
    # Convert the image to grayscale for easier processing (Optional)
    # img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    
    # Search for the obstacle color in the image
    # In this case, we're looking for dark spots (representing the cactus or other obstacles)
    for x in range(0, img.shape[1], 5):  # Scan every 5th pixel for efficiency
        for y in range(0, img.shape[0], 5):
            # If the pixel matches the obstacle color
            if tuple(img[y, x]) == OBSTACLE_COLOR:
                return True  # Obstacle detected
    return False  # No obstacle detected

def jump():
    # Simulate pressing the spacebar (jump)
    pyautogui.press('space')
    print("Jumped!")

def main():
    print("Starting T-Rex Game automation... Press Ctrl+C to stop.")
    while True:
        # Check for obstacles in the game area
        if check_for_obstacle():
            print("Obstacle detected!")
            jump()  # Jump if an obstacle is detected
        time.sleep(SLEEP_INTERVAL)

if __name__ == "__main__":
    main()
