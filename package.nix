{
  stdenv,
  perl5Packages,
  ninja,
  python313,
  target ? "Zpevnik"
}:

stdenv.mkDerivation {
  name = target;
  src = ./.;

  buildInputs = [ ];
  nativeBuildInputs  = [  
    perl5Packages.AppMusicChordPro
    ninja
    python313
  ];

  buildPhase = ''
    mkdir -p "$TMPDIR/home"
    export HOME="$TMPDIR/home"

    python configure.py
    ninja ${target}.pdf
  '';

  installPhase = ''
    mkdir -p $out
    cp _build/${target}.pdf $out/
  '';
}

