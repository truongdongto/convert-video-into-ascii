# ASCII Video Player

Convert and play video files as ASCII art in your terminal.

## Features

- Converts video frames to ASCII art using grayscale mapping
- Adaptive terminal sizing for optimal display
- Customizable playback speed (FPS)
- Duration limiting for testing
- Real-time progress tracking during conversion
- Smooth terminal playback with frame counter

## Requirements

```bash
pip install opencv-python numpy
```

## Usage

### Basic Usage

```python
from ascii_video import main

# Play entire video at default 25 FPS
main("/path/to/your/video.mp4")
```

### Advanced Usage

```python
# Play only first 10 seconds at 15 FPS
main("/path/to/your/video.mp4", max_duration=10, fps=15)

# Custom parameters
main(
    video_path="/path/to/video.mp4",
    max_duration=30,  # Limit to 30 seconds
    fps=20           # 20 frames per second
)
```

### Command Line

Update the `VIDEO_PATH` variable in the script and run:

```bash
python ascii_video.py
```

## Parameters

- `video_path`: Path to the video file
- `max_duration`: Optional duration limit in seconds
- `fps`: Playback frames per second (default: 25)

## How It Works

1. **Frame Extraction**: Uses OpenCV to read video frames
2. **Grayscale Conversion**: Converts BGR frames to grayscale
3. **Resizing**: Adapts frames to terminal dimensions
4. **ASCII Mapping**: Maps pixel intensities to ASCII characters (`@%#*+=-:. `)
5. **Terminal Playback**: Displays frames sequentially with timing control

## Controls

- **Ctrl+C**: Exit the player gracefully
- The video loops automatically after completion

## Terminal Compatibility

- Works on Unix/Linux/macOS terminals
- Windows Command Prompt/PowerShell support
- Automatically detects terminal size for optimal display

## Example Output

```
Converting video to ASCII frames... (Target: 250 frames)
ASCII dimensions: 120x40
Progress: 40.0% (100/250 frames)
Progress: 80.0% (200/250 frames)
Conversion complete! Generated 250 ASCII frames.
Starting playback in 3 seconds... (Press Ctrl+C to exit)

Frame: 125/250 | FPS: 25 | Press Ctrl+C to exit
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@#######*****++++=======-----::::....   
###***+++===---:::...                         
...
```

## Notes

- Larger videos take longer to convert
- Terminal size affects ASCII quality
- Higher FPS values create smoother playback but use more CPU
- Works best with videos that have good contrast
