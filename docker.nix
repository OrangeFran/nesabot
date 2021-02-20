{ pkgs ? import <nixpkgs> {}, ... }:

let
  nesabot-app = import ./app.nix { inherit pkgs; };
in

pkgs.dockerTools.buildImage {
  name = "nesabot";
  created = "now";
  contents = [ nesabot-app ];
  config.Cmd = [ "nesabot" ];
}
