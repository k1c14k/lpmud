# Installation Guide

This is a brief description of how to install the CD driver:

1. **Create Directories**
   - Make a directory `mud`, which contains directories named `src`, `bin`, and `lib`.
   - Move the game driver source (this code) to the `src` directory.

2. **Prepare Makefile**
   - Copy `Makefile.default` to `Makefile` and uncomment the proper definitions for compiling on your system.
   - If your system is not one of those listed, you will have to create a section for it.
   - Try compiling the driver with empty `MISSING_OBJ` and `MISSING_SRC` variables; add only objects required to successfully compile the driver.
   - Pay special attention to the version of yacc being used. **AT&T yacc will NOT work.** `byacc` (standard on some systems) is the preferred yacc to use, `GNU bison` will also work.

3. **Set Paths**
   - Make sure the `MUD_LIB` and `BINDIR` variables in your Makefile reflect where the mud's binaries and mudlib will be placed.

4. **Allocator Options**
   - There are several allocators supported by the driver. The preferred one is `bibop`, and is also the default.

5. **Development Options**
   - If you are going to do driver development, it is recommended that you enable the `DEBUG` option in your Makefile as well.
   - You may want to look over the options in `config.h` and tailor those for your system.

6. **Build the Driver**
   - To actually build the driver, run:
     ```sh
     make
     make utils
     ```
   - To run a regression test of the driver before installing, run:
     ```sh
     make check
     ```

7. **Install the Driver**
   - To install the driver, run:
     ```sh
     make install
     make install.utils
     ```

8. **Install Mudlib**
   - Get a mudlib and install it in the `lib` directory. The most current version of the CDLIB mudlib is available from `ftp.cd.chalmers.se` in the directory `pub/cdlib`.

9. **Test the Game**
   - Test the game with:
     ```sh
     driver &
     ```
   - If you see the message `Setting up ipc`, then you are up and running.
   - Test with:
     ```sh
     telnet localhost 3011
     ```
     (or the port number you specified in the `config.h` file, if you changed it)

10. **Automatic Restart**
    - If you want the game to restart automatically, use:
      ```sh
      bin/restart_mud
      ```

