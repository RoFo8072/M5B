from random import randint
def splash():
    print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n              Biathlon\n\n         a hit or miss game \n ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")

def open():
    return(0)

def closed():
    return(1)
    
def is_open(target):
    if target == open():
        return(True)
    else:
        return(False)
    
def is_closed(target):
    if target == closed():
        return(True)
    else:
        return(False)
    
def new_targets():
    targets = [open()] * 5
    return(targets)

def close_target(target, targets):
    if targets[target] == open():
        targets[target] = closed()  

def hits(targets):
    hit = 0
    for n in range(5):
        if is_closed(targets[n]):
            hit +=1        
    print(hit)
    
def target_to_string(target):
    if is_open(target):
        return("* ")
    else:
        return("0 ")

def targets_to_string(targets):
    s = ""
    for n in range(5):
        s = s + target_to_string(targets[n])
    return(s)
    
def view_targets(targets):
    print("\n0 1 2 3 4\n\n" + targets_to_string(targets)+"\n")

def random_hit():
    return(is_open(randint(0,1)))

def shoot(target, targets):
    if random_hit():
        if is_open(targets[target]):
            print("Hit on open target")
            close_target(target, targets)
        else:
            print("Hit on closed target")
    else:
            print("Miss")
    
splash()
ts = new_targets()
while targets_to_string(ts) != ("0 0 0 0 0 "):
    x = input("Choose target: ")
    try:
        x = int(x)
        if x < 4
            shoot(x, ts)
            view_targets(ts)  
    except (ValueError, IndexError):
        print("Invalid target")
print("Game over, all targets hit") 
