import cv2
import mediapipe as mp
import time
import math

class PoseDetector:
    def __init__(self, mode=False, upper_body=False, smooth=True, detection_confidence=0.5, tracking_confidence=0.5):
        self.mode = mode
        self.upper_body = upper_body
        self.smooth = smooth
        self.detection_confidence = detection_confidence
        self.tracking_confidence = tracking_confidence

        self.mp_draw = mp.solutions.drawing_utils
        self.mp_pose = mp.solutions.pose
        self.pose = self.mp_pose.Pose(
            static_image_mode=self.mode,
            model_complexity=1 if self.upper_body else 0,
            smooth_landmarks=self.smooth,
            min_detection_confidence=self.detection_confidence,
            min_tracking_confidence=self.tracking_confidence
        )

    def find_pose(self, img, draw=True):
        """Detects the pose in the provided image."""
        img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        self.results = self.pose.process(img_rgb)
        if self.results.pose_landmarks and draw:
            self.mp_draw.draw_landmarks(img, self.results.pose_landmarks, self.mp_pose.POSE_CONNECTIONS)
        return img

    def find_position(self, img, draw=True):
        """Finds and returns the positions of landmarks."""
        self.lm_list = []
        if self.results.pose_landmarks:
            for idx, lm in enumerate(self.results.pose_landmarks.landmark):
                h, w, c = img.shape
                cx, cy = int(lm.x * w), int(lm.y * h)
                self.lm_list.append([idx, cx, cy])
                if draw:
                    cv2.circle(img, (cx, cy), 5, (255, 0, 0), cv2.FILLED)
        return self.lm_list

    def find_angle(self, img, p1, p2, p3, draw=True):
        """Finds and returns the angle formed by three landmarks."""
        if len(self.lm_list) > max(p1, p2, p3):
            x1, y1 = self.lm_list[p1][1:]
            x2, y2 = self.lm_list[p2][1:]
            x3, y3 = self.lm_list[p3][1:]

            # Calculate the angle
            angle = math.degrees(math.atan2(y3 - y2, x3 - x2) -
                                 math.atan2(y1 - y2, x1 - x2))
            if angle < 0:
                angle += 360

            if draw:
                cv2.line(img, (x1, y1), (x2, y2), (255, 255, 255), 3)
                cv2.line(img, (x3, y3), (x2, y2), (255, 255, 255), 3)

                for x, y in [(x1, y1), (x2, y2), (x3, y3)]:
                    cv2.circle(img, (x, y), 10, (0, 0, 255), cv2.FILLED)
                    cv2.circle(img, (x, y), 15, (0, 0, 255), 2)

                cv2.putText(img, f'{int(angle)}°', (x2 - 50, y2 + 50),
                            cv2.FONT_HERSHEY_PLAIN, 2, (0, 0, 255), 2)

            return angle
        return None


def main():
    cap = cv2.VideoCapture(0)
    previous_time = 0
    detector = PoseDetector()

    while cap.isOpened():
        success, img = cap.read()
        if not success:
            print("Failed to capture video.")
            break

        img = detector.find_pose(img)
        landmarks = detector.find_position(img, draw=False)

        if landmarks:
            print(f"Landmark 14 (Right Elbow): {landmarks[14]}")
            cv2.circle(img, (landmarks[14][1], landmarks[14][2]), 15, (0, 0, 255), cv2.FILLED)

        current_time = time.time()
        fps = 1 / (current_time - previous_time) if (current_time - previous_time) > 0 else 0
        previous_time = current_time

        cv2.putText(img, f'FPS: {int(fps)}', (70, 50), cv2.FONT_HERSHEY_PLAIN, 3, (255, 0, 0), 3)
        cv2.imshow("Pose Detection", img)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()


if __name__ == "__main__":
    main()
