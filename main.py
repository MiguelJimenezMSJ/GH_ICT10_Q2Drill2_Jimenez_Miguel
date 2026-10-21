from pyscript import display, document

#set of members for each grade
Grade7 = {'Ladis Wusherrum', 'Alison Burgers', 'Employs mus-Wushderhants', 'Richard Watterson'}
Grade8 = {'Optimus Prime', 'MegaTron'}
Grade9 = {'Robert E.O. Speedwagon', 'Rudol von Stroheim'}
Grade10 = {'Peter Cullen', 'Frank Welker'}

#combines all into 1 set
Current_members = Grade7 | Grade8 | Grade9 | Grade10
#store new member
New_members = set()

def student_club(e):
    #gets the first and last name from input field
    Fname = document.getElementById('First_name').value
    Lname = document.getElementById('Last_name').value

    #add the new member and removes blank entries
    New_members.add(f'{Fname} {Lname}'.strip())
    New_members.discard('')

    #combines old and new members
    All_members = Current_members | New_members

    result = document.getElementById('result')
    result.innerHTML = ""

    display(f"Total Members: {len(All_members)}", target='result')
    display(f"All Members: {All_members}", target='result')