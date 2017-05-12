/*
Neal Noble
March 30th, 2016
IT328
Assignment introduction to Javascript
*/

function tvshow (title, synopsis, year, channels, cast_crew) {
    this.title          = title;
    this.synopsis       = synopsis;
    this.year           = year;
    this.channels       = channels;
    this.cast_crew      = cast_crew;
    this.totalChannels  = function() {
        return this.channels.length;
    }
}

var directors    = ["Vincent McEveety","Joseph Sargent","Joseph Pevney"];
var writers      = ["D.C. Fontana","David Gerrold","Robert Bloch"];
var producers    = ["Gene Roddenberry","Gene L. Coon","Robert H. Justman"];
var music        = ["Alexander Courage","Fred Steiner","Gerald Fried"];
var cast         = ["William Shatner", "Lenornd Nemoy","Deforest Kelley", "Nichelle Nichols","James Doohan",
                    "George Takei", "Walter Koenig","Majel Barrett"];

var synopsis = "Wagon Train to the Stars. A western and Sci-fi combined together. In 1966 Westerns were"
             + " very popular on national TV, and race to the moon was a national obsession. Star Trek"
             + " was pitched to NBC as being an action adventure Western in space. CBS had turned down the"
             + " show already in favor the Lost In Space that premiered the same year.";

Star_Trek = new tvshow("Star Trek: TOS",
                        synopsis,
                        "1966 - 1969",
                        ["NBC", "KINGTV", "KSTW", "KONGTV"],
                        [cast, directors, writers, producers, music]
);