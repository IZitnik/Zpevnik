import os

SONG_DIR = "songs"
RES_DIR = "result"
CONFIG = "config.json"
COVER = "cover.pdf"
SONGBOOK = "Zpevnik.pdf"
SONGBOOK_SRC = "songbook.txt"

# initialize RES_DIR & SONG_DIR
if not os.path.exists(SONG_DIR):
    os.makedirs(SONG_DIR)
if not os.path.exists(RES_DIR):
    os.makedirs(RES_DIR)

# Get all .chordpro files in the songs directory
songs = [os.path.join(SONG_DIR, f)
         for f in os.listdir(SONG_DIR) if f.endswith(".chordpro")]

# Generate songbook.txt if it doesn't exist
if not os.path.exists(SONGBOOK_SRC):
    with open(SONGBOOK_SRC, "w") as f:
        f.write(COVER + "\n")
        for song in songs:
            f.write(song + "\n")

with open("build.ninja", "w") as f:
    f.write(f"""# Auto-generated build.ninja
song_dir = {SONG_DIR}
res_dir = {RES_DIR}
config = {CONFIG}
cover = {COVER}
songbook = {SONGBOOK}

rule build_songbook
  command = chordpro --config=$config \
                     --file=$in \
                     -o $res_dir/$out
  description = Building songbook $out according to $in

rule build_song
  command = chordpro --config=$config $in -o $res_dir/$out
  description = Building song $out

rule clean
  command = rm -rf $res_dir/*
  description = Cleaning build directory

""")

    # Songbook build using all songs
    song_inputs = " ".join(songs)
    f.write(f"build $songbook: build_songbook {SONGBOOK_SRC}\n\n")
    # Per-song builds
    for song in songs:
        f.write(f"build {os.path.basename(song)[
                :-9]}.pdf: build_song {song}\n")
    f.write("\n")
    f.write("build clean: clean\n")
    f.write("\n")
    f.write(f"default {SONGBOOK}\n")
