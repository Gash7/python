USA=['NewYork','Atlanta','Chicago','Balimotore']
UK=['London','Brostol','Cambreage']
India=['Pune','Mumbai','Delhi']

city1=input('Enter the city name')
city2=input('Enter the city name')


if city1 and city2 in USA:
    print(city1,city2,'is in',USA)

elif city1 and city2 in UK:
    print((city1,city2),'is in',UK)

elif city1 and city2 in India:
    print((city1,city2),'is in',India)

else:
    print('Please enter city name')

