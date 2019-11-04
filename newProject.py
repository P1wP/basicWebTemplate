#######################################################
###### Automated file creation for web projects #######
#######################################################

#IMPORTS
import os

# Set project name
newProject = input("Project Name?: ")

# Get current Dir
original = os.getcwd()

###CHECK FOR SAME NAME FOLDER
##CHANGE PROJECT NAME IF FOLDER EXISTS
# Create folder
os.mkdir(newProject) # folderName = projectName

# Change Dir to new folder
os.chdir(original + "/" + newProject)

print("Project folder " + newProject + """
Made at """ + original)


# Create sub folders
# img, script, partials, pages ect.
subfolders = ["img", "script", "partials", "pages"]
newDir = os.getcwd()
for i in subfolders:
    print(newProject + "/" + i + " dir --successfull")
    os.mkdir(i)

# Create template files
### Index.html
index = open("index.html", "w")
message = """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<meta http-equiv="X-UA-Compatible" content="ie=edge">
    
<link rel="stylesheet" type="text/css" href="styles.css">
	<title> Title </title>
</head>

<body>

    <script type="text/javascript" src="script.js"></script>
</body>
</html>"""

index.write(message)
index.close()
print( newProject + "/index.html --successfull")

### Script.js
script = open("script.js", "w")
message = """

"""
script.write(message)
script.close()
print(newProject + "/script.js --successfull")

### Styles.sass
styles = open("styles.sass", "w")
message = """

"""
styles.write(message)
styles.close()
print(newProject + "/styles.sass --successfull")

# Open SaSS interpreter
dir = "dir"
commandSass = "sass --watch styles.sass:styles.css"

## Start SASS
print("""
##########################################
""")

def runSass():
    startSass = input("Would you like to start the SASS interpreter? Y/N: ")
    if startSass == "Y":
        os.system("start cmd /k " + commandSass) ##Open CMD sass
    elif startSass == "N":
        print("Fine do it yourself!")   ##DO NOTHING
    else:
        print("Error, Not a valid input!") 
        runSass()  ## ERROR TRY AGAIN
runSass()

# Open project Dir
os.system("explorer")
os.startfile(newDir)

# open CodeEditor
os.startfile("index.html")

# change back to original dir
os.chdir(original)

#Close Python
exit()