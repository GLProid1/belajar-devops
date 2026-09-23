"""Modul sederhana untuk demostrasi Pylint Quality Gate"""

def hitung_luas_persegi_panjang(panjang: int, lebar: int) -> int:
    """Fungsi untuk menghitung luas persegi panjang
  
    Args:
      panjang (int): Panjang sisi persegi panjang.
      lebar (int): Lebar sisi persegi panjang.
    
    Returns:
        int: Hasil perkalian panjang dan lebar
    """
    return panjang * lebar

def main():
    """Fungsi utama untuk menjalankan program"""
    hasil = hitung_luas_persegi_panjang(4, 10)
    print(f"Luas persegi panjang adalah: {hasil}")
  
if __name__ == "__main__":
    main()
  