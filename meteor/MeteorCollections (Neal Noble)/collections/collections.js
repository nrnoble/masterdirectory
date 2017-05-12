import{ mongo } from  "meteor/mongo";

//export access to my collections
export  const bookmarksCollection = new Mongo.Collection("bookmarks");

export var foo12 = "foo_12";

// export acess to any data to start our application
export  const bookmarksDummyData = [
    {
        "name": "New York Times",
        "url": "http://www.nytimes.com",
        "lastVisited": new Date (2015,10,21)
    },

    {
        "name": "imdb",
        "url": "http://imdb.com",
        "lastVisited": new Date (2016,1,24)
    },

    {
        "name": "battle.net",
        "url": "battle.net",
        "lastVisited": new Date (2016,5,5)
    }


];
