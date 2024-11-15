import cv2
import mediapipe as mp
import time
from main import detect_move, calculate_game_result
def start_game():
    ## IMPORT HAND AND DRAWING UTILS AND TURN ON WEBCAM
    mp_drawing = mp.solutions.drawing_utils
    mp_hands = mp.solutions.hands
    capture = cv2.VideoCapture(0)

    # GAME STATE VARIABLES
    timer_started, hold_for_play = False, False
    game_over_text, computer_played = "", ""
    start_time, time_left_now = 0, 3

    # OPENING THE UTILS FOR HANDS
    with mp_hands.Hands(min_detection_confidence=0.7, min_tracking_confidence=0.4, max_num_hands=1) as hands:
        # LOOP OVER EACH FRAME
        while True:
            # CAPTURE EACH FRAME
            ret, frame = capture.read()
            # FLIP FRAME
            frame = cv2.flip(frame, 1)
            if not ret:
                break

            # TIMER LOGIC FOR COUNT DOWN
            if timer_started:
                elapsed = time.time() - start_time
                if elapsed >= 1:
                    time_left_now -= 1
                    start_time = time.time()
                    if time_left_now <= 0:
                        hold_for_play = True
                        timer_started = False

            # CONVERT THE BGR TO RGB AND DETECT HANDS IN EACH FRAME
            results = hands.process(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))
            player_move = "UNKNOWN"

            # IF HAND FETECTED THEN ITERATE OVER EACH FINGER'S MARKINGS
            if results.multi_hand_landmarks:
                for hand_landmarks in results.multi_hand_landmarks:
                    # DRAW LINES TO SHOW HAND IS DETECTED AND DETECT THE MOVE
                    mp_drawing.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)
                    player_move = detect_move(hand_landmarks)

            # CALCULATE THE RESULTS ONLY IF HOLD_FOR_PLAY BUTTON IS PRESSED AND MOVE IS NOT UNKNOWN
            if hold_for_play and player_move != "UNKNOWN":
                hold_for_play = False
                game_result, computer_move = calculate_game_result(player_move)
                computer_played = f"You: {player_move} | Computer: {computer_move}"
                game_over_text = ["It's a draw!", "You've won!", "You've lost!"][game_result]

            # RESULT TEXT DISPLAYED
            cv2.putText(frame, game_over_text + " " + computer_played, (10, 450), cv2.FONT_HERSHEY_COMPLEX, 0.75,
                        (255, 255, 255), 2)

            # CREATING NEW LABEL TO PLAY THE GAME AGAIN
            label = "PLAY NOW!" if hold_for_play else f"STARTING IN {time_left_now}" if timer_started else "PRESS SPACE TO START!"

            # PLAY AGAIN TEXT DISPLAYED
            cv2.putText(frame, label, (150, 50), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 255, 255), 2)

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