
import cv2
import mediapipe as mp
import os
import math
import time


BaseOptions = mp.tasks.BaseOptions
PoseLandmarker = mp.tasks.vision.PoseLandmarker
PoseLandmarkerOptions = mp.tasks.vision.PoseLandmarkerOptions
VisionRunningMode = mp.tasks.vision.RunningMode


def calculate_angle(a, b, c):

    angle = math.degrees(
        math.atan2(c[1] - b[1], c[0] - b[0])
        - math.atan2(a[1] - b[1], a[0] - b[0])
    )

    angle = abs(angle)

    if angle > 180:
        angle = 360 - angle

    return angle


def detect_pushup():

    model_path = os.path.join(
        os.path.dirname(__file__),
        "pose_landmarker_lite.task"
    )

    options = PoseLandmarkerOptions(
        base_options=BaseOptions(
            model_asset_path=model_path
        ),
        running_mode=VisionRunningMode.VIDEO,
        num_poses=1
    )

    with PoseLandmarker.create_from_options(options) as landmarker:

        # Open Windows camera
        camera = cv2.VideoCapture(0, cv2.CAP_DSHOW)

        if not camera.isOpened():

            print("ERROR: Could not open camera.")

            return 0, 0

        print("Camera started successfully.")
        print("Do your push-ups.")
        print("Press Q to finish the workout.")

        # Start timer
        start_time = time.time()

        frame_timestamp = 0

        pushup_count = 0
        pushup_state = "UP"

        window_name = "AI Gym - Push-up Detection"

        cv2.namedWindow(
            window_name,
            cv2.WINDOW_NORMAL
        )

        while True:

            success, frame = camera.read()

            if not success:

                print("ERROR: Could not read camera frame.")

                break

            # Mirror camera
            frame = cv2.flip(frame, 1)

            # Convert BGR to RGB
            rgb_frame = cv2.cvtColor(
                frame,
                cv2.COLOR_BGR2RGB
            )

            mp_image = mp.Image(
                image_format=mp.ImageFormat.SRGB,
                data=rgb_frame
            )

            # Detect pose
            result = landmarker.detect_for_video(
                mp_image,
                frame_timestamp
            )

            frame_timestamp += 1

            if result.pose_landmarks:

                landmarks = result.pose_landmarks[0]

                height, width, _ = frame.shape

                # Left shoulder
                shoulder = landmarks[11]

                # Left elbow
                elbow = landmarks[13]

                # Left wrist
                wrist = landmarks[15]

                shoulder_point = (
                    int(shoulder.x * width),
                    int(shoulder.y * height)
                )

                elbow_point = (
                    int(elbow.x * width),
                    int(elbow.y * height)
                )

                wrist_point = (
                    int(wrist.x * width),
                    int(wrist.y * height)
                )

                # Calculate elbow angle
                angle = calculate_angle(
                    shoulder_point,
                    elbow_point,
                    wrist_point
                )

                # Draw shoulder point
                cv2.circle(
                    frame,
                    shoulder_point,
                    8,
                    (0, 255, 0),
                    -1
                )

                # Draw elbow point
                cv2.circle(
                    frame,
                    elbow_point,
                    8,
                    (0, 255, 0),
                    -1
                )

                # Draw wrist point
                cv2.circle(
                    frame,
                    wrist_point,
                    8,
                    (0, 255, 0),
                    -1
                )

                # Draw shoulder-elbow line
                cv2.line(
                    frame,
                    shoulder_point,
                    elbow_point,
                    (255, 255, 0),
                    3
                )

                # Draw elbow-wrist line
                cv2.line(
                    frame,
                    elbow_point,
                    wrist_point,
                    (255, 255, 0),
                    3
                )

                form_feedback = "Keep Going"

                # Push-up detection
                if angle < 90:

                    status = "DOWN"

                    form_feedback = "Good Depth"

                    if pushup_state == "UP":

                        pushup_state = "DOWN"

                elif angle > 160:

                    status = "UP"

                    form_feedback = "Good Form"

                    if pushup_state == "DOWN":

                        pushup_count += 1

                        pushup_state = "UP"

                else:

                    status = "MOVING"

                    form_feedback = "Keep Going"

                # Display elbow angle
                cv2.putText(
                    frame,
                    f"Elbow Angle: {int(angle)}",
                    (30, 50),
                    cv2.FONT_HERSHEY_SIMPLEX,
                    1,
                    (0, 255, 0),
                    2
                )

                # Display status
                cv2.putText(
                    frame,
                    status,
                    (30, 100),
                    cv2.FONT_HERSHEY_SIMPLEX,
                    1,
                    (0, 255, 255),
                    2
                )

                # Display push-up count
                cv2.putText(
                    frame,
                    f"Push-up Reps: {pushup_count}",
                    (30, 150),
                    cv2.FONT_HERSHEY_SIMPLEX,
                    1,
                    (255, 0, 0),
                    2
                )

                # Display form feedback
                cv2.putText(
                    frame,
                    f"Form: {form_feedback}",
                    (30, 200),
                    cv2.FONT_HERSHEY_SIMPLEX,
                    1,
                    (0, 255, 255),
                    2
                )

            else:

                # No person detected
                cv2.putText(
                    frame,
                    "No person detected",
                    (30, 50),
                    cv2.FONT_HERSHEY_SIMPLEX,
                    1,
                    (0, 0, 255),
                    2
                )

            # Display camera
            cv2.imshow(
                window_name,
                frame
            )

            # Keyboard control
            key = cv2.waitKey(10) & 0xFF

            if key == ord("q") or key == 27:

                print("Workout stopped by user.")

                break

        # Calculate workout duration
        end_time = time.time()

        duration_minutes = round(
            (end_time - start_time) / 60,
            2
        )

        # Close camera
        camera.release()

        cv2.destroyAllWindows()

        print(
            "Push-up repetitions:",
            pushup_count
        )

        print(
            "Workout duration:",
            duration_minutes,
            "minutes"
        )

        return pushup_count, duration_minutes


if __name__ == "__main__":

    detect_pushup()

