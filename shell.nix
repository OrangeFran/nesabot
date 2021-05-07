{ 
  pkgs ? import (
    # The packages from the stable channel work
    fetchTarball "https://nixos.org/channels/nixpkgs-20.09-darwin/nixexprs.tar.xz"
  ) {}, ...
}:

pkgs.mkShell {
  buildInputs = with pkgs.python3.pkgs; [
    python-dotenv
    beautifulsoup4
    requests
  ];
}

