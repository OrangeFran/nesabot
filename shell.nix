{ pkgs ? import <nixpkgs> {}, ... }:

let
  # The packages from the stable channel work
  pkgs-stable = import (
    fetchTarball "https://nixos.org/channels/nixpkgs-20.09-darwin/nixexprs.tar.xz"
  ) {};
in

pkgs-stable.mkShell {
  buildInputs = with pkgs-stable.python3.pkgs; [
    beautifulsoup4
    requests
    python-telegram-bot
  ];
}

