import { Template } from 'meteor/templating';
import { ReactiveVar } from 'meteor/reactive-var';
import { bookmarksCollection } from '../collections/collections.js';
import { foo12 } from '../collections/collections.js';

import './main.html';

Template.bookmarks.helpers({
  bookmarksList: function() {
      // retreive all bookmarks from collections
      return bookmarksCollection.find()
  }
})


Template.foo.helpers({
  myFoo: function() {
      
      return foo12;
  }
})


