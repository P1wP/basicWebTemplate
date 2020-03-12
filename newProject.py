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
start = """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<meta http-equiv="X-UA-Compatible" content="ie=edge">

"""
index.write(start)

# JQuery?
# Included with Bootstrap
def addJQuery():
    jQuery = input("Do you want JQuery? Y/N: ").upper()#input to uppercase
    if jQuery == "Y":
        query = """

        <!-- JQuery -->
        <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.4.1/jquery.min.js"></script>
        """
        index.write(query)
        print("JQuery --successfull")
    elif jQuery == "N":
        print("NO JQuery for you.")
    else:
        print("ERROR: invalid input")
        addJQuery()


# Boostrap?
def addBootrap():
    bootstrap = input("Do you want Bootstrap? Y/N: ").upper() # input to upper

    if bootstrap == "Y":
        boot = """

        <!-- BootStrap -->
        <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.4.1/css/bootstrap.min.css">
        <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.4.1/jquery.min.js"></script>
        <script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.16.0/umd/popper.min.js"></script>
        <script src="https://maxcdn.bootstrapcdn.com/bootstrap/4.4.1/js/bootstrap.min.js"></script>"""
        index.write(boot)
        print("Bootstrap --successfull")

    elif bootstrap == "N":
        print("NO bootstrap for you.")
        addJQuery()
    else:
        print("ERROR: invalid input")
        addBootrap()
addBootrap()


# FontAwsome?
def addFontawesome():

    fontAwesome = input("Do you want fontawesome? Y/N: ").upper() #input to uppercase
   
    if fontAwesome == "Y":
        font = """

        <!-- FontAwesome -->
        <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css">"""
        index.write(font)
        print("FontAwesome --successfull")
    elif fontAwesome == "N":
        print("NO fontawesome for you.")
    else:
        print("ERROR: invalid input")
        addFontawesome()
addFontawesome()

# CLOSE INDEX.HTML
end = """
    <!-- CSS -->
    <link rel="stylesheet" type="text/css" href="styles.css">

    <!-- TITLE -->
	<title> """ + newProject + """ </title>
</head>

<body>
    Hello World!


    <!-- SCRIPTS -->
    <script type="text/javascript" src="script.js"></script>
</body>
</html>"""

index.write(end)
index.close()
print( newProject + "/index.html --successfull")


#### CREATE OTHER FILES ####

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
    startSass = input("Would you like to start the SASS interpreter? Y/N: ").upper()# Input to UpperCase

    # Check Input from user
    if startSass == "Y":
        os.system("start cmd /k " + commandSass) ##Open CMD sass
    elif startSass == "N":
        print("Fine do it yourself!")   ##DO NOTHING
    else:
        print("ERROR: invalid input") 
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