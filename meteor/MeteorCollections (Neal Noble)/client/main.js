import { Template } from 'meteor/templating';
import { ReactiveVar } from 'meteor/reactive-var';
import { bookmarksCollection } from '../collections/collections.js';
//import { foo12 } from '../collections/collections.js';
import './main.html';

Template.bookmarks.helpers({
  bookmarksList: function() {
      // retreive all bookmarks from collections
      return bookmarksCollection.find();
  }
});

Template.addBookmarkForm.events({
    'submit .addBookmarkForm': function(event){
        event.preventDefault(); //stop the form from posting back to the same page

        // get form values
        var name = $('#bookmarkName').val();
        var url = $('#bookmarkUrl').val();

        // insert a new document into collection
        bookmarksCollection.insert({
            "name": name,
            "url": url,
            "lastVisited": new Date()
        });
    }
})

Template.bookmarksHeading.events({
    'click button': function(event){
        if (confirm("Really delete all bookmarks?")){
            //bookmarksCollection.remove({})

            bookmarksCollection.find().forEach(function(bookmark){
                bookmarksCollection.remove({"_id": bookmark._id});
            })
        }
    }
})






