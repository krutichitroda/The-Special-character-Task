const network = {
  users: [
    {
      userId: "U001",
      name: "Alice",
      friends: ["U002", "U003", "U004"],
      followers: 1500,
      posts: [
        { postId: "P001", likes: 150, comments: 20 },
        { postId: "P002", likes: 200, comments: 35 }
      ]
    }

    [
    {
      userId: "U002",
      name: "Bob",
      friends: ["U002", "U006", "U007"],
      followers: 17000,
      posts: [
        { postId: "P001", likes: 130, comments: 80 },
        { postId: "P002", likes: 400, comments: 45 }
      ]
    }
    ]    
  ]
};



MutualConnections = []
def findMutualFriends(userId1,userId2, network):
    if users(userId1(friends)== userId2(friends)):
        print(friends)
        MutualConnections.append(friends)
    print(MutualConnections[])
    return

score = 0 
def calculateInfluenceScore(useId , network):
    for score range in (0,100):
    users(score) =  (followers × 0.5) + (avgLikesPerPost × 0.3) + (mutualConnections × 0.2)
        if score < 100:
            print(score)
        return

maxDepth = 3
arr2 = []
def findConnectionPath(userId1, userId2, network, maxDepth):
    if mutualConnections <= maxDepth:
        print(userId)
        arr2.append(userId)
    else:
        print(" ")
    print(arr2)
return


def recommendFriends(userId, network, count):
    for userId in users:
        if userId1(mutualConnections) == userId2(mutualConnections):
            print(user)

