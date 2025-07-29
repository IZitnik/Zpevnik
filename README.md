# Zpevnik - Personal Songbook Generator

This project builds my personal songbook in PDF format using [ChordPro](https://www.chordpro.org/) and [Ninja](https://ninja-build.org/) as the build system.

## Usage

### 1. Prerequisites

- Python 3
- [ChordPro](https://www.chordpro.org/)
- [Ninja](https://ninja-build.org/)

Install ChordPro if not already installed 
according to chordpro's [installation guidelines](https://www.chordpro.org/chordpro/chordpro-installation/).

Install Ninja using your system's package manager 
or from [here](https://ninja-build.org/).

### 2. Configure the build

Change variables at the start of the 
*configure.py* file as you see fit.

When satisfied, run the configuration script
to generate the `build.ninja` file:
```bash
python configure.py
```

#### This will:

- **Generate songbook source file** if it doesn't exist with all songs in `songs/` and with specified cover
- scan the `songs/` folder and create **target for each individual song**.
- adds **target for specified songbook**.

### 3. Build the Songbook

To build the full songbook:
```bash
ninja
```

To build an individual song:
```bash
ninja <songname>.pdf
```

All output PDFs will appear in the `result/` directory 
or directory specified in `configure.py`.

## Customization

- **Change Song Order**: Edit `songbook.txt` to rearrange songs.
- **Update Cover**: Replace `cover.pdf` with your preferred front page.
- **ChordPro Config**: Customize chordpro by editing `config.json`.
- **Build config**: Edit the `configure.py` file.
