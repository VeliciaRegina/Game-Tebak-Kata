def clear_screen():
    """Bersihkan layar dengan mencetak banyak baris kosong."""
    print("\n" * 40)

def tekan_enter():
    """Tunggu user menekan Enter."""
    input("\nTekan Enter untuk melanjutkan...")

def enter_and_clear():
    """Tunggu user menekan Enter dan membersihkan layar."""
    tekan_enter()
    clear_screen()
