Rock Paper Scissors Hand Gesture Game
=====================================

This project is a hand gesture recognition game that allows players to play "Rock Paper Scissors" using their hand gestures. It uses the MediaPipe library for hand detection and OpenCV to capture video from the camera.

Contents:
---------
1. Requirements
2. Installation
3. How It Works
4. Functions Explained
5. Usage

Requirements:
-------------
- Python 3.7+
- OpenCV
- MediaPipe
- A computer with a webcam

Installation:
-------------
1. Clone the repository:
```bash
   git clone https://github.com/ritessshhh/rock-paper-scissors.git
   cd rock-paper-scissors
```

2. Install the dependencies:
```bash
   pip install -r requirements.txt
```

How It Works:
-------------
This application captures video from the webcam and uses MediaPipe's hand landmarks detection to interpret hand gestures as "Rock," "Paper," or "Scissors." Once the player’s move is detected, the computer randomly selects a move, and the game outcome is displayed on the screen.

Functions Explained:
--------------------

1. ```get_finger_status(hand_landmarks, finger_name)```
   - Purpose: Determines if a specific finger (index, middle, ring, pinky) is extended.
   - Parameters:
     - hand_landmarks: The detected hand landmarks from MediaPipe.
     - finger_name: The name of the finger to check (INDEX, MIDDLE, RING, or PINKY).
   - Returns: True if the finger is extended, False otherwise.
   - Explanation: Compares the y-coordinates of the finger's tip and MCP joint to detect extension.

2. ```get_thumb_status(hand_landmarks)```
   - Purpose: Checks if the thumb is extended.
   - Parameters:
     - hand_landmarks: The detected hand landmarks from MediaPipe.
   - Returns: True if the thumb is extended, False otherwise.
   - Explanation: Uses x-coordinates to detect if the thumb tip is extended.

3. ```detect_move(hand_landmarks)```
   - Purpose: Detects the player's move (Rock, Paper, or Scissors) based on hand landmarks.
   - Parameters:
     - hand_landmarks: The detected hand landmarks from MediaPipe.
   - Returns: A string indicating the player's move (Rock, Paper, Scissors, or UNKNOWN).
   - Explanation: Combines thumb and finger statuses into a gesture pattern to interpret the move.

4. ```calculate_game_result(player_move)```
   - Purpose: Determines the result of the game.
   - Parameters:
     - player_move: The move made by the player (Rock, Paper, or Scissors).
   - Returns: A tuple with the result (1 for win, -1 for loss, 0 for draw) and the computer's move.
   - Explanation: Randomly selects a move for the computer and compares it with the player's move to determine the result.

5. ```start_game()```
   - Purpose: Main function that initializes the webcam and runs the game loop.
   - Explanation: Captures video, detects hand landmarks, interprets moves, and displays game results. Manages game states like the timer and handles keypresses to start or end the game.

Usage:
------
1. Run the script:
   python main.py

2. Press the spacebar to start the game countdown.

3. Show one of the following hand gestures:
   - Rock: All fingers down
   - Paper: All fingers up
   - Scissors: Index and middle fingers up

4. The game result will be displayed on the screen.

5. Press the escape key (Esc) to exit the game.

Enjoy playing Rock, Paper, Scissors using your hand gestures!