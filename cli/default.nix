{ lib, python3Packages }:
with python3Packages;
buildPythonApplication {
  pname = "fortnox_cli";
  version = "1.0";

  propagatedBuildInputs = [ ];

  src = ./.;
}
