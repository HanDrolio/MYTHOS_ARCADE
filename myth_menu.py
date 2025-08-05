import os
import subprocess

GBA_CORE = "/usr/lib/x86_64-linux-gnu/libretro/mgba_libretro.so"
GBA_ROM_DIR = os.path.expanduser("~/MYTHOS_ARCADE/roms/gba")

def list_roms():
    return [f for f in os.listdir(GBA_ROM_DIR) if f.endswith(".gba")]

def launch_rom(rom_name):
    rom_path = os.path.join(GBA_ROM_DIR, rom_name)
    subprocess.Popen([
        "retroarch", "-L", GBA_CORE, rom_path
    ])

def main():
    roms = list_roms()
    if not roms:
        print("No GBA ROMs found.")
        return

    print("🎮 Myth.OS Arcade — GBA ROMs:\n")
    for i, rom in enumerate(roms):
        print(f"{i + 1}. {rom}")

    choice = input("\nSelect a game (number): ")
    try:
        index = int(choice) - 1
        if 0 <= index < len(roms):
            print(f"\n🕹️ Launching {roms[index]}...\n")
            launch_rom(roms[index])
        else:
            print("Invalid selection.")
    except ValueError:
        print("Please enter a number.")

if __name__ == "__main__":
    main()
