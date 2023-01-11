from countryinfo import CountryInfo

country = CountryInfo(input("Digite o nome de um país: "))

print(f'País: {country.name()}')
print(f'Capital: {country.capital()}')
print(f'Moedas: {country.currencies()}')
print(f'Idiomas: {country.languages()}')
print(f'Fazem Fronteira: {country.borders()}')
print(f'Codigo de area: {country.calling_codes()}')
print(f'Populacao: {country.population()}')

# primeiro mini projetinho