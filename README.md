# LPMud Arkadia Distribution

This distribution includes a mudlib and driver, both extended from the original CD mudlib and driver. The latest versions of the originals can be found at [Genesis MUD](http://genesis.cs.chalmers.se).

## Polish Language Support

Some modifications focus on supporting Polish grammar, mainly in the `parse.c` file of the driver. However, Polish support is only a small part of the overall changes. Enhancements have been made to improve game mechanics, functionality for developers, and to fix bugs from the original authors.

## Development and Sharing

The mudlib and driver have been developed on Arkadia. We share our work to accelerate the development of this codebase. We hope to be informed about interesting changes made to the driver or mudlib on other MUDs that benefit from our work.

The latest version of this distribution is available at:

`ftp://arkadia@ftp.arkadia.rpg.pl`

## Installation Instructions

Driver sources are located in the `src` subdirectory. To install the MUD:

1. Edit the following files:
   - `src/config.h` (mainly the port number)
   - `src/Makefile` (paths, system type, parser, compilation options)
2. Run the following commands in order:
   - `make`
   - `make install`
   - `make install_utils`
3. To start the MUD, run `bin/restart_mud` and connect via telnet to the port set in `config.h` (default: 2300).
4. Log in as the wizard character named `root` (no password required); this account has maximum privileges.

## Troubleshooting

If you encounter problems, please do not bother wizards from any MUD. Try to find a solution yourself. Creating a new MUD involves many more difficult stages; if you cannot overcome this one, it may not be worth engaging in such a large project.

If you are determined enough, we wish you the best of luck!

**Alvin@Arkadia**

