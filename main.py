import cv2 as cv
import mediapipe as mp
import time

def main():
    # Initialize video capture and mediapipe pose detection
    cap = cv.VideoCapture(0)
    mp_pose = mp.solutions.pose
    pose = mp_pose.Pose()
    mp_draw = mp.solutions.drawing_utils

    # Drawing specifications for landmarks and connections
    line_spec = mp_draw.DrawingSpec(color=(0, 255, 0), thickness=3)  # Green lines
    circle_spec = mp_draw.DrawingSpec(color=(0, 0, 255), thickness=2, circle_radius=5)  # Red circles

    p_time = 0

    while True:
        # Capture frame from webcam
        success, img = cap.read()
        if not success:
            print("Unable to read from webcam. Exiting...")
            break

        # Convert the image to RGB for processing
        img_rgb = cv.cvtColor(img, cv.COLOR_BGR2RGB)
        results = pose.process(img_rgb)

        # Check for pose landmarks
        if results.pose_landmarks:
            for id, lm in enumerate(results.pose_landmarks.landmark):
                h, w, c = img.shape
                cx, cy = int(lm.x * w), int(lm.y * h)
                print(f"Landmark ID: {id}, Coordinates: ({cx}, {cy})")

            # Draw pose landmarks and connections on the image
            mp_draw.draw_landmarks(
                img, results.pose_landmarks, mp_pose.POSE_CONNECTIONS,
                circle_spec, line_spec
            )

        # Calculate and display FPS
        c_time = time.time()
        fps = 1 / (c_time - p_time)
        p_time = c_time
        cv.putText(img, f"FPS: {int(fps)}", (10, 70), cv.FONT_HERSHEY_PLAIN, 3, (255, 255, 0), 3)

        # Show the output image
        cv.imshow("Pose Detection", img)

        # Break loop if 'q' is pressed
        if cv.waitKey(10) & 0xFF == ord('q'):
            break

    # Release resources
    cap.release()
    cv.destroyAllWindows()

if __name__ == "__main__":
    main()
