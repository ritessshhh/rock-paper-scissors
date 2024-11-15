import cv2
import mediapipe as mp
import time
import random

# Constants required as per mediapipe
FINGER_IDS = {'INDEX': 8, 'MIDDLE': 12, 'RING': 16, 'PINKY': 20}
MOVES = ["Rock", "Paper", "Scissors"]
WIN_CONDITIONS = {"Rock": "Scissors", "Paper": "Rock", "Scissors": "Paper"}

# Helper Functions
def get_finger_status(hand_landmarks, finger_name):
    """Check if a finger is extended. Returns True of it's extended else false"""
    tip = hand_landmarks.landmark[FINGER_IDS[finger_name]].y
    mcp = hand_landmarks.landmark[FINGER_IDS[finger_name] - 2].y
    return tip < mcp

def get_thumb_status(hand_landmarks):
    """Check if the thumb is extended. Returns True of it's extended else false"""
    thumb_tip = hand_landmarks.landmark[mp.solutions.hands.HandLandmark.THUMB_TIP].x
    thumb_ip = hand_landmarks.landmark[mp.solutions.hands.HandLandmark.THUMB_IP].x
    thumb_mcp = hand_landmarks.landmark[mp.solutions.hands.HandLandmark.THUMB_MCP].x
    return thumb_tip > thumb_ip > thumb_mcp

def detect_move(hand_landmarks):
    """Detect the player's move based on hand landmarks."""
    states = [
        "1" if get_thumb_status(hand_landmarks) else "0",
        "1" if get_finger_status(hand_landmarks, 'INDEX') else "0",
        "1" if get_finger_status(hand_landmarks, 'MIDDLE') else "0",
        "1" if get_finger_status(hand_landmarks, 'RING') else "0",
        "1" if get_finger_status(hand_landmarks, 'PINKY') else "0"
    ]
    gesture = "".join(states)
    return {
        "00000": "Rock",
        "11111": "Paper",
        "01100": "Scissors"
    }.get(gesture, "UNKNOWN")

def calculate_game_result(player_move):
    """Determine the game result."""
    computer_move = random.choice(MOVES)
    if player_move == computer_move:
        return 0, computer_move  # Draw
    if WIN_CONDITIONS[player_move] == computer_move:
        return 1, computer_move  # Player wins
    return -1, computer_move  # Player loses

# Main Game Function
def start_game():

    # IMPORT HAND AND DRAWING UTILS AND TURN ON WEBCAM
    mp_drawing = mp.solutions.drawing_utils
    mp_hands = mp.solutions.hands
    capture = cv2.VideoCapture(1)

    # GAME STATE VARIABLES

    # OPENING THE UTILS FOR HANDS
    with mp_hands.Hands(min_detection_confidence=0.7, min_tracking_confidence=0.4, max_num_hands=1) as hands:

        # LOOP OVER EACH FRAME
        while True:

            # CAPTURE EACH FRAME
            ret, frame = capture.read()

            # IF RET IS TRUE THAT MEANS IT FAILED TO CAPTURE
            if not ret:
                break

            # FLIP FRAME
            frame = cv2.flip(frame, 1)

            # TIMER LOGIC FOR COUNT DOWN

            # CONVERT THE BGR TO RGB AND DETECT HANDS IN EACH FRAME

            # IF HAND FETECTED THEN ITERATE OVER EACH FINGER'S MARKINGS

            # CALCULATE THE RESULTS ONLY IF HOLD_FOR_PLAY BUTTON IS PRESSED AND MOVE IS NOT UNKNOWN

            # RESULT TEXT DISPLAYED

            # CREATING NEW LABEL TO PLAY THE GAME AGAIN

            # PLAY AGAIN TEXT DISPLAYED

            # SHOW THE GENERATED AND ANALYSED FRAME
            cv2.imshow('Rock Paper Scissors!', frame)

            # IF ESC IS PRESSED IT QUITS, IF SPACE KEY IS PRESSED IT STARTS THE GAME.
            key = cv2.waitKey(1)
            if key == 32:  # Space Key
                timer_started, time_left_now = True, 3
                start_time = time.time()
            if key == 27:  # Escape Key
                break


    capture.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    start_game()