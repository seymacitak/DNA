islem = ""
output = ""

print("DNA programina hos geldiniz")
dizi = input("Elinizdeki diziyi giriniz\nDizi : ")

while islem != "q":
	print("Islemler: ")
	print("1. Tamamlayici dize olusturmak\n2. Toplam baz sayisi\n3. Toplam Timin sayisi\n4. Toplam Adenin sayisi\n5. Toplam Sitozi sayisi\n6. Toplam Guanin sayisi\n7. Dizedeki kodonlari listelemek\n8. Tekrarlı dizi sayisi ")
	islem = input("Yapmak istediginiz islemin numarasini giriniz ")
	
	if islem == "1":
		print(" ")

		while True:
			for harf in dizi:

				if harf == 'A':			
					output += 'T'    

				elif harf =='T':
					output += 'A'
  
				elif harf == 'G':
					output += 'C'
    		
				elif harf == 'C':
					output += 'G'

				else:
					output = 'Hatalı baz girisi '

			print(output)	
			break	
	
	elif islem == "2": 				
		print(len(dizi)) 

	elif islem == "3":
		print(dizi.count("T"))

	elif islem == "4":
		print(dizi.count("A"))

	elif islem == "5":
		print(dizi.count("C"))

	elif islem == "6":
		print(dizi.count("G"))

	elif islem == "7":
		
		for i in range(0, len(dizi), 3) :
			print(dizi[i] + dizi[i+1] + dizi[i+2],  end=" , " )
