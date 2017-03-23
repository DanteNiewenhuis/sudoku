import random
import dfs
import analyse
import math
#import matplotlib.pyplot as plt

def revert_changes(swapped_state):
    state = swapped_state[0]
    state.signal = swapped_state[1]

def swap_state(map, signals):
    swapped_state = random.choice(map)
    old_signal = swapped_state.signal
    possible_signals = dfs.possible_signals(signals, swapped_state)
    new_signal = random.choice(possible_signals)
    swapped_state.signal = new_signal
    return [swapped_state, old_signal]

def hill_climber(map, costs, signals):
    #plot = []
    freq = analyse.signal_frequentie(map)
    old_costs = analyse.get_cost(freq, costs)
    for x in range(1,1000):
        #plot.append(old_costs)
        checker = 0
        temperature = 200-0.5*x
        if temperature <= 0:
            temperature = 1
        swapped_state = swap_state(map, signals)
        new_freq = analyse.signal_frequentie(map)
        new_costs = analyse.get_cost(new_freq, costs)
        improvement = old_costs - new_costs
        try:
            chance = math.exp(improvement/temperature)
            if chance > 1:
                chance = 1
        except OverflowError:
            chance = 0
        if random.random() < chance:
            checker = 1
        if checker == 1:
            old_costs = new_costs
        else:
            revert_changes(swapped_state)
    '''
    plt.plot(plot)
    plt.ylabel('kosten')
    plt.xlabel('iteraties')
    plt.show()
    '''
    return map