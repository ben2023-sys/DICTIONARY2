from tkinter import Tk, Entry, Button, Label, StringVar, Toplevel

# Main application window
window = Tk()
window.geometry("600x400")
window.title("Multilingual Dictionary")

Label(
    window,
    text="Select a Language Dictionary",
    font=('Arial', 20, 'bold'),
    pady=20
).pack()


# Function to create a dictionary window
def create_dictionary_window(title, dictionary):
    def open_window():
        new_window = Toplevel(window)
        new_window.title(f"{title} Dictionary")
        new_window.geometry("400x300")

        Label(new_window, text=f"{title} Dictionary", font=('Arial', 16, 'bold')).pack(pady=10)

        entry_text = Entry(new_window, font=('Arial', 14))
        entry_text.pack(pady=10)

        result = StringVar()
        Label(new_window, textvariable=result, font=('Arial', 14), fg="blue").pack(pady=10)

        def search():
            word = entry_text.get().strip().lower()
            result.set(dictionary.get(word, "Not Found"))

        Button(
            new_window,
            text="Search",
            font=('Arial', 14),
            width=10,
            command=search
        ).pack(pady=10)

    return open_window


# Dictionaries for each language
spanish_dictionary = {
    "manzana": "apple",
    "árbol": "tree",
    "casa": "house",
    "gato": "cat",
    "perro": "dog",
    "coche": "car",
    "silla": "chair",
    "mesa": "table",
    "libro": "book",
    "flor": "flower",
    "escuela": "school",
    "maestro": "teacher",
    "amigo": "friend",
    "agua": "water",
    "comida": "food",
    "camisa": "shirt",
    "pantalones": "pants",
    "días": "days",
    "mes": "month",
    "años": "years",
}

tiv_dictionary = {
    "nyian": "apple",
    "ior": "tree",
    "agha": "house",
    "mbáka": "cat",
    "mbwa": "dog",
    "gba": "car",
    "kpatema": "chair",
    "kpado": "table",
    "áka": "book",
    "kpande": "flower",
    "kase": "school",
    "orvenda": "teacher",
    "orhemen": "friend",
    "amem": "water",
    "mnger": "food",
    "ivenda": "shirt",
    "gbande": "pants",
    "tar": "days",
    "mbagede": "month",
    "ikyô": "years",
    }

french_dictionary = {"pomme": "apple",
    "arbre": "tree",
    "maison": "house",
    "chat": "cat",
    "chien": "dog",
    "voiture": "car",
    "chaise": "chair",
    "table": "table",
    "livre": "book",
    "fleur": "flower",
    "école": "school",
    "professeur": "teacher",
    "ami": "friend",
    "eau": "water",
    "nourriture": "food",
    "chemise": "shirt",
    "pantalon": "pants",
    "jours": "days",
    "mois": "month",
    "années": "years",
}
german_dictionary = {
    "apfel": "apple", "baum": "tree", "haus": "house", "katze": "cat", "hund": "dog",
    "auto": "car", "stuhl": "chair", "tisch": "table", "buch": "book", "blume": "flower",
    "schule": "school", "lehrer": "teacher", "freund": "friend", "wasser": "water",
    "essen": "food", "hemd": "shirt", "hose": "pants", "tage": "days",
    "monat": "month", "jahre": "years",
}

igbo_dictionary = {
"ugbo mmiri": "boat",
    "ulo": "house",
    "nri": "food",
    "mmiri": "water",
    "akwukwo": "book",
    "anu": "meat",
    "ahia": "market",
    "ulo akwukwo": "school",
    "nwoke": "man",
    "nwanyị": "woman",
    "nwa": "child",
    "ututu": "morning",
    "ehihie": "afternoon",
    "abalị": "night",
    "oku": "fire",
    "ohịa": "forest",
    "osimiri": "river",
    "ulo ọgwụ": "hospital",
    "ulo nzukọ": "church",
    "ulo mposi":"toilet"
}

# Buttons to open dictionary windows
Button(
    window, text="spanish Dictionary", font=('Arial', 14), width=25,
    command=create_dictionary_window("spanish", spanish_dictionary)
).pack(pady=10)

Button(
    window, text="tiv Dictionary", font=('Arial', 14), width=25,
    command=create_dictionary_window("tiv", tiv_dictionary)
).pack(pady=10)

Button(
    window, text="french Dictionary", font=('Arial', 14), width=25,
    command=create_dictionary_window("french", french_dictionary)
).pack(pady=10)

Button(
    window, text="German Dictionary", font=('Arial', 14), width=25,
    command=create_dictionary_window("German", german_dictionary)
).pack(pady=10)

Button(
    window, text="Igbo Dictionary", font=('Arial', 14), width=25,
    command=create_dictionary_window("Igbo", igbo_dictionary)
).pack(pady=10)

# Run the application
window.mainloop()
