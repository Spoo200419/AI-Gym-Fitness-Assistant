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


def detect_squat():

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

        # Windows camera
        camera = cv2.VideoCapture(0, cv2.CAP_DSHOW)

        if not camera.isOpened():

            print("ERROR: Could not open camera.")

            return 0, 0

        print("Camera started successfully.")
        print("Do your squats.")
        print("Press Q to finish the workout.")

        start_time = time.time()

        frame_timestamp = 0

        squat_count = 0
        squat_state = "UP"

        window_name = "AI Gym - Squat Detection"

        cv2.namedWindow(
            window_name,
            cv2.WINDOW_NORMAL
        )

        while True:

            success, frame = camera.read()

            if not success:

                print("ERROR: Could not read camera frame.")

                break

            # Flip camera like a mirror
            frame = cv2.flip(frame, 1)

            rgb_frame = cv2.cvtColor(
                frame,
                cv2.COLOR_BGR2RGB
            )

            mp_image = mp.Image(
                image_format=mp.ImageFormat.SRGB,
                data=rgb_frame
            )

            result = landmarker.detect_for_video(
                mp_image,
                frame_timestamp
            )

            frame_timestamp += 1

            if result.pose_landmarks:

                landmarks = result.pose_landmarks[0]

                height, width, _ = frame.shape

                # Left side body landmarks
                hip = landmarks[23]
                knee = landmarks[25]
                ankle = landmarks[27]

                hip_point = (
                    int(hip.x * width),
                    int(hip.y * height)
                )

                knee_point = (
                    int(knee.x * width),
                    int(knee.y * height)
                )

                ankle_point = (
                    int(ankle.x * width),
                    int(ankle.y * height)
                )

                angle = calculate_angle(
                    hip_point,
                    knee_point,
                    ankle_point
                )

                # Draw points
                cv2.circle(
                    frame,
                    hip_point,
                    8,
                    (0, 255, 0),
                    -1
                )

                cv2.circle(
                    frame,
                    knee_point,
                    8,
                    (0, 255, 0),
                    -1
                )

                cv2.circle(
                    frame,
                    ankle_point,
                    8,
                    (0, 255, 0),
                    -1
                )

                # Draw body lines
                cv2.line(
                    frame,
                    hip_point,
                    knee_point,
                    (255, 255, 0),
                    3
                )

                cv2.line(
                    frame,
                    knee_point,
                    ankle_point,
                    (255, 255, 0),
                    3
                )

                form_feedback = "Keep Going"

                if angle < 100:

                    status = "SQUAT DOWN"

                    form_feedback = "Good Depth"

                    if squat_state == "UP":

                        squat_state = "DOWN"

                elif angle > 160:

                    status = "STANDING"

                    form_feedback = "Good Form"

                    if squat_state == "DOWN":

                        squat_count += 1

                        squat_state = "UP"

                else:

                    status = "MOVING"

                    form_feedback = "Keep Going"

                # Display information
                cv2.putText(
                    frame,
                    f"Knee Angle: {int(angle)}",
                    (30, 50),
                    cv2.FONT_HERSHEY_SIMPLEX,
                    1,
                    (0, 255, 0),
                    2
                )

                cv2.putText(
                    frame,
                    status,
                    (30, 100),
                    cv2.FONT_HERSHEY_SIMPLEX,
                    1,
                    (0, 255, 255),
                    2
                )

                cv2.putText(
                    frame,
                    f"Squat Reps: {squat_count}",
                    (30, 150),
                    cv2.FONT_HERSHEY_SIMPLEX,
                    1,
                    (255, 0, 0),
                    2
                )

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

                cv2.putText(
                    frame,
                    "No person detected",
                    (30, 50),
                    cv2.FONT_HERSHEY_SIMPLEX,
                    1,
                    (0, 0, 255),
                    2
                )

            # Show camera window
            cv2.imshow(
                window_name,
                frame
            )

            # Wait for keyboard input
            key = cv2.waitKey(10) & 0xFF

            if key == ord("q") or key == 27:

                print("Workout stopped by user.")

                break

        end_time = time.time()

        duration_minutes = round(
            (end_time - start_time) / 60,
            2
        )

        camera.release()

        cv2.destroyAllWindows()

        print("Squat repetitions:", squat_count)

        print(
            "Workout duration:",
            duration_minutes,
            "minutes"
        )

        return squat_count, duration_minutes