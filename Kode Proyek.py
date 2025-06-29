import csv

class TreeNode:
    def __init__(self, atribut=None, is_leaf=False, rekomendasi=None):
        self.atribut = atribut
        self.branches = {}
        self.is_leaf = is_leaf
        self.rekomendasi = rekomendasi

    def add_branch(self, atribut_value, node):
        self.branches[atribut_value] = node

class DecisionTree:
    def __init__(self):
        self.root = None

    def buat_tree(self, data):
        self.root = self._buat_custom_tree(data)

    def _buat_custom_tree(self, data):
        root = TreeNode(atribut="Usia")
        usia_groups = {}

        for item in data:
            usia = item["Usia"]
            if usia not in usia_groups:
                usia_groups[usia] = []
            usia_groups[usia].append(item)

        for usia, usia_data in usia_groups.items():
            kategori_node = TreeNode(atribut="Kategori")
            kategori_groups = {}
            for item in usia_data:
                kategori = item["Kategori"]
                if kategori not in kategori_groups:
                    kategori_groups[kategori] = []
                kategori_groups[kategori].append(item)

            for kategori, kategori_data in kategori_groups.items():
                if kategori == "Fiksi":
                    genre_node = TreeNode(atribut="Genre")
                    genre_groups = {}
                    for item in kategori_data:
                        genre = item["Genre"]
                        if genre not in genre_groups:
                            genre_groups[genre] = []
                        genre_groups[genre].append(item)

                    for genre, genre_data in genre_groups.items():
                        halaman_node = TreeNode(atribut="Banyak halaman")
                        halaman_groups = {}
                        for item in genre_data:
                            halaman = item["Banyak halaman"]
                            if halaman not in halaman_groups:
                                halaman_groups[halaman] = []
                            halaman_groups[halaman].append(item)

                        for halaman, halaman_data in halaman_groups.items():
                            bahasa_node = TreeNode(atribut="Bahasa")
                            bahasa_groups = {}
                            for item in halaman_data:
                                bahasa = item["Bahasa"]
                                if bahasa not in bahasa_groups:
                                    bahasa_groups[bahasa] = []
                                bahasa_groups[bahasa].append(item)

                            for bahasa, bahasa_data in bahasa_groups.items():
                                leaf_node = TreeNode(is_leaf=True, rekomendasi=bahasa_data[0]["Rekomendasi Buku"])
                                bahasa_node.add_branch(bahasa, leaf_node)

                            halaman_node.add_branch(halaman, bahasa_node)

                        genre_node.add_branch(genre, halaman_node)

                    kategori_node.add_branch(kategori, genre_node)

                elif kategori == "Nonfiksi":
                    genre_node = TreeNode(atribut="Genre")
                    genre_groups = {}
                    for item in kategori_data:
                        genre = item["Genre"]
                        if genre not in genre_groups:
                            genre_groups[genre] = []
                        genre_groups[genre].append(item)

                    for genre, genre_data in genre_groups.items():
                        halaman_node = TreeNode(atribut="Banyak halaman")
                        halaman_groups = {}
                        for item in genre_data:
                            halaman = item["Banyak halaman"]
                            if halaman not in halaman_groups:
                                halaman_groups[halaman] = []
                            halaman_groups[halaman].append(item)

                        for halaman, halaman_data in halaman_groups.items():
                            bahasa_node = TreeNode(atribut="Bahasa")
                            bahasa_groups = {}
                            for item in halaman_data:
                                bahasa = item["Bahasa"]
                                if bahasa not in bahasa_groups:
                                    bahasa_groups[bahasa] = []
                                bahasa_groups[bahasa].append(item)

                            for bahasa, bahasa_data in bahasa_groups.items():
                                leaf_node = TreeNode(is_leaf=True, rekomendasi=bahasa_data[0]["Rekomendasi Buku"])
                                bahasa_node.add_branch(bahasa, leaf_node)

                            halaman_node.add_branch(halaman, bahasa_node)

                        genre_node.add_branch(genre, halaman_node)

                    kategori_node.add_branch(kategori, genre_node)

            root.add_branch(usia, kategori_node)

        return root

    def get_rekomendasi(self, user_preferences):
        current_node = self.root

        while not current_node.is_leaf:
            atribut = current_node.atribut
            value = user_preferences.get(atribut)

            if value not in current_node.branches:
                return "Buku tidak ditemukan"

            current_node = current_node.branches[value]

        return current_node.rekomendasi

