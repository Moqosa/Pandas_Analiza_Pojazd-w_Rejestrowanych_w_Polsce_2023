import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_excel('database.xlsx') #Załadowanie bazy danych

months_to_average = ['styczeń', 'luty', 'marzec', 'kwiecień', 'maj', 'czerwiec', 'lipiec', 'sierpień', 'wrzesień', 'październik'] #Lista tabeli z nazwami miesięcy do pobrania
average_vehical_value = df[months_to_average].mean() #Wyliczenie średniej z każdego miesiąca


creat_list = list(average_vehical_value) #Stworzenie listy w celu zsumowania jej wartości
sum_list_numbers = sum(creat_list) #Sumowanie wartości listy


max_value = df[months_to_average].max() #Znaleznie największej wartości zarejestrowanych pojazdów dla każdego miesiąca
list_of_max_value = list(max_value) #Dodanie nawjwiększaje wartości zarejestrowanych pojazdów do listy


list_of_months_number = [] #Tworzenie jest w celu przypiasaniu numeru miesiąca

for i in range(1, len(months_to_average) + 1): #Pętla do iteracji miesięce i dodania ich jako wartości liczbowe do listy
    list_of_months_number.append(i)


plt.plot(list_of_months_number, average_vehical_value) #Wyświetlanie oraz upiększanie wykresu
plt.grid(True, linestyle='--', alpha=0.7)
plt.scatter(list_of_months_number, average_vehical_value, c='red', marker='o', s=50, edgecolors='black')
plt.xlim(1, 10)
plt.text(4, 10000, f'The average number of registered vehicles \n in Poland in 2023 per month is: {sum_list_numbers/ len(creat_list)}')


plt.xlabel('Months') #Tekst osi X
plt.ylabel('Average number of registered vehicles') #Tekst osi Y

plt.show() #Wyświetlanie wykresu





