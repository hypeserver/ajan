import random
import operator
from functools import lru_cache

from mesa import Agent

from behaviors import Racism, Education

RACES = ["blue", "red", "green", "purple"]
COLOURS = RACES
LANGUAGES = ["telefen", "falakan", "bodoron", "zinaten"]

# Should deprecate and use the agent.origins
Ethnicities = range(4)


class PersonAgent(Agent):
    behaviors = [Racism, Education]

    def __init__(self, **kwargs):
        self.nationalism = random.randint(1,20)
        self.origins = Origins.random()

        self.education = random.randint(1,20)
        self.is_living = True

        self.known_origins = {str(race): origin for race, origin in self.origins.items() if origin >= 0.25}
        self.known_origin_names = [str(race) for race, origin in self.origins.items() if origin >= 0.25]
        self.sorted_known_origins = sorted(self.known_origins.items(), key=operator.itemgetter(1), reverse=True)
        self.sorted_known_origin_names = list(dict(self.sorted_known_origins).keys())
        self.rsorted_known_origin_names = list(reversed(self.sorted_known_origin_names))
        self.sorted_origins = sorted(self.origins.items(), key=operator.itemgetter(1), reverse=True)
        self.sorted_origin_names = tuple(dict(self.sorted_origins).keys())
        self.dominant_origin = self.sorted_origins[0][0]

        self.ethnicity = self.dominant_origin

        self.cellmates_hated = 0

        super().__init__(kwargs.get('unique_id'), kwargs.get('model'))

    def move(self):
        self.model.grid.move_to_empty(self)

    def move_to_nearby_empty(self):
        neighborhood = self.model.grid.get_neighborhood(self.pos, moore=True, radius=1)
        nearby_empty_cells = [nearby_cell for nearby_cell in neighborhood if self.model.grid.is_cell_empty(nearby_cell)]

        if nearby_empty_cells:
            self.model.grid.move_agent(self, random.choice(nearby_empty_cells))

    def step(self):
        if self.is_living:
            if self.nationalism > 500:
                self.move_to_nearby_empty()

            for behaviour in self.behaviors:
                behaviour(self, self.model).run()

    def kill(self):
        self.is_living = False

    def __repr__(self):
        return str(self.ethnicity) + " " + str(self.is_living)

class Ethnicity(object):
    def __init__(self, name, colour, native_languages, likes, hates):
        self.colour = colour
        self.native_languages = native_languages
        self.likes = likes
        self.hates = hates
        self.name = name

    def __repr__(self):
        return self.name

    def __hash__(self):
        return hash(self.name)

    def __eq__(self, other):
        return self.name == other.name


class Origins(dict):

    def __missing__(self, key):
        return 0

    def mix(self, ethnicity2):
        # Mixes two different origins and returns a crossbreed origin.
        keys = set(self.keys())
        keys.update(ethnicity2.keys())

        for key in keys:
            self[key] = (self[key] + ethnicity2[key]) / 2
        return self

    @staticmethod
    def random():
        names = RACES
        colours = COLOURS
        languages = LANGUAGES

        origins = Origins()

        # Returns a beta random rumber, closer to 1 than len(RACES). This allows a random number of different origins.
        number_of_ethnicities = int(random.betavariate(2, 3) * len(names)) + 1
        ethnicities = random.sample(names, number_of_ethnicities)

        for i, this_ethnicity in enumerate(ethnicities):
            others = names.copy()
            others.remove(this_ethnicity)

            liked_ethnicities = random.sample(others, number_of_ethnicities-1)
            hated_ethnicities = random.sample(others, number_of_ethnicities-1)

            eth = Ethnicity(this_ethnicity, colours[i], languages[i], liked_ethnicities, hated_ethnicities)

            origins[eth] = random.uniform(0, 1)

        total_weight = sum(o[1] for o in origins.items())
        for key in origins.keys():
            origins[key] /= total_weight

        return origins

