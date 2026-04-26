import cv2
import mediapipe as mp

print("Starting Hand Gesture Recognition...")

# Initialize MediaPipe
mp_hands = mp.solutions.hands
mp_draw = mp.solutions.drawing_utils

hands = mp_hands.Hands(
    max_num_hands=1,
    min_detection_confidence=0.7,
    min_tracking_confidence=0.7
)

# Start webcam
cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)

if not cap.isOpened():
    print("Camera not working")
    exit()

print("Press ESC to exit")

while True:
    ret, frame = cap.read()

    if not ret:
        print("Camera error")
        break

    # Flip for mirror effect
    frame = cv2.flip(frame, 1)

    # Convert to RGB
    rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    # Process hand detection
    result = hands.process(rgb)

    gesture = "No Hand"

    if result.multi_hand_landmarks:
        for idx, hand_landmarks in enumerate(result.multi_hand_landmarks):

            # Draw landmarks
            mp_draw.draw_landmarks(
                frame, hand_landmarks, mp_hands.HAND_CONNECTIONS
            )

            lm = hand_landmarks.landmark

            # Detect hand type (Left / Right)
            hand_label = result.multi_handedness[idx].classification[0].label

            tips = [4, 8, 12, 16, 20]
            fingers = []

            # 👍 Improved thumb logic
            if hand_label == "Right":
                fingers.append(1 if lm[4].x < lm[3].x else 0)
            else:
                fingers.append(1 if lm[4].x > lm[3].x else 0)

            # Other fingers
            for i in range(1, 5):
                if lm[tips[i]].y < lm[tips[i] - 2].y:
                    fingers.append(1)
                else:
                    fingers.append(0)

            # 🎯 Gesture classification
            if fingers == [0, 0, 0, 0, 0]:
                gesture = "Fist"

            elif fingers == [1, 0, 0, 0, 0]:
                gesture = "Thumbs Up"

            elif fingers == [0, 1, 0, 0, 0]:
                gesture = "One"

            elif fingers == [0, 1, 1, 0, 0]:
                gesture = "Peace"

            elif fingers == [1, 1, 0, 0, 1]:
                gesture = "Call Me"

            elif fingers == [0, 1, 1, 1, 0]:
                gesture = "Three"

            elif fingers == [1, 1, 1, 1, 1]:
                gesture = "Open Hand"

            else:
                gesture = "Unknown"

    # Display gesture
    cv2.putText(frame, gesture, (50, 100),
                cv2.FONT_HERSHEY_SIMPLEX, 1.5, (0, 255, 0), 3)

    # Show webcam
    cv2.imshow("Hand Gesture Recognition", frame)

    # Exit on ESC
    if cv2.waitKey(1) & 0xFF == 27:
        print("Exiting...")
        break

# Cleanup
cap.release()
