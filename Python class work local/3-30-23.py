message = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Duis et euismod nisl. Nulla facilisi. Aliquam euismod lectus ac ipsum cursus, vel aliquam elit semper. Nullam elementum massa quis quam "

words = message.lower().replace(".", "").replace(",", "").split(" ")


word_Count ={}
for word in words:
    if word in word_Count:
        word_Count[word] += 1
    else:
        word_Count[word] = 1

user_input = input("Enter A Word To s=Search: ")

if user_input in word_Count:
    print(f"The word '{user_input}' occurred {word_Count[user_input]} times.")
else:
    print(f"The word '{user_input}' did not occur.")




