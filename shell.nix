{ pkgs ? import <nixpkgs> {}, ... }:

# TODO: Drop "mach-nix" and create this
#       in bare nix without any external tools

let
  # "mach-nix" makes this a lot easier
  mach-nix = import (
    builtins.fetchTarball {
      url = "https://github.com/DavHau/mach-nix/tarball/3.1.1";
      sha256 = "06bxmz7x1fnjx2d0gb63fdm0jci2mcdnpa3isbhjr92z1l2a7hl1";
    }
  ) { inherit pkgs; };
in

# Easy
mach-nix.mkPythonShell {
  requirements = builtins.readFile ./requirements.txt;
}
