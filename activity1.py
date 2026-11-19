import pandas as pd
import matplotlib.pyplot as plt

countries_df=pd.read_csv('countries Data.csv')
countries=countries_df

countries.head(3)

c_52=countries[countries['Country Name']=='United States']
c_52.head(3)

c_07=countries[countries['Country Name']=='India']
c_07.head(3)

type(c_52)

c_merge=c_52.merge(c_07, on='Year', how='inner')
c_merge.head(3)

c_merge=c_merge[['Year', 'Country Name_x', 'Country Name_y', 'GDP_x', 'GDP_y']]
c_merge.head(3)

c_merge['ppopulation_growth']=(c_merge['Population_y']-c_merge['Population_x'])/c_merge['Population_x']*100
c_merge.head(3)

#test the math
3145637627847364346 - 456478321567

c_merge['GDP_growth']=(c_merge['GDP_y']-c_merge['GDP_x'])/c_merge['GDP_x']*100
c_merge.head(3)

c_merge.shape, type(c_merge)

c_merge=c_merge.sort_values('population_growth', ascending=False)
c_merge.head(3)
c_merge.shape

c_merge
names=[
    'china',
    'India',
    'United States',
    'Indonesia',
    'Pakistan',
    'Brazil',
    'Nigeria',
    'Bangladesh',
    'Russia'
]
pop_grow=c_merge['population_growth']/10**6
plt.figure(figsize=(15,9))
plt.bar(names, pop_grow)
plt.xlabel('Countries')
plt.ylabel('Population Growth (in millions)')
plt.title('Population Growth of Countries')

plt.xticks(rotation=45)

for x,y in zip (names,pop_grow):
    label="{:.2f}".format(y)

    plt.annotate(label, (x,y), textcoords="offset points", xytext=(0,10), ha='center')

plt.show()