import tkinter as tk

# Function to display dictionaries
def display_dictionary(language):
    dictionaries = {
        #IRO BENEDICT
        'German.dic': {'Hund': 'Dog', 'Katze': 'Cat', 'Haus': 'House', 'Baum': 'Tree', 'Auto': 'Car', 'Buch': 'Book', 'Tisch': 'Table', 'Stuhl': 'Chair', 'Tür': 'Door', 'Fenster': 'Window', 'Blume': 'Flower', 'Himmel': 'Sky', 'Wasser': 'Water', 'Feuer': 'Fire', 'Erde': 'Earth', 'Mond': 'Moon', 'Sonne': 'Sun', 'Stern': 'Star', 'Berg': 'Mountain', 'Fluss': 'River'},
       #Sunday Michael Ekene
        'French.dic': { 'bonjour': 'hello',
    'merci': 'thank you',
    'oui': 'yes',
    'non': 'no',
    'au revoir': 'goodbye',
    'bien': 'good',
    'mal': 'bad',
    'amour': 'love',
    'ami': 'friend',
    'maison': 'house',
    'chat': 'cat',
    'nuit': 'night',
    'chien': 'dog',
    'voiture': 'car',
    'arbre': 'tree',
    'fleur': 'flower',
    'livre': 'book',
    'ecole': 'school',
    'ville': 'city',
    'pays': 'country'},
        #Daniel Chima Okeke
        'Igbo.dic': {"Nne": "Mother",
        "Nna": "Father",
        "Ụlọ": "House",
        "Akwụkwọ": "Book",
        "Ezi": "Good",
        "Nri": "Food",
        "Mmiri": "Water",
        "Anụ": "Meat",
        "Ọkụ": "Fire",
        "Ụwa": "World",
        "Ọgwụ": "Medicine",
        "Ekwensu": "Devil",
        "Chineke": "God",
        "Ihu": "Face",
        "Akwụkwọ ozi": "Letter",
        "Ndị mmadụ": "People",
        "Ọhịa": "Forest",
        "Ugo": "Eagle",
        "Nche": "Guard",
        "Eziokwu": "Truth"},
        #MARTINS GOODLUCK DANIEL
        'Spanish.dic': {
            'ola' : 'Hello',
            'Adiós' : 'Goodbye',
            'Gracias' : 'Thank you',
            'Agua' : 'Water',
            'Comida' : 'Food',
            'Casa' : 'House',
            'Coche' : 'Car',
            'Árbol' : 'Tree',
            'Perro' : 'Dog',
            'Gato' : 'Cat',
            'Sol' : 'Sun',
            'Padre' : 'Father',
            'Madre' : 'Mother',
            'Hermano' : 'Brother',
            'Hermana' : 'Sister',
            'Amigo' : 'Friend',
            'Amor' : 'Love',
            'Feliz' : 'Happy',
            'Hermosa' :'Beautiful',
            'Padre' : 'Father'
            },
        #AKASE IWASEN MICHAEL
        'Tiv.dic':{
    'Ter':'Father',
    'Aondo':'God',
    'Msuugh':'I greet',
    'Oryiman':'Saviour',
    'Angbyian':'Sibling',
    'Kwase':'Girl',
    'Nomso':'Boy',
    'Ngo':'Mother',
    'Dem':'Leave me',
    'Se':'Us',
    'Hemba':'More than',
    'Doo':'Good',
    'Vihi':'Spoil',
    'Kanyi':'What',
    'Jijingi':'Spirit',
    'Shima':'Heart',
    'Uma':'Life',
    'Humba':'Better',
    'Or':'Person',
    'Hembe':'Break'}
    }
    # Format dictionary output for readability
    selected_dict = dictionaries.get(language, 'Not available')
    formatted_text = f"{language} Dictionary:\n"
    for key, value in selected_dict.items():
        formatted_text += f"{key}: {value}\n"
    result_text.config(state=tk.NORMAL)
    result_text.delete(1.0, tk.END)
    result_text.insert(tk.END, formatted_text)
    result_text.config(state=tk.DISABLED)

# Create main window
root = tk.Tk()
root.title("Dictionaries App")
root.geometry("800x700")
root.configure(bg='#f0f0f0')

# Add a title label
title_label = tk.Label(root, text="Dictionaries App", font=("Helvetica", 18, "bold"), bg='#f0f0f0')
title_label.pack(pady=20)

# Create a text widget to display the dictionary output
result_text = tk.Text(root, font=("Helvetica", 12), bg='#f0f0f0', height=25, width=70, wrap=tk.WORD)
result_text.pack(pady=20)
result_text.config(state=tk.DISABLED)

# Button data with titles
buttons = [
    "German.dic",
    "French.dic",
    "Igbo.dic",
    "Spanish.dic",
    "Tiv.dic"
]

# Create buttons
for text in buttons:
    btn = tk.Button(root, text=text, command=lambda t=text: display_dictionary(t), height=1, width=20, bg='#4caf50', fg='white', font=("Helvetica", 12))
    btn.pack(pady=10)

# Run the application
root.mainloop()
