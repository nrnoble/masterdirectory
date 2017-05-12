import { Meteor } from 'meteor/meteor';
import{ mongo } from  "meteor/mongo";
import { bookmarksCollection } from '../collections/collections.js';
import { bookmarksDummyData } from '../collections/collections.js';


//import { bookmarksCollection } from 'server/collections.js';
//import { bookmarksDummyData } from 'server/collections.js';


Meteor.startup(() => {
  // remove any database values that are present
  //   bookmarksCollection.remove({}); // works only on serverside
  //
  //   // add dummy data
  //   for (var i = 0; i < bookmarksDummyData.length; i++)
  //   {
  //       bookmarksCollection.insert(bookmarksDummyData[i]);
  //   }
});


