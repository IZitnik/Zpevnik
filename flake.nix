{
  description = "Zpevnik";

  inputs = {
    nixpkgs.url = "github:NixOS/nixpkgs/nixos-unstable";
    flake-parts.url = "github:hercules-ci/flake-parts";
  };

  outputs = inputs@{ flake-parts, ... }:
    let
      songs =
        map (builtins.replaceStrings [".chordpro"] [""]) (
          builtins.attrNames (builtins.readDir ./songs)
        );
    in 
    flake-parts.lib.mkFlake { inherit inputs; } {
      systems = [
        "x86_64-linux"
        "aarch64-linux"
        "x86_64-darwin"
        "aarch64-darwin"
      ];

      perSystem = { config, pkgs, system, ... }:
        let
          mkSong = file: {
            name = file;
            value = pkgs.callPackage ./package.nix {
              target = file;
            };
          };
          songPkgs = builtins.listToAttrs (map mkSong songs);
        in
        {
          packages = songPkgs // rec {
            Zpevnik = pkgs.callPackage ./package.nix {};
            default = Zpevnik;
          };

          devShells.default = pkgs.mkShell {
            nativeBuildInputs = [
              pkgs.perl5Packages.AppMusicChordPro
              pkgs.ninja
              pkgs.python313
            ];
          };
        };
    };
}
