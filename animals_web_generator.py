import json 


def load_data(file_path):
    '''Loads json file'''
    with open(file_path, "r") as handle:
        return json.load(handle)
    

def load_html(file_path):
    '''Load html file'''
    with open(file_path, "r") as handler:
        html_data = handler.read()
        return html_data


def save_data(filename, data):
    '''save data to new file'''
    with open(filename, "w") as handler:
        handler.write(data)


def get_animal_facts(data):
    '''Print data from animal dictionary'''
    animal_data_string = ""

    # Iterate animal dict extract data add with html tags to animal_data_string
    for animal in data:
        animal_data_string += '<li class="cards__item">\n'
        try:
            animal_data_string += f"Name: {animal['name']}\n"
        except KeyError:
            pass
        
        try:
            animal_data_string += f"Diet: {animal['characteristics']['diet']}\n"
        except KeyError:
            pass
        
        try:
            animal_data_string += f"Location: {animal['locations'][0]}\n"
        except KeyError:
            pass
        
        try:
            animal_data_string += f"Type: {animal['characteristics']['type']}\n"
        except KeyError:
            pass
        animal_data_string += '</li>\n'
    return animal_data_string
        


def main():
    # Load all the data 
    animals_json = load_data('animals_data.json')
    animal_facts = get_animal_facts(animals_json)
    animals_html_file = load_html('animals_template.html')

    # Replace somethin in animals_html_file
    animals_html_file = animals_html_file.replace("__REPLACE_ANIMALS_INFO__", animal_facts)

    # Save the file
    save_data("animals.html", animals_html_file)


if __name__ == "__main__":
    main()