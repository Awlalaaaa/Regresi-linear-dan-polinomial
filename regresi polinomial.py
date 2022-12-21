Python 3.11.0 (v3.11.0:deaf509e8f, Oct 24 2022, 14:43:23) [Clang 13.0.0 (clang-1300.0.29.30)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
>>> import numpy as np # modul numpy untuk memudahkan pengolahan data
... from sklearn.linear_model import LinearRegression # modul untuk memproses data
... 
... # Database
... # x = Data, y = Target
... x = [[2],[4],[8],[10],[12],[14],[16],[18],[20],[22]]
... y = [4, 8, 16, 20, 24, 28, 32, 36, 40, 44] # hasil kali 2 dari nilai x
... 
... regr = LinearRegression().fit(x,y) # meregresi dan menampilkan grafik
... regr.score(x,y) # menghasilkan nilai
... 
... # Data uji
... predict = np.array([[60]]) # nilai yang diprediksi
... 
... # Menampilkan data prediksi
... print ("Laila puspitasari 1207030022") # menampilkan nama dan nim
... print ("Prediksi") # menampilkan kata prediksi
... print ("Input = ", predict) # menampilkan kata input dari nilai prediksi
... print ("Output = ", regr.predict(predict)) # menampilkan kata output dari nilai regresi prediksiimport numpy as np # modul numpy untuk memudahkan pengolahan data
... from sklearn.linear_model import LinearRegression # modul untuk memproses data
... 
... # Database
... # x = Data, y = Target
... x = [[2],[4],[8],[10],[12],[14],[16],[18],[20],[22]]
... y = [4, 8, 16, 20, 24, 28, 32, 36, 40, 44] # hasil kali 2 dari nilai x
... 
... regr = LinearRegression().fit(x,y) # meregresi dan menampilkan grafik
... regr.score(x,y) # menghasilkan nilai
... 
... # Data uji
... predict = np.array([[60]]) # nilai yang diprediksi
... 
... # Menampilkan data prediksi
... print ("Laila Puspitasari 1207030022") # menampilkan nama dan nim
... print ("Prediksi") # menampilkan kata prediksi
... print ("Input = ", predict) # menampilkan kata input dari nilai prediksi
