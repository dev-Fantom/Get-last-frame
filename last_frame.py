import cv2
import os


def get_max_frame_count(video_file):
    cap = cv2.VideoCapture(video_file)
    if not cap.isOpened():
        print(f"Error opening video file: {video_file}")
        return 0

    frame_count = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
    cap.release()
    return frame_count


def main(directory_path):
    video_info_list = []

    for filename in os.listdir(directory_path):
        if filename.endswith(".mp4"):
            video_file = os.path.join(directory_path, filename)
            max_frame_count = get_max_frame_count(video_file)
            video_info_list.append(
                {"filename": filename, "max_frame_count": max_frame_count}
            )

    sorted_video_info = sorted(video_info_list, key=lambda x: x["filename"])

    for video_info in sorted_video_info:
        filename = video_info["filename"]
        max_frame_count = video_info["max_frame_count"]
        print(f"{filename}, Max Frame Count: {max_frame_count}")


if __name__ == "__main__":
    video_directory = "video"
    main(video_directory)
