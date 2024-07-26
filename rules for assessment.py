#"DOSEN MATKUL PBO PRODI TRK SV IPB telah membuat aturan penilaian:
#Bobot Kehadiran = 15%
#Bobot Tugas = 25%
#Bobot UTS = 30%
#Bobot UAS = 30%
#Nilai Akhir ditetapkan sebagai berikut:
#Grade A lebih besar atau sama dengan dari 85
#Grade B antara 70 s.d 85
#Grade C antara 50 s.d 70
#Grade D antara 40 s.d 50
#Kurang dari 40 Tidak Lulus
#Data yang dimiliki adalah:
#Mahasiswa 1 nilai berturut-turut 80,75,85,70 Tentukan Grade mahasiswa tersebut"
class Nilai:
	def __init__(self, nama, kehadiran, tugas, uts, uas):
		self.nama = nama
		self.kehadiran = kehadiran
		self.tugas = tugas
		self.uts = uts
		self.uas = uas
		print("Nama 				: {}".format(nama))
		print("Nilai Kehadiran			: {}".format(kehadiran))
		print("Nilai Tugas			: {}".format(tugas))
		print("Nilai UT			: {}".format(uts))
		print("Nilai US			: {}".format(uas))
		
	def Bobot(self):
		kehadiran = self.kehadiran 
		tugas = self.tugas
		uts = self.uts
		uas = self.uas
		nilaikehadiran = kehadiran/100*15
		nilaitugas = tugas/100*25
		nilaiuts = uts/100*30
		nilaiuas = uas/100*30
		print("Nilai Bobot Kehadiran Anda 	: {:.2f}".format(nilaikehadiran))
		print("Nilai Bobot Tugas Anda 		: {:.2f}".format(nilaitugas))
		print("Nilai Bobot UTS Anda 		: {:.2f}".format(nilaiuts))
		print("Nilai Bobot UAS Anda 		: {:.2f}".format(nilaiuas))
		hasilnilai = nilaikehadiran + nilaitugas + nilaiuts + nilaiuas
		self.hasilnilai = hasilnilai
		print("Total dari Bobot Nilai Anda	: {:.2f}".format(hasilnilai))
		print("----------------------------------------")
		
	def hurufmutu(self):
		hasilnilai = self.hasilnilai
		if hasilnilai >= 85:
			hurufmutu = "A" 
		elif hasilnilai >= 70:
			hurufmutu = "B" 
		elif hasilnilai >= 50:
			hurufmutu = "C"
		elif hasilnilai >= 40:
			hurufmutu = "D"
		elif hasilnilai < 40:
			hurufmutu = "E atau disebut sebagai Tidak Lulus"
		print("Total Nilai Bobot anda adalah {:.2f} dimana hasil akhir yang anda dapatkan adalah {} ".format(hasilnilai, hurufmutu),end="\n\n")
		print("\n")

print("Program Perhitungan hurufmutu berdasarkan Bobot Nilai.",end="\n\n")
		
MHS1 = Nilai("Muhammad Hafizh Maulidan",96,90,93,85)
MHS1.Bobot()
MHS1.hurufmutu()
MHS2 = Nilai("Andreas John Aries vito",80,75,85,70)
MHS2.Bobot()
MHS2.hurufmutu()
