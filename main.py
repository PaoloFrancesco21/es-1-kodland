meme_dict = {
            "CRINGE": "Qualcosa di eccezionalmente strano o imbarazzante",
            "LOL": "Una risposta comune a qualcosa di divertente",
            }
parola = input("Scrivi una parola che non capisci (usa solo lettere maiuscole!): ")
if parola in meme_dict.keys():
    print(meme_dict[parola])
    # Cosa fare se la parola è stata trovata?
else:
    # Cosa fare se la parola non è stata trovata?
    print("la parola non è stata trovata")
    
