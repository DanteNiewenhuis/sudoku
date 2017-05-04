import readMap
import dfs
import hill_solve
import draw
import sim_an_search

#map = readMap.readStates('UnitedStates.txt')

signals = ['zA', 'zB', 'zC', 'zD', 'zE', 'zF', 'zG']
signal_costs = {'zA':19, 'zB':20, 'zC':21, 'zD':23, 'zE':36, 'zF':37, 'zG':38}

#dfs.dfs(map, signals)
map = readMap.read_complete_map('')
sim_an_search.hill_climber(map, signal_costs, signals, 200000, 5, 0.001)
#hill_solve.hill_climber(map, signal_costs, signals)
#draw.draw_america(map, signal_costs)