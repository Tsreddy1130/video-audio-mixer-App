# import os
# import re
# from moviepy import VideoFileClip, AudioFileClip

# input_folder = r"/Users/SESHIREDDY/Documents/DSA/Data Structure"
# output_folder = os.path.join(input_folder, "mix")
# os.makedirs(output_folder, exist_ok=True)

# files = os.listdir(input_folder)

# videos = [f for f in files if f.lower().endswith((".mp4", ".mkv"))]
# audios = [f for f in files if f.lower().endswith((".m4a", ".f140", ".f398", ".f609"))]

# # Extract number prefix like "01", "02", etc.
# def get_number_prefix(filename):
#     match = re.match(r"(\d+)", filename)
#     return match.group(1) if match else None

# video_dict = {get_number_prefix(v): v for v in videos}
# audio_dict = {get_number_prefix(a): a for a in audios}

# for num, video in video_dict.items():
#     if num in audio_dict:
#         audio = audio_dict[num]
#         print(f"🎬 Mixing [{num}]: {video} + {audio}")
#         video_clip = VideoFileClip(os.path.join(input_folder, video))
#         audio_clip = AudioFileClip(os.path.join(input_folder, audio))

#         final_clip = video_clip.with_audio(audio_clip)


#         output_path = os.path.join(output_folder, f"{num}_mixed.mp4")
#         final_clip.write_videofile(output_path, codec="libx264", audio_codec="aac")
#     else:
#         print(f"⚠️ No audio found for video [{num}]: {video}")

# print(f"\n✅ Done! Mixed files saved in: {output_folder}")
import tkinter as tk
from tkinter import filedialog, messagebox
from moviepy import VideoFileClip, AudioFileClip

def select_video():
    filepath = filedialog.askopenfilename(
        title="Select Video File",
        filetypes=[("Video Files", "*.mp4 *.mkv *.webm *.mov")]
    )
    if filepath:
        video_path.set(filepath)

def select_audio():
    filepath = filedialog.askopenfilename(
        title="Select Audio File",
        filetypes=[("Audio Files", "*.m4a *.mp3 *.aac *.f140 *.f398 *.f609")]
    )
    if filepath:
        audio_path.set(filepath)

def mix_and_save():
    vpath = video_path.get()
    apath = audio_path.get()

    if not vpath or not apath:
        messagebox.showerror("Error", "Please select both video and audio files.")
        return

    save_path = filedialog.asksaveasfilename(
        defaultextension=".mp4",
        filetypes=[("MP4 Video", "*.mp4")],
        title="Save Mixed Video As"
    )
    if not save_path:
        return

    try:
        status.set("Mixing...")
        root.update()

        video_clip = VideoFileClip(vpath)
        audio_clip = AudioFileClip(apath)
        final_clip = video_clip.with_audio(audio_clip)

        final_clip.write_videofile(save_path, codec="libx264", audio_codec="aac")

        messagebox.showinfo("Done", f"✅ Mixed video saved at:\n{save_path}")
        status.set("Ready")
    except Exception as e:
        messagebox.showerror("Error", str(e))
        status.set("Error")

# GUI
root = tk.Tk()
root.title("🎬 Audio-Video Mixer")

video_path = tk.StringVar()
audio_path = tk.StringVar()
status = tk.StringVar(value="Ready")

tk.Label(root, text="Video File:").grid(row=0, column=0, padx=5, pady=5, sticky="e")
tk.Entry(root, textvariable=video_path, width=50).grid(row=0, column=1, padx=5)
tk.Button(root, text="Browse", command=select_video).grid(row=0, column=2, padx=5)

tk.Label(root, text="Audio File:").grid(row=1, column=0, padx=5, pady=5, sticky="e")
tk.Entry(root, textvariable=audio_path, width=50).grid(row=1, column=1, padx=5)
tk.Button(root, text="Browse", command=select_audio).grid(row=1, column=2, padx=5)

tk.Button(root, text="🎯 Mix & Save", command=mix_and_save, bg="green", fg="white").grid(
    row=2, column=0, columnspan=3, pady=10
)

tk.Label(root, textvariable=status).grid(row=3, column=0, columnspan=3, pady=5)

root.mainloop()
