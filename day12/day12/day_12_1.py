############## Scope #####

enemies = 1

def increase_ennemies():
    #global  enemies
    #enemies += 4
    #print(f"Enemies inside function : {enemies}")
    return enemies + 1

increase_ennemies()

print(f"Enemies outside a function : {enemies}")


'''
def game():
    """Namespace"""
    player_health = 10

    print(player_health)
    def drink_potion():
        player_health = 80
        print(player_health)

    drink_potion()


game()
'''