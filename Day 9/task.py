#Example of simple dictionary
capitals = {
    "France":"Paris",
    "Germany":"Berlin"
}

#Nested List in Dictionary
#Example, Travel log of all the cities I have been in each of the countries I've been in
#travel_log = {
#    "France": ["Paris", "Lille", "Dijon"],
#    "Germany":["Stuttgart", "Berlin"],
#}

#Task, print Lille
#france_cities = travel_log["France"]
#print(france_cities[1])

#Better way
#print(travel_log["France"][1])

#2D list, list inside of a list
nested_list = ["a","b", ["c","d"]]

#Print out the letter D from the nested list
print(nested_list[2][1])

#Can nest a dictionary within a dictionary itself
#For example, how many times you visited the country
travel_log = {
    "France": {
        "cities_visited":["Paris", "Lille", "Dijon"],
        "total_visits":12
    },
    "Germany":{
        "cities_visited":["Stuttgart", "Hamburg","Berlin"],
        "total_visits":5
    },
}

#Task print out Stuttgart
print(travel_log["Germany"]["cities_visited"][0])