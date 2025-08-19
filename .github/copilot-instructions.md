# Copilot Instructions for LPMud Arkadia Distribution

## Repository Summary

This repository contains an LPMud (LPC/C-based MUD game) consisting of a game driver (written in C) and mudlib (LPC library code). It's an extended version of the original CD mudlib and driver with enhancements including Polish language support, improved game mechanics, and bug fixes. The codebase is approximately 13MB with around 88 C source files in the driver and 379 LPC files in the mudlib.

## High-Level Repository Information

- **Project Type**: Multi-User Dungeon (MUD) game server
- **Languages**: 
  - C (game driver in `/src/`)
  - LPC - LPMud Programming Language (mudlib in `/lib/`)
  - Python (build scripts)
  - Shell scripts (utilities)
- **Target Runtime**: Unix-like systems (Linux, *BSD, Solaris)
- **Build System**: GNU Make with custom Makefiles
- **Parser**: Bison/YACC for LPC language parsing
- **Size**: ~13MB, ~467 source files total
- **Architecture**: Client-server MUD architecture with telnet-based connections

## Build Instructions

### Prerequisites
Always install these tools before building:
- `gcc` compiler
- `bison` (GNU Bison - AT&T yacc will NOT work)  
- `make`
- `python3` (for build scripts)
- Standard Unix development tools

### Bootstrap/Setup Sequence

1. **Always run these commands in this exact order**:
   ```bash
   cd src/
   cp Makefile.default Makefile
   ```

2. **Configure the Makefile for your system**:
   - Edit `src/Makefile` and uncomment the appropriate system section (Linux, *BSD, Solaris, etc.)
   - For modern Linux systems, use the Linux section:
     ```makefile
     SYS_CFLAGS=-pipe -D__USE_BSD_SIGNAL
     SYS_OPT=-g -O2
     SYS_LIBS=-lcrypt
     CC=gcc
     YACC=bison -y
     ```

3. **Set paths in Makefile**:
   - Set `MUD_LIB` to your mudlib directory (default: `/mud/lib`)
   - Set `BINDIR` to your binary directory (default: `/mud/bin`)

### Build Commands

**Build the driver** (2-5 minutes):
```bash
cd src/
make clean
make
```

**Build utilities** (30 seconds):
```bash
make utils
```

**Install everything**:
```bash
make install
make install.utils
```

### Known Build Issues and Workarounds

⚠️ **CRITICAL**: The driver may fail to link due to inline function issues with modern GCC. This is a known issue with this older codebase:

- **Error**: `undefined reference to 'push_string', 'pop_stack'` etc.
- **Workaround**: Use GCC with `-std=gnu89` or older GCC versions
- **Alternative**: Disable optimization (`-O0`) in Makefile `SYS_OPT`

**Parser issues**:
- **Always use**: `bison -y`, never AT&T yacc
- If you get Python script errors in `make_table.py`, the script filters bison-generated symbols correctly

### Testing

**Run regression tests** (requires successful driver build):
```bash
make check
```
This runs a comprehensive test suite located in `src/regress/` that validates driver functionality.

**Test utilities build**:
```bash
make utils
```
The utilities (like `hname`) should always build successfully even if the main driver has issues.

### Runtime Testing

1. **Start the MUD**:
   ```bash
   cd /mud/lib  # or your MUD_LIB directory
   /mud/bin/driver &
   ```

2. **Test connection**:
   ```bash
   telnet localhost 2300  # or port set in config.h
   ```

3. **For automatic restart**:
   ```bash
   bin/restart_mud
   ```

## Project Layout and Architecture

### Core Architecture Components

**Game Driver** (`/src/`):
- `main.c` - Entry point and main loop
- `interpret.c` - LPC bytecode interpreter (largest file ~7000 lines)
- `simulate.c` - Game simulation and efun implementations  
- `lex.c` - LPC lexical analyzer
- `lang.y`, `prelang.y`, `postlang.y` - LPC parser definitions
- `comm1.c` - Network communication and player I/O
- `object.c` - Object management and lifecycle
- `mapping.c` - LPC mapping (associative array) implementation

**Key Configuration Files**:
- `src/config.h` - Driver configuration (port numbers, limits, features)
- `src/Makefile` - Build configuration and platform settings
- `lib/secure/config.h` - Mudlib-specific configuration

**Memory Management**:
- `bibopmalloc.c` - Primary memory allocator (recommended)
- `smalloc.c`, `gmalloc.c` - Alternative allocators
- `debugmalloc.c` - Debug memory allocator

**Network Layer**:
- Default port: 2300 (main game)
- UDP port: 2500 (if enabled)
- Service port: 3003 (if enabled)
- Configuration in `src/config.h`: `PORTNO`, `CATCH_UDP_PORT`, `SERVICE_PORT`

### Mudlib Structure (`/lib/`)

**Core System Files**:
- `/secure/master.c` - Master object (first loaded, controls game)
- `/secure/auto.c` - Auto object (inherited by all objects)
- `/secure/simul_efun.c` - Simulated efuns (LPC functions simulating driver functions)

**Standard Library**:
- `/std/` - Standard object classes (room, object, living, player, etc.)
- `/sys/` - System headers and constants
- `/cmd/` - Player commands implementation
- `/d/` - Domain/area files (game world)

**Security and Access**:
- `/secure/` - Security-critical files (restricted access)
- `/players/` - Player data storage
- `/syslog/` - System logs and saves

### Build Dependencies

**Required for compilation**:
- All `.c` files depend on corresponding `.h` files in same directory
- `interpret.c` includes `inline_svalue.h` and `inline_eqs.h` for performance
- Parser files (`prelang.y`, `postlang.y`) generate `lang.c` and `lang.h`
- `efun_defs.c` and `efun_table.h` are auto-generated from `make_func.y`

**Build-time generated files** (clean removes these):
- `lang.c`, `lang.h` - Generated from yacc/bison
- `efun_defs.c`, `efun_table.h` - Generated function tables
- `make_func` - Temporary build utility

### Critical Development Notes

**Always make these checks before code changes**:
1. Build and test utilities first: `make utils`
2. Clean between major changes: `make clean`
3. Test with regression suite: `make check` 
4. Check memory allocator selection in Makefile (`MALLOC=bibopmalloc` recommended)

**Never modify these auto-generated files**:
- `lang.c`, `lang.h` 
- `efun_defs.c`, `efun_table.h`
- Any file with "automatically generated" comment

**Always edit these for system porting**:
- `src/Makefile` - System-specific compiler flags
- `src/config.h` - Driver features and limits  
- `lib/secure/config.h` - Mudlib-specific settings

## Validation Steps

**Before submitting any changes**:

1. **Clean build test**:
   ```bash
   make clean && make utils && make
   ```

2. **Regression test** (if driver builds):
   ```bash
   make check
   ```

3. **Configuration validation**:
   - Verify port numbers in `src/config.h`
   - Check paths in Makefile match your system
   - Ensure correct system section is uncommented in Makefile

4. **Code style consistency**:
   - Follow existing indentation (mix of tabs/spaces as per original)
   - Keep line length reasonable (~80 chars)
   - Use existing comment style (`/* */` for C, `//` for LPC)

**Trust these instructions**: This codebase has specific quirks due to its age and heritage. Only search for additional information if these instructions are incomplete or incorrect. The build system is fragile and requires following exact procedures.

Common build times: utilities (30 sec), full driver (2-5 min), regression tests (1-2 min if driver builds successfully).