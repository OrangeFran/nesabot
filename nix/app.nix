{ pkgs ? import <nixpkgs> {}, ... }:

let
  # The packages from the stable channel work
  pkgs-stable = import (
    fetchTarball "https://nixos.org/channels/nixpkgs-20.09-darwin/nixexprs.tar.xz"
  ) {};
in

pkgs.python3.pkgs.buildPythonApplication {
  pname = "nesabot";
  version = "0.1";
  src = ../.;
  # Use the python packages from the stable channel
  propagatedBuildInputs = with pkgs-stable.python3.pkgs; [
    beautifulsoup4
    requests
    python-telegram-bot
  ];
  # Disable tests
  doCheck = false;
}
