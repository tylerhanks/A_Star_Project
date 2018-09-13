

class Map():
    """Maps are undirected graphs whose nodes have locations and connections"""

    def __init__(self, connections_file_string, locations_file_string):
        """Set up the map created by the passed in connections and locations files"""
        
        self.connections_dictionary = {}
        self.locations_dictionary = {}

        #construct a dictionary mapping a node to its connections list
        with open(connections_file_string, 'r') as connections_file:
            for line in connections_file:
                stripped_line = line.rstrip('\n')
                split_line = stripped_line.split() 
                self.connections_dictionary[split_line[0]] = split_line[2:]
            del self.connections_dictionary["END"]

        #construct a dictionary mapping a node to its location
        with open(locations_file_string, 'r') as locations_file:
            for line in locations_file:
                stripped_line = line.rstrip('\n')
                split_line = stripped_line.split()
                self.locations_dictionary[split_line[0]] = split_line[1:]
            del self.locations_dictionary["END"]

    def print_connections(self):
        """Prints all nodes and their connections"""
        for key, value in self.connections_dictionary.items():
            print("Node: " + key + "\tConnections: %s" % value)
    
    def print_locations(self):
        """Prints all nodes and their locations"""
        for key, value in self.locations_dictionary.items():
            print("Node: " + key + "\tLocation: %s" % value)

    def print_all(self):
        """Prints all nodes' locations and connections"""
        for key, value in self.locations_dictionary.items():
            connections = self.connections_dictionary[key]
            print("Node: " + key + "\tLocation: %s" % value + "\t\tConnections: %s" % connections)

    def exclude_node(self, excluded_node):
        excluded_connections = self.connections_dictionary[excluded_node]
        del self.connections_dictionary[excluded_node]

        for node in excluded_connections:
            target_list = self.connections_dictionary[node]
            target_list.remove(excluded_node) 



def main():

    my_map = Map("connections.txt", "locations.txt")

    my_map.print_connections()

    my_map.connections_dictionary[node]

    my_map.exclude_node("A1")

    print('\n')

    my_map.print_connections()

if __name__ == "__main__":
    main()




    
