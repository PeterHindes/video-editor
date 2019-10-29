import ffmpeg

in_file = ffmpeg.input('.\\Forest.mov')
overlay_file = ffmpeg.input('.\\vlc.png')
(
    ffmpeg
    .concat(
        in_file.trim(start_frame=0, end_frame=200),
        in_file.trim(start_frame=600, end_frame=800),
    )
    .overlay(overlay_file).scale(50,50)
    .drawbox(50, 50, 120, 120, color='red', thickness=5)
    .output('.\\out.mp4')
    .run()
)