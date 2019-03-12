# Navigation System


In this project, we've developed a custom navigation app that will help guide visitors to a St Louis
Zoo. 

There are 20 animal attractions (such as Snow Leopard, Zebra or Lion) in the zoo, 53 roads
and a main entrance/exit, that is, 21 nodes and 53 edges. We categorize all the attractions into 8
animal species, such as primate, big cat, reptile and so on. For edges, we categorize into 2 types.
One is accessible for all including disabled people (ADA), the other is only for non-disable people,
such as rocks walk, stairs, or paved walk. In addition, we have 3 uni-direction edges, speicifically,
from Penguin to Bee & Butterfly Entry, from Bee & Butterfly Entry to Bee & Butterfly Exit, and
from Bee & Butterfly Exit to Andean Bear. The rest edges are all bi-directional. Hence, for each
edge, we not only assign a street name but also the direction such as south, west, northeast and so
on, which helps to guide visitors more conveniently. Here we've attached the zoo map, showing all the attractions and streets in St Louis zoo.


Before the navigation system runs, we alphabetically list all the attractions. It allows users to enter
their starting point and the next attraction they want to visit. It also allows users to choose whether
they require a handicapped-accessible route. Then it  will calculate a shortest path and print clear
direction navigation instructions with total distance. It also allow the user to quit or enter another
navigation query, which defaults to starting at the last end point.