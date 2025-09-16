from moviepy.editor import VideoFileClip, concatenate_videoclips

# Load your scene videos
intro = VideoFileClip("media/videos/rcr/480p15/RCRIntro.mp4")
intro1 = VideoFileClip("media/videos/rcr/480p15/MicroProgramIntro.mp4")
arch = VideoFileClip("media/videos/rcr/480p15/ArchitectureDiagram.mp4")
vis = VideoFileClip("media/videos/rcr/480p15/RCRVisualization.mp4")
outro = VideoFileClip("media/videos/rcr/480p15/RCROutro.mp4")

# Concatenate them in order
final = concatenate_videoclips([intro,intro1, arch, vis, outro])

# Export as one mp4 with progress bar visible
final.write_videofile(
    "RCR.mp4",
    codec="libx264",   # widely supported codec
    fps=30,            # frame rate
    threads=4,         # speeds up rendering on multicore CPU
    preset="ultrafast" # faster export (bigger file size, but fine for testing)
)
