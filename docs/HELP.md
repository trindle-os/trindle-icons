# Trindle Icons: help

Trindle Icons gives your desktop round, coloured app icons. There is one set, Trindle Circle. It has about 6,000 app icons drawn on round tiles. Any app we have not drawn uses a Papirus icon instead.

## Use the icons

1. Install the package `trindle-circle-icon-theme` (see the README for the steps).
2. Open Settings, then Appearance, then Icons.
3. Pick Trindle Circle.

## Ask for an icon or report a problem

You can report a problem or ask for an icon in one of two places. The choice is yours.

- Buildmorphic, at https://trindle.buildmorphic.com: the easy choice for most people. Reports sent automatically go here.
- GitHub issues, on the project page: for people who already use GitHub.

Say what you did, what you expected, and what happened instead. Include the icon set version and your desktop setup.

For security problems, use the private route in SECURITY.md, not a public issue.

## Change or add an icon

Code changes are not taken through this repository at the moment. You are free to fork the project under its licence (GPL-3.0-or-later). CONTRIBUTING.md has the details.

## Licences

- The coloured app icons and the code are GPL-3.0-or-later. See LICENSE.
- The one-colour icons in `symbolic/` are MIT. See symbolic/LICENSE.
- Papirus (GPL-3.0, by the Papirus Development Team) is used as the reference for icon names and as the fallback for icons we have not drawn.
- App names and logos belong to their owners. The icons identify each app and do not mean the app's owner endorses this set.

## What can go wrong

- An app shows a Papirus icon rather than a Trindle one. We have not drawn that app yet.
- The install fails if you leave out the `./` before the file name. Use `sudo apt install ./trindle-circle-icon-theme_<version>_all.deb` from the folder with the file.
- Building from source stops with a message if the Papirus folder is missing. Fetch Papirus or set `PAPIRUS_DIR`, as the README says.
