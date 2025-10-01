def add_notes(filename):
    note=input("Enter your note")
    with open(filename,"a") as file:
        file.write(note+"\n")
    print("note saved")
def view_notes(filename):
    try:
        with open(filename,"r") as file:
            notes=file.readlines()
            if notes:
                print("all notes")
                for idx,note in enumerate(notes,1):
                    print(f"{note}")
            else:
                print("notes not found")
    except FileNotFoundError:
        print("no notes file found")
def search_notes(filename):
    term=input("Enter the term")
    try:
        with open(filename,"r") as file:
            found=False
            for line in file:
                if term.lower() in line.lower():
                    print(line.strip())
                    found=True
            if not found:
                print("the line of term is not found")
    except FileNotFoundError:
        print("no notes file found")
def main():
    filename=input("Enter the filename")
    while True:
        print("\n notes taking app")
        print("1.add notes")
        print("2.view all notes")
        print("3.search notes")
        print("4.quit")
        choice=int(input("Enter your choice"))
        if choice==1:
            add_notes(filename)
        elif choice==2:
            view_notes(filename)
        elif choice==3:
            search_notes(filename)
        elif choice==4:
            print("finished")
            break
        else:
            print("invalid choice")
if __name__=="__main__":
    main()