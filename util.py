### function to assign user's ethnicity
def assign_eth(entry):
    if entry == "white":
        return "white only"
    elif entry == "black":
        return "black only"
    elif entry == "asian":
        return "asian only"
    elif entry == "hispanic / latin":
        return "latino / hispanic only"
    elif entry == "native american":
        return entry
    elif entry == "pacific islander":
        return entry
    elif entry == "indian":
        return entry
    elif entry == "middle eastern":
        return entry
    elif entry == "unknown":
        return entry
    else:
        return "mixed"
    
### function to count the number of languages a user speaks
def count_languages(row):
    num_languages = 0
    languages = row.split(", ")
    for i in languages:
        if i != "c++":
            num_languages += 1
        else:
            continue
    return num_languages

### function to classify user's location
northeast = ["connecticut", "maine", "massachussetts", "new hampshire", "rhode island", 
             "vermont", "new jersey", "new york", "pennsylvania"]
midwest = ["illinois", "indiana", "michigan", "ohio", "wisconsin", "iowa", "kansas", 
           "minnesota", "missouri", "nebraska", "north dakota", "south dakota"]
south = ["delaware", "district of columbia", "florida", "georgia", "maryland", 
         "north carolina", "south carolina", "virginia", "west virginia", "alabama",
         "kentucky", "mississippi", "tennessee", "arkansas", "louisiana", "oklahoma", "texas"]
west = ["arizona", "colorado", "idaho", "montana", "nevada", "new mexico", "utah", "wyoming",
        "alaska", "california", "hawaii", "oregon", "washington"]

def classify_location(row):
    full_location = row.split(", ")
    if full_location[-1] in northeast:
        return "northeast"
    elif full_location[-1] in midwest:
        return "midwest"
    elif full_location[-1] in south:
        return "south"
    elif full_location[-1] in west:
        return "west"
    else:
        return "not united states"
    
### function to map the user's education
hs_less = ["graduated from high school", "dropped out of high school", "working on high school",
           "high school", "dropped out of college/university", "dropped out of two-year college",
           "dropped out of med school", "dropped out of law school"]
uni_coll = ["working on college/university", "graduated from college/university",
            "working on two-year college", "college/university", "two-year college", 
            "graduated from two-year college", "working on med school", "graduated from law school",
            "graduated from med school", "working on law school", "law school", 
            "dropped out of masters program", "med school", "dropped out of masters program"]
masters_more = ["graduated from masters program", "working on masters program", "graduated from ph.d program",
                "working on ph.d program", "masters program", "dropped out of ph.d program", "ph.d program"]
space_camp = ["working on space camp", "graduated from space camp", "dropped out of space camp", "space camp"]

def map_education(row):
    if row in hs_less:
        return "high school or less"
    elif row in uni_coll:
        return "university/college"
    elif row in masters_more:
        return "masters or more"
    elif row in space_camp:
        return "space camp"
    elif row == "not disclosed":
        return row
    else:
        return row

### dictionary to map the user's job to a broader category
job_dict = {
    # STEM & IT
    "computer / hardware / software": "STEM & IT",
    "science / tech / engineering": "STEM & IT",

    # Finance & Business
    "banking / financial / real estate": "Finance & Business",
    "sales / marketing / biz dev": "Finance & Business",
    "executive / management": "Finance & Business",

    # Service & Travel
    "transportation": "Service & Travel",
    "hospitality / travel": "Service & Travel",
    "clerical / administrative": "Service & Travel",

    # Creative & Media
    "artistic / musical / writer": "Creative & Media",
    "entertainment / media": "Creative & Media",

    # Public Service & Government
    "political / government": "Public Service & Government",
    "law / legal services": "Public Service & Government",
    "military": "Public Service & Government",

    # Health & Education
    "medicine / health": "Health & Education",
    "education / academia": "Health & Education",

    # Trades & Manual Labor
    "construction / craftsmanship": "Trades & Manual Labor",

    # Non-working
    "student": "Non-working",
    "unemployed": "Non-working",
    "retired": "Non-working",

    # Other/Rather not say/Undisclosed
    "not disclosed": "Other/Rather not say/Undisclosed",
    "other": "Other/Rather not say/Undisclosed",
    "rather not say": "Other/Rather not say/Undisclosed"
}

### function to map user's body type
bt_thin = ["thin", "skinny", "used up"]
bt_plus_sized = ["a little extra", "curvy", "full figured", "overweight"]
bt_sporty = ["athletic", "fit", "jacked"]
bt_undisclosed = ["not disclosed", "rather not say"]

def map_body_type(row):
    if row in bt_thin:
        return "thin"
    elif row in bt_plus_sized:
        return "plus-sized"
    elif row in bt_sporty:
        return "sporty"
    elif row in bt_undisclosed:
        return "undisclosed"
    else:
        return row

### function to determine diet strictness
def diet_strictness(row):
    split_row = row.split(" ")
    if (len(split_row) > 1) and (split_row[-1] != "disclosed"):
        if split_row[0] == "strictly":
            return "strict"
        elif split_row[0] == "mostly":
            return "somewhat strict"
    else:
        return "undisclosed"
    
### function to determine whether the user wants kids
def wants_kids(row):
    if row == "not disclosed":
        return "not disclosed"
    elif "does" in row:
        return "doesn't want"
    elif "might" in row:
        return "might want them/might want more"
    elif "wants more" in row:
        return "wants them/wants more"
    else:
        return "not disclosed"
    
### function to determine the importance of the user's religion
def religion_importance(row):
    if "laughing about it" in row:
        return "laughing about it"
    elif "not too serious about it" in row:
        return "not too serious about it"
    elif "somewhat serious about it" in row:
        return "somewhat serious about it"
    elif "very serious about it" in row:
        return "very serious about it"
    else:
        return "not disclosed"
    
### function to for the importance of the user's star sign
def sign_importance(row):
    if "does" in row:
        return "doesn't matter"
    elif "fun to think about" in row:
        return "it's fun to think about it"
    elif "matters a lot" in row:
        return "it matters a lot"
    else:
        return "not disclosed"

### function to determine whether the user has pets
def has_pets(row):
    if "has dogs and has cats" in row:
        return "has cats and dogs"
    elif "has cats" in row:
        return "has cats"
    elif "has dogs" in row:
        return "has dogs"
    else:
        return "not disclosed"
    
### function to determine whether the user likes pets
def likes_pets(row):
    if "likes dogs and likes cats" in row:
        return "likes cats and dogs"
    elif "likes dogs" in row:
        return "likes dogs"
    elif "likes cats" in row:
        return "likes cats"
    else:
        return "not disclosed"
    
### function to determine whether the user dislikes pets
def dislikes_pets(row):
    if "dislikes dogs and dislikes cats" in row:
        return "dislikes cats and dogs"
    elif "dislikes dogs" in row:
        return "dislikes dogs"
    elif "dislikes cats" in row:
        return "dislikes cats"
    else:
        return "not disclosed"

### function to plot counts for EDA
def create_count_plot(data, var_name):
    import matplotlib.pyplot as plt
    import seaborn as sns

    plt.figure(figsize = (10, 6))
    ax = sns.countplot(x = data, palette = "bright", stat = "percent")

    # add percentage labels to each bar
    for c in ax.containers:
        ax.bar_label(c, fmt = "%.1f%%")
    
    ax.margins(y = 0.1)

    # set up the rest of the graph
    plt.xticks(rotation = 45)
    plt.title("Proportion of classes", fontsize = 16)
    plt.xlabel(var_name, fontsize = 12)
    plt.ylabel("Proportion (%)", fontsize = 12)
    plt.show()
    plt.clf()