print('I am a module')

# from here you go to the terminal below and go to the following path
    # C:\Users\Tyler\Documents\(1) PCAP - Modules and Packages\(1.6) modules_own_module
    # after you are in the path, input the following ---> python main.py
"""
    what this does --> in the main.py file you have 'import own_module', so when you run 'python main.py' in the terminal it executes the code in the own_module.py file
    
    when a module is imported, its contents are excuted automatically
    
    However, this isn't very useful when importing modules in a practical sense. You aren't going to import a module to print a statement
    
    That being said --> that's why most modules have functions and variable definitions within them
        Nothing will be outputted, however since python runs through the file line by line, you will have access to all the content
"""
    
# __name__ == '__main__'
    # It Allows You to Execute Code When the File Runs as a Script, but Not When It's Imported as a Module
    
if __name__ == '__main__':
    print('File executed directly')
else:
    print('File executed as a module')
    

# public and private variables
    # variables with single or double underscores at the beginning of a variable 
        # means the user should never modify the variable
        
        
    