def load_data_from_csv(file_path):
    data = []
    with open("DUMMY.csv", 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            data.append(row)
    return data

def main():
    file_path = "DUMMY.csv"
    data = load_data_from_csv(file_path)
    tree = DecisionTree()
    tree.buat_tree(data)

    print("Masukkan preferensi Anda untuk mendapatkan rekomendasi buku:")

    pilihan_usia = ["<7 ", "7 - 12", "13 - 16", "17 - 20", "21+"]
    pilihan_kategori = ["Fiksi", "Nonfiksi"]

    pilihan_genre_fiksi = ["Fantasi", "Aksi", "Misteri", "Horror", "Romantis", "Komedi"]
    pilihan_genre_nonfiksi = ["Sejarah", "Sains", "Biografi", "Inspiratif", "Ekonomi", "Kesehatan"]

    pilihan_halaman = ["<100", "100-300", "300+"]
    pilihan_bahasa = ["IND", "ENG"]

    while True:
        print("\nPilihan Usia:")
        for i, option in enumerate(pilihan_usia):
            print(f"  {i+1}. {option}")
        try:
            usia_idx = int(input("Pilih nomor usia (1-5): ")) - 1
            if 0 <= usia_idx < len(pilihan_usia):
                usia = pilihan_usia[usia_idx]
                break
            else:
                print("\033[91mInput tidak valid. Silakan masukkan angka antara 1 dan 5.\033[0m")
        except ValueError:
            print("\033[91mInput tidak valid. Silakan masukkan angka.\033[0m")

    while True:
        print("\nPilihan Kategori:")
        for i, option in enumerate(pilihan_kategori):
            print(f"  {i+1}. {option}")
        try:
            kategori_idx = int(input("Pilih nomor kategori (1-2): ")) - 1
            if 0 <= kategori_idx < len(pilihan_kategori):
                kategori = pilihan_kategori[kategori_idx]
                break
            else:
                print("\033[91mInput tidak valid. Silakan masukkan angka antara 1 dan 2.\033[0m")
        except ValueError:
            print("\033[91mInput tidak valid. Silakan masukkan angka.\033[0m")

    if kategori == "Fiksi":
        while True:
            print("\nPilihan Genre Fiksi:")
            for i, option in enumerate(pilihan_genre_fiksi):
                print(f"  {i+1}. {option}")
            try:
                genre_idx = int(input("Pilih nomor genre (1-6): ")) - 1
                if 0 <= genre_idx < len(pilihan_genre_fiksi):
                    genre = pilihan_genre_fiksi[genre_idx]
                    break
                else:
                    print("\033[91mInput tidak valid. Silakan masukkan angka antara 1 dan 6.\033[0m")
            except ValueError:
                print("\033[91mInput tidak valid. Silakan masukkan angka.\033[0m")
    else:
        while True:
            print("\nPilihan Kategori Nonfiksi:")
            for i, option in enumerate(pilihan_genre_nonfiksi):
                print(f"  {i+1}. {option}")
            try:
                genre_idx = int(input("Pilih nomor kategori (1-6): ")) - 1
                if 0 <= genre_idx < len(pilihan_genre_nonfiksi):
                    genre = pilihan_genre_nonfiksi[genre_idx]
                    break
                else:
                    print("\033[91mInput tidak valid. Silakan masukkan angka antara 1 dan 6.\033[0m")
            except ValueError:
                print("\033[91mInput tidak valid. Silakan masukkan angka.\033[0m")

    while True:
        print("\nPilihan Banyak Halaman:")
        for i, option in enumerate(pilihan_halaman):
            print(f"  {i+1}. {option}")
        try:
            halaman_idx = int(input("Pilih nomor banyak halaman (1-3): ")) - 1
            if 0 <= halaman_idx < len(pilihan_halaman):
                halaman = pilihan_halaman[halaman_idx]
                break
            else:
                print("\033[91mInput tidak valid. Silakan masukkan angka antara 1 dan 3.\033[0m")
        except ValueError:
            print("Input tidak valid. Silakan masukkan angka.")

    while True:
        print("\nPilihan Bahasa:")
        for i, option in enumerate(pilihan_bahasa):
            print(f"  {i+1}. {option}")
        try:
            bahasa_idx = int(input("Pilih nomor bahasa (1-2): ")) - 1
            if 0 <= bahasa_idx < len(pilihan_bahasa):
                bahasa = pilihan_bahasa[bahasa_idx]
                break
            else:
                print("\033[91mInput tidak valid. Silakan masukkan angka antara 1 dan 2.\033[0m")
        except ValueError:
            print("\033[91mInput tidak valid. Silakan masukkan angka.\033[0m")

    user_preferences = {
        "Usia": usia,
        "Kategori": kategori,
        "Genre": genre,
        "Banyak halaman": halaman,
        "Bahasa": bahasa
    }

    rekomendasi = tree.get_rekomendasi(user_preferences)

    print("\nBerdasarkan preferensi Anda:")
    for key, value in user_preferences.items():
        print(f"  {key}: {value}")
    print(f"\n\033[1mRekomendasi Buku: {rekomendasi}\033[0m")

if __name__ == "__main__":
    main()