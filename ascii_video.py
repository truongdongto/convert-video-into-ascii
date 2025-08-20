import cv2
import os
import sys
import time
import numpy as np

def frame_to_ascii(frame, width=120, height=40):
    """
    Convert a video frame to ASCII art.
    
    Args:
        frame: OpenCV frame (BGR image)
        width: Width of ASCII output (characters)
        height: Height of ASCII output (lines)
    
    Returns:
        String representation of the frame in ASCII art
    """
    # ASCII characters from darkest to lightest
    ascii_chars = "@%#*+=-:. "
    
    # Convert BGR to grayscale
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
    # Resize frame to desired ASCII dimensions
    resized = cv2.resize(gray, (width, height))
    
    # Normalize pixel values to 0-255 range
    normalized = cv2.normalize(resized, None, 0, 255, cv2.NORM_MINMAX)
    
    # Convert to ASCII
    ascii_frame = ""
    for row in normalized:
        ascii_row = ""
        for pixel in row:
            # Map pixel intensity (0-255) to ASCII character index
            char_index = int(pixel * (len(ascii_chars) - 1) / 255)
            ascii_row += ascii_chars[char_index]
        ascii_frame += ascii_row + "\n"
    
    return ascii_frame

def ascii_img():
    # This function can be removed as it's not used
    return ['first_ascii_img', 'second_ascii_img']

def get_terminal_size():
    """Get terminal dimensions for optimal ASCII sizing"""
    try:
        size = os.get_terminal_size()
        return size.columns, size.lines - 2  # Leave some space for messages
    except:
        return 120, 40  # Default fallback

def main(video_path, max_duration=None, fps=25):
    """
    Reads a video and converts each frame into ASCII art.
    Then, it plays the ASCII art video in the terminal.
    """
    
    cap = cv2.VideoCapture(video_path)
    
    if not cap.isOpened():
        print(f"Error: Could not open video file at {video_path}")
        return

    # Get optimal ASCII dimensions based on terminal size
    term_width, term_height = get_terminal_size()
    ascii_width = min(term_width, 120)
    ascii_height = min(term_height, 40)

    video_fps = cap.get(cv2.CAP_PROP_FPS) or 25
    interval = max(1, int(video_fps // fps))
    total_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
    
    max_frames = total_frames
    if max_duration:
        max_frames = min(total_frames, int(fps * max_duration))
    
    ascii_frames = []
    count = 0
    
    print(f"Converting video to ASCII frames... (Target: {max_frames} frames)")
    print(f"ASCII dimensions: {ascii_width}x{ascii_height}")
    
    while cap.isOpened() and len(ascii_frames) < max_frames:
        ret, frame = cap.read()
        
        if not ret:
            break
        
        if count % interval == 0:
            ascii_frame = frame_to_ascii(frame, ascii_width, ascii_height)
            ascii_frames.append(ascii_frame)
            
            # Show progress
            if len(ascii_frames) % 10 == 0:
                progress = len(ascii_frames) / max_frames * 100
                print(f"Progress: {progress:.1f}% ({len(ascii_frames)}/{max_frames} frames)")
        
        count += 1
        
    cap.release()
    
    if not ascii_frames:
        print("No frames were processed. Please check your video file.")
        return
    
    print(f"Conversion complete! Generated {len(ascii_frames)} ASCII frames.")
    print("Starting playback in 3 seconds... (Press Ctrl+C to exit)")
    time.sleep(3)
    
    # Clear screen before starting
    os.system('cls' if os.name == 'nt' else 'clear')
    delay = 1 / fps
    
    try:
        frame_count = 0
        while True:
            for i, ascii_frame in enumerate(ascii_frames):
                # Clear the screen and print the new frame
                sys.stdout.write("\033[H\033[2J")  # More reliable screen clearing
                sys.stdout.write(f"Frame: {i+1}/{len(ascii_frames)} | FPS: {fps} | Press Ctrl+C to exit\n")
                sys.stdout.write(ascii_frame)
                sys.stdout.flush()
                time.sleep(delay)
                frame_count += 1
    except KeyboardInterrupt:
        # Catch Ctrl+C to exit gracefully
        print("\n\033[1;32m[Exiting ASCII video player]\033[0m")
        print(f"Played {frame_count} frames total.")

if __name__ == "__main__":
    VIDEO_PATH = "/Users/macaz/Downloads/Videos/video-1660799578.mp4"  # Change this path to your video
    
    # You can customize these parameters:
    # main(VIDEO_PATH, max_duration=10, fps=15)  # Play only first 10 seconds at 15 FPS
    main(VIDEO_PATH)  # Play entire video at default 25 FPS