import os

SONG_DIR = "songs"
RES_DIR = "result"
CONFIG = "config.json"
COVER = "cover.pdf"
SONGBOOK = "Zpevnik.pdf"

# Get all .chordpro files in the songs directory
songs = [os.path.join(SONG_DIR, f)
         for f in os.listdir(SONG_DIR) if f.endswith(".chordpro")]

with open("build.ninja", "w") as f:
    f.write(f"""# Auto-generated build.ninja
song_dir = {SONG_DIR}
res_dir = {RES_DIR}
config = {CONFIG}
cover = {COVER}
songbook = {SONGBOOK}

rule build_songbook
  command = chordpro --config=$config --cover=$cover $in -o $res_dir/$out
  description = Building songbook $out

rule build_song
  command = chordpro --config=$config $in -o $res_dir
  description = Building song $in

rule clean
  command = rm -rf $res_dir
  description = Cleaning build directory

""")

    # Songbook build using all songs
    song_inputs = " ".join(songs)
    f.write(f"build $songbook: build_songbook {song_inputs}\n\n")

    # Per-song builds
    for song in songs:
        f.write(f"build {os.path.basename(song)}.pdf: build_song {song}\n")

    f.write("\n")
    f.write("build clean: clean\n")
