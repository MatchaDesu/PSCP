"Phasmophobia"

banshee = ["EMF Level 5","Fingerprints","Freezing Temperatures"]
demon = ["Ghost Writing","Spirit Box","Freezing Temperatures"]
jinn = ["EMF Level 5","Spirit Box","Ghost Orb"]
mare = ["Spirit Box","Freezing Temperatures","Ghost Orb"]
oni = ["EMF Level 5","Ghost Writing","Spirit Box"]
phantom = ["EMF Level 5","Freezing Temperatures","Ghost Orb"]
poltergeist = ["Fingerprints","Spirit Box","Ghost Orb"]
revenant = ["EMF Level 5","Ghost Writing","Fingerprints"]
shade = ["EMF Level 5","Ghost Writing","Ghost Orb"]
spirit = ["Ghost Writing","Fingerprints","Spirit Box"]
wraith = ["Fingerprints","Spirit Box","Freezing Temperatures"]
yurei = ["Ghost Writing","Freezing Temperatures","Ghost Orb"]

def main() :
    "main"
    evidence = ["Ghost Orb","Spirit Box", "Fingerprints", "EMF Level 5", \
        "Freezing Temperatures", "Ghost Writing"]

    discovered = ""

    ghost_dict = {
        "banshee": banshee,
        "demon": demon,
        "jinn": jinn,
        "mare": mare,
        "oni": oni,
        "phantom": phantom,
        "poltergeist": poltergeist,
        "revenant": revenant,
        "shade": shade,
        "spirit": spirit,
        "wraith": wraith,
        "yurei": yurei
    }

    ghost_name = list(ghost_dict.keys())

    for i in range(3) :
        discovered = input()
        if discovered in evidence :
            ghost_name = list(filter(lambda x : discovered in ghost_dict[x] ,ghost_name))

    if len(ghost_name) > 0 :
        for i in ghost_name :
            print(i.title())
    else :
        print("Not yet discovered")

main()
