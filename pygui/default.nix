{ lib
, python3Packages
, gtk4
, libadwaita
, wrapGAppsHook4
, gobject-introspection
}:
with python3Packages;
buildPythonApplication {
  pname = "Fortnox Time Reporter pyGUI";
  version = "1.0";

  nativeBuildInputs = [ gobject-introspection wrapGAppsHook4 libadwaita gtk4 ];

  propagatedBuildInputs = [ pygobject3 pyserial libadwaita gtk4 ];

  src = ./.;
}

