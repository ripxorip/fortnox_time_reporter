{ stdenv
, lib
, fetchurl
, pkg-config
, gi-docgen
, meson
, ninja
, gnome
, desktop-file-utils
, appstream-glib
, gettext
, itstool
, libxml2
, gtk4
, libadwaita
, glib
, atk
, gobject-introspection
, vala
, wrapGAppsHook4
}:

stdenv.mkDerivation rec {
  pname = "fortnox_time_reporter";
  version = "44.1";

  outputs = [ "out" "dev"];

  src = ./.;

  nativeBuildInputs = [
    desktop-file-utils
    gettext
    itstool
    meson
    ninja
    pkg-config
    gi-docgen
    gobject-introspection
    vala
    wrapGAppsHook4
  ];

  buildInputs = [
    gtk4
    libadwaita
    atk
    glib
  ];

  nativeCheckInputs = [
    appstream-glib
    desktop-file-utils
  ];

  mesonFlags = [
  ];

  postFixup = ''
  '';

  passthru = {
    updateScript = gnome.updateScript {
      packageName = "fortnox_time_reporter";
      attrPath = "gnome.${pname}";
    };
  };
}
