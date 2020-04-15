import random
from collections import deque
from itertools import combinations

class User:
    def __init__(self, name):
        self.name = name

class SocialGraph:
    def __init__(self):
        self.last_id = 0
        self.users = {}
        self.friendships = {}

    def add_friendship(self, user_id, friend_id):
        """
        Creates a bi-directional friendship
        """
        if user_id == friend_id:
            print("WARNING: You cannot be friends with yourself")
        elif friend_id in self.friendships[user_id] or user_id in self.friendships[friend_id]:
            print("WARNING: Friendship already exists")
        else:
            self.friendships[user_id].add(friend_id)
            self.friendships[friend_id].add(user_id)

    def add_user(self, name):
        """
        Create a new user with a sequential integer ID
        """
        self.last_id += 1  # automatically increment the ID to assign the new user
        self.users[self.last_id] = User(name)
        self.friendships[self.last_id] = set()

    def populate_graph(self, num_users, avg_friendships):
        """
        Takes a number of users and an average number of friendships
        as arguments

        Creates that number of users and a randomly distributed friendships
        between those users.

        The number of users must be greater than the average number of friendships.
        """
        # Reset graph
        self.last_id = 0
        self.users = {}
        self.friendships = {}

        # Add users
        for i in range(num_users):
            self.add_user(f"User {i+1}")

        # Create friendships
        # plan:
        # create a list with all possible friendship combos
        # shuffle the list, then get the first n elements

        #### O(n^2)
        # possible_friendships = []
        # for user_id in self.users:
        #     for friend_id in range(user_id + 1, self.last_id + 1):
        #         possible_friendships.append((user_id, friend_id))

        #### O(nCk) or O(n choose k). k=2 in this case. ppl usually call k "r",
        # because the default param name is called "r" --> itertools.combinations(iterable, r)
        possible_friendships = list(combinations(self.users, 2))

        random.shuffle(possible_friendships)

        # Create n friendships where n = avg_frindships * num_users // 2
        # avg_frindships = total_friendships / num_users
        # total_frindships = avg_friendships * num_users
        for i in range(num_users * avg_friendships // 2):
            f1, f2 = possible_friendships[i]
            self.add_friendship(f1, f2)


    def get_all_social_paths(self, user_id):
        """
        Takes a user's user_id as an argument

        Returns a dictionary containing every user in that user's
        extended network with the shortest friendship path between them.

        The key is the friend's ID and the value is the path.
        """
        visited = {}  # Note that this is a dictionary, not a set
        # do a bfs
        # add each path to visited as value, and each last fren in path as key
        q = deque([[user_id]])
        while len(q)>0:
            path = q.pop()
            v = path[-1]
            if v not in visited:
                visited[v] = path
                for n in self.friendships[v]:
                    q.appendleft(path + [n])
        return visited


if __name__ == '__main__':
    sg = SocialGraph()
    sg.populate_graph(10, 2)
    print(sg.friendships)
    connections = sg.get_all_social_paths(1)
    print(connections)

# 3. Questions
# To create 100 users with an average of 10 friends each, 
# how many times would you need to call add_friendship()? Why?
# ANSWER: 50, bc 2 users per friendship

# If you create 1000 users with an average of 5 random friends each, 
# what percentage of other users will be in a particular user's extended social network? 
# What is the average degree of separation between a user and those in his/her extended network?

# 4. Stretch Goal
# You might have found the results from question #2 above to be surprising. 
# Would you expect results like this in real life? 
# If not, what are some ways you could improve your friendship 
# distribution model for more realistic results?

# If you followed the hints for part 1, your populate_graph() will run in O(n^2) time. 
# Refactor your code to run in O(n) time. 
# Are there any tradeoffs that come with this implementation?
