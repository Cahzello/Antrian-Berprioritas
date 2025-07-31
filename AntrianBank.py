from gtts import gTTS
from playsound3 import playsound

class HeapPriorityQueue:
    def __init__(self):
        self.elements = []
        self.counter = 0  # urutan kedatangan

    def push(self, item, priority):
        self.elements.append((priority, self.counter, item))
        self.counter += 1
        self._bubble_up(len(self.elements) - 1)

    def pop(self):
        if not self.elements:
            raise IndexError("Tidak bisa pop dalam keadadan kosong!")
        top_item = self.elements[0]
        self.elements[0] = self.elements[-1]
        self.elements.pop()
        if self.elements:
            self._bubble_down(0)
        return top_item

    def peek(self):
        if not self.elements:
            raise IndexError("Tidak bisa peek dalam keadadan kosong!")
        return self.elements[0]

    def size(self):
        return len(self.elements)

    def _bubble_up(self, index):
        if index == 0:
            return
        parent_index = (index - 1) // 2
        if self.elements[index][:2] < self.elements[parent_index][:2]:
            self.elements[index], self.elements[parent_index] = self.elements[parent_index], self.elements[index]
            self._bubble_up(parent_index)

    def _bubble_down(self, index):
        left = 2 * index + 1
        right = 2 * index + 2
        smallest = index

        if left < len(self.elements) and self.elements[left][:2] < self.elements[smallest][:2]:
            smallest = left
        if right < len(self.elements) and self.elements[right][:2] < self.elements[smallest][:2]:
            smallest = right
        if smallest != index:
            self.elements[index], self.elements[smallest] = self.elements[smallest], self.elements[index]
            self._bubble_down(smallest)

# Fungsi tampil tabel
def tampilkan_tabel(meja1, meja2, selanjutnya):
    print("\n+----------+----------+-------------------+")
    print("| Meja 1   | Meja 2   | Nomor Selanjutnya |")
    print("+----------+----------+-------------------+")
    print(f"| {meja1:^8} | {meja2:^8} | {selanjutnya:^17} |")
    print("+----------+----------+-------------------+")

# ====== Program Utama ======
queue = HeapPriorityQueue()
status = True
bisnis_counter = 0
personal_counter = 0
nomorAntrianMeja1 = "Kosong"
nomorAntrianMeja2 = "Kosong"

while status:
    print("\nSelamat Datang di Bank")
    print("-" * 50)
    print("Ketik 0: Keluar")
    print("Ketik 1: Ambil antrian Tabungan Bisnis")
    print("Ketik 2: Ambil antrian Tabungan Personal")
    print("Ketik 3: Meja 1 panggil antrian")
    print("Ketik 4: Meja 2 panggil antrian")
    print("-" * 50)
    print(f"Total Antrian Saat Ini: {queue.size()}")
    print(f"Jumlah nomor Bisnis  : {bisnis_counter}")
    print(f"Jumlah nomor Personal: {personal_counter}")
    print("-" * 50)

    if queue.size() > 0:
        try:
            _, _, next_customer = queue.peek()
        except IndexError:
            next_customer = "Kosong"
    else:
        next_customer = "Kosong"

    tampilkan_tabel(nomorAntrianMeja1, nomorAntrianMeja2, next_customer)

    try:
        n = int(input("Pilihan nomor: "))
    except ValueError:
        print("Input tidak valid.")
        continue

    if n == 0:
        status = False
        print("Terima kasih telah menggunakan layanan.")
    elif n == 1:
        bisnis_counter += 1
        nomor = f"B{bisnis_counter:03d}"
        queue.push(nomor, 1)
        print(f"Nomor antrian Anda: {nomor}")
    elif n == 2:
        personal_counter += 1
        nomor = f"P{personal_counter:03d}"
        queue.push(nomor, 2)
        print(f"Nomor antrian Anda: {nomor}")
    elif n == 3:
        try:
            _, _, customer_id = queue.pop()
            nomorAntrianMeja1 = customer_id
            txt = f"Meja Kasir 1 memanggil nomor: {customer_id}"
            print(txt)
            tts = gTTS(txt, lang='id')
            tts.save("./tts.mp3")
            print("Sedang memutar suara..")
            playsound("./tts.mp3")
        except IndexError:
            nomorAntrianMeja1 = "Kosong"
            print("Tidak ada antrian untuk Meja Kasir 1.")
    elif n == 4:
        try:
            _, _, customer_id = queue.pop()
            nomorAntrianMeja2 = customer_id
            txt = f"Meja Kasir 2 memanggil nomor: {customer_id}"
            print(txt)
            tts = gTTS(txt, lang='id')
            tts.save("./tts.mp3")
            print("Sedang memutar suara..")
            playsound("./tts.mp3")
        except IndexError:
            nomorAntrianMeja2 = "Kosong"
            print("Tidak ada antrian untuk Meja Kasir 2.")
    else:
        print("Pilihan tidak valid, silahkan ulangi.")
