Area = {
    "Eldorhaven" : [["Eldoria's Enchanted Forest", "Mysthaven"], ["Route 6", "City of Jewels"], ["Route 7", "Twillight Haven"]],
    "Mysthaven" : [["Route 2", "Celestria"], ["Route 1", "Stonegate"], ["Eldoria's Enchanted Forest", "Eldorhaven"]],
    "Celestia" : [["Route 5", "Emberfall"], ["Route 2", "Mysthaven"]],
    "Emberfall" : [["City gate", "City of Jewels"], ["Route 5", "Celestia"]],
    "City of Jewels" : [["City gate", "Emberfall"], ["Route 6", "Eldorhaven"], "Beach Side"],
    "Beach Side" : ["City of Jewels"],
    "Stonegate" : [["Forest of Rumors", "Rogue town"],["Route 1", "Mysthaven"]],
    "Roguetown" : [['Forest of Rumors', "Stonegate"]],
    "Solstice City" : [],
    "City of Death" : [["Route 3", "Ghost Town"]],
    "Ghost Town" : [["Route 4", "Thunderpeak"],["Route 3", "City of Death"]],
    "Thunderpeak" : [["Route 4", "Ghost Town"]],
    "Twillight Haven" : [["Route 7", "Eldorhaven"]]
}

Area_elements = {
    "Eldorhaven" : ["Your House", "Someone's House", "Lyra's Enchantment Store", "Guildcenter", "Eldorius's Statue"],
    "Mysthaven" : ["Guildcenter", "Someone's House", "Someone's House", "A Pond"],
    "Celetria" : ["Celestria's Circus", "Celestria's Mart","Someone's House", "Someone's House", "Backyard"],
    "Emberfall" : ["Guildcenter", "Someone's House", "Rebellions's Residence", "The Red Waterfall"],
    "City of Jewels" : ["Guildcenter", "Jewellery shop", "Shadow Hideout", "Eldoria's Musuem"],
    "Beach Side" : ["Brook's House"], 
    "Stonegate" : ["Train Station", "Jeremy's House"],
    "Solstice City" : ["Solstice Arena", "Guildcenter", "Train Station"], 
    "Rogue Town" : ["Malik's House", "Ruined Guildcenter", "Ancient Ruins"],
    "City of death" : ["Graveyard", "Train Station"],
    "Ghost Town": ["Someone's House", "Someone's House", "Someone's House", "Ghosted House", "A Strange Sign"],
    "Thunderpeak" : ["Eldoria's Palace", "Wishing Well", "Shipping Area"],
    "Twillight Haven": ["Guildcenter", "Local Mart", "Shipping Area"]

}
current_task = []
task = []
inventory = []
location = 'Eldorhaven'
location_element = ''
visited = []
dead = []