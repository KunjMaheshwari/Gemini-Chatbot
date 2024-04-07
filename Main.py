import google.generativeai as genai

API_KEY = "key";

genai.configure(api_key= API_KEY)

model = genai.GenerativeModel('gemini-pro')

# res = model.generate_content("Write a program in Python to print the first 10 even numbers from 0")
while True:
    query = input("Gemini: What do you want to know today?\n Your Response: ")
    if query == "exit":
        print("Gemini: Bye!")
        break
    response = model.generate_content(query)
    print("Gemini: ", response.text)
