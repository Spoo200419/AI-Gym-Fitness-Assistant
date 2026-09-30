import cv2
import mediapipe as mp
import os


# MediaPipe Tasks
BaseOptions = mp.tasks.BaseOptions
PoseLandmarker = mp.tasks.vision.PoseLandmarker
PoseLandmarkerOptions = mp.tasks.vision.PoseLandmarkerOptions
VisionRunningMode = mp.tasks.vision.RunningMode


def detect_pose():

    # Path to pose model
    model_path = os.path.join(
        os.path.dirname(__file__),
        "pose_landmarker_lite.task"
    )

    # Pose model configuration
    options = PoseLandmarkerOptions(
        base_options=BaseOptions(
            model_asset_path=model_path
        ),
        running_mode=VisionRunningMode.VIDEO,
        num_poses=1
    )

    # Create pose detector
    with PoseLandmarker.create_from_options(options) as landmarker:

        camera = cv2.VideoCapture(0)

        if not camera.isOpened():
            print("Error: Could not open camera.")
            return

        print("Camera started successfully.")
        print("Press Q to close.")

        frame_timestamp = 0

        while True:

            success, frame = camera.read()

            if not success:
                print("Could not read camera frame.")
                break

            # OpenCV uses BGR, MediaPipe uses RGB
            rgb_frame = cv2.cvtColor(
                frame,
                cv2.COLOR_BGR2RGB
            )

            # Convert frame to MediaPipe image
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

            # Draw detected landmarks
            if result.pose_landmarks:

                for landmarks in result.pose_landmarks:

                    for landmark in landmarks:

                        height, width, _ = frame.shape

                        x = int(landmark.x * width)
                        y = int(landmark.y * height)

                        cv2.circle(
                            frame,
                            (x, y),
                            5,
                            (0, 255, 0),
                            -1
                        )

            cv2.imshow(
                "AI Gym - Pose Detection",
                frame
            )

            if cv2.waitKey(1) & 0xFF == ord("q"):
                break

        camera.release()
        cv2.destroyAllWindows()


if __name__ == "__main__":
    detect_pose()