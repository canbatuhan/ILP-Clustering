import argparse

from structs import Grid
from functions import clustering
from functions import helpers
from functions import logger
from functions import preprocessing
from functions import visualizer


parser = argparse.ArgumentParser(description='ILP Sensor Clustering - Clustering of sensors using Integer Linear Programming concept')
parser.add_argument('--size', required=False, default=100, type=int)
parser.add_argument('--sensor_count', required=False, default=75, type=int)
parser.add_argument('--distance_threshold', required=False, default=15, type=float)
parser.add_argument('--max_score', required=False, default=10, type=int)
parser.add_argument('--min_score', required=False, default=1, type=int)


args = vars(parser.parse_args())
GRID_SIZE = args['size']
SENSOR_COUNT = args['sensor_count']
DISTANCE_THRESHOLD = args['distance_threshold']
MAX_SCORE = args['max_score']
MIN_SCORE = args['min_score']


if __name__=='__main__':
    # ___Initializing___
    grid = Grid(GRID_SIZE)
    # sensor_set = preprocessing.generate_random_sensors(GRID_SIZE, SENSOR_COUNT, MAX_SCORE, MIN_SCORE)
    sensor_set = preprocessing.init_sensors_from_file('docs/input/sensor_locations.tsv')
    preprocessing.set_sensor_scores(sensor_set, 'docs/input/sensor_placements.csv')


    """# ___Building___
    generated_model, gateway_locations = clustering.generate_model(grid)

    # ___Developing___
    developed_model = clustering.develop_model(generated_model, grid,sensor_set, gateway_locations, DISTANCE_THRESHOLD)

    # ___Optimizing___
    gateway_set = clustering.optimize_model(developed_model, grid, gateway_locations)

    # ___Connecting___
    helpers.connect_nodes(sensor_set, gateway_set, DISTANCE_THRESHOLD)

    # ___Logging___
    logger.record_nodes(sensor_set, 'docs/output/log/sensors.txt')
    logger.record_nodes(gateway_set, 'docs/output/log/gateways.txt')

    # ___Visualization___
    visualizer.show_locations("Sensor", sensor_set, grid, 'docs/output/img/sensor_placement.png')
    visualizer.show_locations("Gateway", gateway_set, grid, 'docs/output/img/gateway_placement.png')
    visualizer.show_grid(sensor_set, gateway_set, grid, DISTANCE_THRESHOLD, 'docs/output/img/grid.png')
"""