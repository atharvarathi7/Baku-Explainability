import pickle 
import os

class DictionarySaver:
    def __init__(self, directory):
        self.directory = directory

    def save_as_txt(self, filename, dictionary):
        # Ensure the directory exists
        if not os.path.exists(self.directory):
            os.makedirs(self.directory)
        
        # Construct the full file path
        file_path = os.path.join(self.directory, filename)
        
        # Write the dictionary to the file
        with open(file_path, 'w') as file:
            for i in dictionary:
                file.write("----- New Episode--------")
                for key, value in i.items():
                    file.write(f"{key}: {value}\n")

    def save_as_pkl(self, filename, dictionary):
        # Ensure the directory exists
        if not os.path.exists(self.directory):
            os.makedirs(self.directory)
        
        # Construct the full file path
        file_path = os.path.join(self.directory, filename)
        
        # Write the dictionary to the file in binary mode
        with open(file_path, 'wb') as file:
            pickle.dump(dictionary, file)