#!/usr/bin/env python
""" generated source for module MovieClip """
from __future__ import print_function
from functools import wraps
from threading import RLock

def lock_for_object(obj, locks={}):
    return locks.setdefault(id(obj), RLock())

def synchronized(call):
    assert call.__code__.co_varnames[0] in ['self', 'cls']
    @wraps(call)
    def inner(*args, **kwds):
        with lock_for_object(args[0]):
            return call(*args, **kwds)
    return inner

# 
#  * @(#)MovieClip.java   1.99.1 08/12/08
#  
#  ************************************************************************
#  * Copyright (c) 2008 by the Association for Computing Machinery        *
#  *                                                                      *
#  * The Java Task Force seeks to impose few restrictions on the use of   *
#  * these packages so that users have as much freedom as possible to     *
#  * use this software in constructive ways and can make the benefits of  *
#  * that work available to others.  In view of the legal complexities    *
#  * of software development, however, it is essential for the ACM to     *
#  * maintain its copyright to guard against attempts by others to        *
#  * claim ownership rights.  The full text of the JTF Software License   *
#  * is available at the following URL:                                   *
#  *                                                                      *
#  *          http://www.acm.org/jtf/jtf-software-license.pdf             *
#  *                                                                      *
#  ************************************************************************
#  REVISION HISTORY
# 
#  Class introduced in V1.1
# package: acm.util
#  Implementation notes 
# 
#  * This class uses QuickTime for Java, which is not available on all Java platforms.
#  * To ensure that this class can be compiled even on systems that lack the QuickTime
#  * libraries, all calls to the library are implemented through reflection.
#  
#  Class: MovieClip 
# 
#  * This class represents a video clip, which can be read from a QuickTime
#  * movie file or web-based resource.
#  
class MovieClip(Container):
    """ generated source for class MovieClip """
    #  Constructor: MovieClip(filename) 
    # 
    #  * Creates a <code>MovieClip</code> object from the specified movie file.
    #  *
    #  * @usage MovieClip movie = new MovieClip(filename);
    #  * @param filename The file from which the movie is read
    #  
    @overloaded
    def __init__(self, filename):
        """ generated source for method __init__ """
        super(MovieClip, self).__init__()
        self.__init__(filename, filename)

    #  Constructor: MovieClip(file) 
    # 
    #  * Creates a <code>MovieClip</code> object from the specified movie file.
    #  *
    #  * @usage MovieClip movie = new MovieClip(file);
    #  * @param file A <code>File</code> object from which the movie is read
    #  
    @__init__.register(object, File)
    def __init___0(self, file_):
        """ generated source for method __init___0 """
        super(MovieClip, self).__init__()
        self.__init__(file_, file_.__name__)

    #  Constructor: MovieClip(url) 
    # 
    #  * Creates a <code>MovieClip</code> object from the specified network URL.
    #  *
    #  * @usage MovieClip movie = new MovieClip(file);
    #  * @param url A network URL containing the movie
    #  
    @__init__.register(object, URL)
    def __init___1(self, url):
        """ generated source for method __init___1 """
        super(MovieClip, self).__init__()
        self.__init__(url, JTFTools.getURLSuffix(url.__str__()))

    #  Method: play() 
    # 
    #  * Starts the movie from its current position.
    #  *
    #  * @usage movie.play();
    #  
    def play(self):
        """ generated source for method play """
        setLooping(False)
        startMovie()

    #  Method: loop() 
    # 
    #  * Plays the movie in a continuous audio loop.
    #  *
    #  * @usage movie.loop();
    #  
    def loop(self):
        """ generated source for method loop """
        setLooping(True)
        startMovie()

    #  Method: stop() 
    # 
    #  * Stops the playback of the movie.
    #  *
    #  * @usage movie.stop();
    #  
    @synchronized
    def stop(self):
        """ generated source for method stop """
        stopMovie()
        setLooping(False)

    #  Method: getName() 
    # 
    #  * Returns the name of the movie, which is typically the file name from which it
    #  * was read.
    #  *
    #  * @usage String name = movie.__name__;
    #  * @return The name of the movie
    #  
    def getName(self):
        """ generated source for method getName """
        return movieName

    #  Method: setName(name) 
    # 
    #  * Sets a name to identify the movie.
    #  *
    #  * @usage movie.setName(name);
    #  * @param name The name to use for the movie
    #  
    def setName(self, name):
        """ generated source for method setName """
        movieName = name

    #  Method: getFrameCount() 
    # 
    #  * Returns the number of frames in a movie.
    #  *
    #  * @usage int nFrames = movie.getFrameCount();
    #  * @return The number of frames in a movie
    #  
    def getFrameCount(self):
        """ generated source for method getFrameCount """
        return getQTDuration()

    #  Method: getFrameRate() 
    # 
    #  * Returns the frame rate of the movie.
    #  *
    #  * @usage double frameRate = movie.getFrameRate();
    #  * @return The frame rate of the movie (in frames/second)
    #  
    def getFrameRate(self):
        """ generated source for method getFrameRate """
        return getQTTimeScale()

    #  Method: getDuration() 
    # 
    #  * Returns the duration of a movie (in seconds).
    #  *
    #  * @usage double duration = movie.getDuration();
    #  * @return The duration of a movie (in seconds)
    #  
    def getDuration(self):
        """ generated source for method getDuration """
        return self.getFrameCount() / self.getFrameRate()

    #  Method: getFrameIndex() 
    # 
    #  * Returns the current frame index in the movie.
    #  *
    #  * @usage int frameIndex = movie.getFrameIndex();
    #  * @return The current frame index in the movie
    #  
    def getFrameIndex(self):
        """ generated source for method getFrameIndex """
        return getCurrentTime()

    #  Method: setFrameIndex(frame) 
    # 
    #  * Sets the current frame index.
    #  *
    #  * @usage movie.setFrameIndex(frameIndex);
    #  * @param frameIndex The current frame index in the movie
    #  
    def setFrameIndex(self, frameIndex):
        """ generated source for method setFrameIndex """
        setCurrentTime(frameIndex)

    #  Method: rewind() 
    # 
    #  * Rewinds the movie to the beginning.  This method is useful after you have
    #  * stopped a movie and want to replay it from the beginning.
    #  *
    #  * @usage movie.rewind();
    #  
    def rewind(self):
        """ generated source for method rewind """
        self.setFrameIndex(0)

    #  Method: getVolume() 
    # 
    #  * Returns the playback volume setting for the movie, which is a number
    #  * between 0 (silent) and 1 (maximum volume).
    #  *
    #  * @usage double volume = movie.getVolume();
    #  * @return The playback volume setting for the movie
    #  
    def getVolume(self):
        """ generated source for method getVolume """
        return clipVolume

    #  Method: setVolume(volume) 
    # 
    #  * Sets the playback volume setting for the movie, which is a number
    #  * between 0 (silent) and 1 (maximum volume).
    #  *
    #  * @usage movie.setVolume(volume);
    #  * @param volume The new volume setting for the movie
    #  
    def setVolume(self, volume):
        """ generated source for method setVolume """
        clipVolume = volume
        setControllerVolume(volume)

    #  Method: getPlaybackRate() 
    # 
    #  * Returns the playback rate, which is a floating-point number indicating
    #  * the speed and direction of playback.  The value 1.0 indicates normal
    #  * speed, 2.0 indicates a movie running at double speed, and 0.5 indicates
    #  * a movie running at half speed.  Negative values indicate that the movie
    #  * should run in reverse, so that a playback rate of -1.0 specifies that the
    #  * movie should run backwards at normal speed.
    #  *
    #  * @usage double rate = movie.getPlaybackRate();
    #  * @return The playback rate for the movie
    #  
    def getPlaybackRate(self):
        """ generated source for method getPlaybackRate """
        return clipRate

    #  Method: setPlaybackRate(rate) 
    # 
    #  * Sets the playback rate for the movie.  The value 1.0 indicates normal
    #  * speed, 2.0 indicates a movie running at double speed, and 0.5 indicates
    #  * a movie running at half speed.  Negative values indicate that the movie
    #  * should run in reverse, so that a playback rate of -1.0 specifies that the
    #  * movie should run backwards at normal speed.
    #  *
    #  * @usage sound.setPlaybackRate(rate);
    #  * @param rate The new playback rate for the movie
    #  
    def setPlaybackRate(self, rate):
        """ generated source for method setPlaybackRate """
        clipRate = rate
        if not isStopped():
            setRate(rate)

    #  Method: enableController() 
    # 
    #  * Enables the QuickTime controller displayed at the bottom of the movie.  This
    #  * call has no effect if a controller is already enabled.
    #  *
    #  * @usage movie.enableController();
    #  
    def enableController(self):
        """ generated source for method enableController """
        if hasQuickTime:
            setControllerVisible(True)

    #  Method: disableController() 
    # 
    #  * Disables the QuickTime controller from the bottom of the movie, making it
    #  * disappear from the window.  This call has no effect if no controller is
    #  * already disabled.
    #  *
    #  * @usage movie.disableController();
    #  
    def disableController(self):
        """ generated source for method disableController """
        if hasQuickTime:
            setControllerVisible(False)

    #  Method: isControllerEnabled() 
    # 
    #  * Returns <code>true</code> if the QuickTime controller is enabled.
    #  *
    #  * @usage if (movie.isControllerEnabled()) . . .
    #  * @return <code>true</code> if the controller is enabled
    #  
    def isControllerEnabled(self):
        """ generated source for method isControllerEnabled """
        return controllerVisible

    #  Method: getControllerHeight() 
    # 
    #  * Returns the height of the QuickTime controller, measured in pixels.  If
    #  * no controller is installed, <code>getControllerHeight</code> returns 0.
    #  *
    #  * @usage int height = movie.getControllerHeight();
    #  * @return The height of the QuickTime controller (in pixels)
    #  
    def getControllerHeight(self):
        """ generated source for method getControllerHeight """
        return 0 if (controller == None) else CONTROLLER_HEIGHT

    # /
    #  Overridden methods                                                 
    # /
    #  Method: getPreferredSize() 
    # 
    #  * Returns the desired height of the movie panel, which is taken from the
    #  * underlying movie, taking account of the controller, if any.
    #  *
    #  * @usage Dimension size = movie.getPreferredSize();
    #  * @return The desired height of the movie panel
    #  * @noshow
    #  
    def getPreferredSize(self):
        """ generated source for method getPreferredSize """
        if movie == None:
            return DEFAULT_SIZE
        try:
            getNaturalBoundsRect = movieClass.getMethod("getNaturalBoundsRect", [None] * 0)
            getWidth = qdRectClass.getMethod("getWidth", [None] * 0)
            getHeight = qdRectClass.getMethod("getHeight", [None] * 0)
            rect = getNaturalBoundsRect.invoke(movie, [None] * 0)
            width = (int(getWidth.invoke(rect, [None] * 0))).intValue()
            height = (int(getHeight.invoke(rect, [None] * 0))).intValue()
            size = Dimension(width, height + self.getControllerHeight())
            return size
        except Exception as ex:
            raise ErrorException(ex)

    # /
    #  Private methods                                                    
    # /
    #  Private constructor: MovieClip(source, name) 
    # 
    #  * Constructs a new movie from a data source and assigns the specified name.
    #  
    @__init__.register(object, object, str)
    def __init___2(self, source, name):
        """ generated source for method __init___2 """
        super(MovieClip, self).__init__()
        startQuickTime()
        movieName = name
        clipVolume = 1.0
        clipRate = 1.0
        setLayout(BorderLayout())
        if hasQuickTime:
            try:
                readMovie(source)
            except Exception as ex:
                add(ErrorWindow(name, "Can't read movie file"), BorderLayout.CENTER)
        else:
            add(ErrorWindow(name, errorMessage), BorderLayout.CENTER)
        addComponentListener(MovieClipListener())

    #  Private method: startQuickTime() 
    # 
    #  * Opens a new QuickTime session and tests to see whether the correct version
    #  * of QuickTime exists.
    #  
    def startQuickTime(self):
        """ generated source for method startQuickTime """
        hasQuickTime = False
        try:
            movieClass = Class.forName("quicktime.std.movies.Movie")
            movieControllerClass = Class.forName("quicktime.std.movies.MovieController")
            openMovieFileClass = Class.forName("quicktime.io.OpenMovieFile")
            qdRectClass = Class.forName("quicktime.qd.QDRect")
            qtDataRefClass = Class.forName("quicktime.std.movies.media.DataRef")
            qtFactoryClass = Class.forName("quicktime.app.view.QTFactory")
            qtFileClass = Class.forName("quicktime.io.QTFile")
            qtSessionClass = Class.forName("quicktime.QTSession")
            timeRecordClass = Class.forName("quicktime.std.clocks.TimeRecord")
            isInitialized = qtSessionClass.getMethod("isInitialized", [None] * 0)
            with lock_for_object(lock):
                if isInitialized.invoke(None, [None] * 0) == Boolean.FALSE:
                    open = qtSessionClass.getMethod("open", [None] * 0)
                    open.invoke(None, [None] * 0)
            getMajorVersion = qtSessionClass.getMethod("getMajorVersion", [None] * 0)
            version = (int(getMajorVersion.invoke(None, [None] * 0))).intValue()
            if version < MIN_QUICKTIME_VERSION:
                raise ErrorException("MovieClip requires QuickTime V7 or later")
            hasQuickTime = True
        except Exception as ex:
            errorMessage = ex.getMessage()

    #  Private method: startMovie() 
    # 
    #  * Starts the movie from its current position.  This method is identical to
    #  * clicking the <code>play</code> control in the QuickTime controller.
    #  
    def startMovie(self):
        """ generated source for method startMovie """
        if not hasQuickTime or movie == None:
            return
        try:
            types = [Float.TYPE]
            args = [float(float(clipRate))]
            play = movieControllerClass.getMethod("play", types)
            self.play.invoke(controller, args)
        except Exception as ex:
            raise ErrorException(ex)

    #  Private method: stopMovie() 
    # 
    #  * Stops the movie.  This method is identical to clicking the
    #  * <code>pause</code> control in the QuickTime controller.
    #  
    def stopMovie(self):
        """ generated source for method stopMovie """
        if not hasQuickTime or movie == None:
            return
        try:
            types = [Float.TYPE]
            args = [float(0.0)]
            play = movieControllerClass.getMethod("play", types)
            self.play.invoke(controller, args)
        except Exception as ex:
            raise ErrorException(ex)

    #  Private method: setLooping(flag) 
    # 
    #  * Sets a flag to indicate whether the movie should play in a continuous
    #  * loop.
    #  
    def setLooping(self, flag):
        """ generated source for method setLooping """
        if not hasQuickTime or movie == None:
            return
        try:
            types = [Boolean.TYPE]
            args = [bool(flag)]
            setLooping = movieControllerClass.getMethod("setLooping", types)
            self.setLooping.invoke(controller, args)
        except Exception as ex:
            raise ErrorException(ex)

    #  Private method: readMovie(source) 
    # 
    #  * Reads a QuickTime movie by calling a method appropriate to the source type.
    #  * If the movie is read successfully, this code adds it to the primary container.
    #  
    def readMovie(self, source):
        """ generated source for method readMovie """
        try:
            if isinstance(source, (str, )):
                name = str(source)
                if name.startsWith("http:"):
                    try:
                        movie = readMovieFromURL(URL(name))
                    except MalformedURLException as ex:
                        raise ErrorException("MovieClip: Malformed URL")
                else:
                    movie = readMovieFromFile(File(name))
            elif isinstance(source, (File, )):
                movie = readMovieFromFile(source)
            elif isinstance(source, (URL, )):
                movie = readMovieFromURL(source)
            controller = createController()
            controllerVisible = True
            addQTComponent(controller)
        except Exception as ex:
            raise ErrorException(ex)

    #  Private method: createController() 
    # 
    #  * Creates a QuickTime controller for the current movie.
    #  
    def createController(self):
        """ generated source for method createController """
        types = [movie.__class__]
        args = [movie]
        movieControllerConstructor = movieControllerClass.getConstructor(types)
        return movieControllerConstructor.newInstance(args)

    #  Private method: addQTComponent(obj) 
    # 
    #  * Adds a component to the main container.  If the argument is a QuickTime object,
    #  * the code invokes the appropriate <code>asComponent</code> method to create a
    #  * Java component.
    #  
    def addQTComponent(self, obj):
        """ generated source for method addQTComponent """
        if not (isinstance(obj, (Component, ))):
            types = [obj.__class__]
            args = [obj]
            makeQTComponent = qtFactoryClass.getMethod("makeQTComponent", types)
            obj = makeQTComponent.invoke(None, args)
            if not (isinstance(obj, (Component, ))):
                qtClass = obj.__class__
                asComponent = qtClass.getMethod("asComponent", [None] * 0)
                obj = asComponent.invoke(obj, [None] * 0)
        removeAll()
        add(obj, BorderLayout.CENTER)

    #  Private method: readMovieFromFile(file) 
    # 
    #  * Reads a movie from a file object.
    #  
    def readMovieFromFile(self, file_):
        """ generated source for method readMovieFromFile """
        try:
            types1 = [Class.forName("java.io.File")]
            args1 = [file_]
            qtFileConstructor = qtFileClass.getConstructor(types1)
            qtFile = qtFileConstructor.newInstance(args1)
            types2 = [qtFileClass]
            args2 = [qtFile]
            asRead = openMovieFileClass.getMethod("asRead", types2)
            openMovieFile = asRead.invoke(None, args2)
            types3 = [openMovieFileClass]
            args3 = [openMovieFile]
            fromFile = movieClass.getMethod("fromFile", types3)
            return fromFile.invoke(None, args3)
        except Exception as ex:
            raise ErrorException(ex)

    #  Private method: readMovieFromURL(href) 
    # 
    #  * Reads a movie from the specified URL.
    #  
    def readMovieFromURL(self, url):
        """ generated source for method readMovieFromURL """
        try:
            types1 = [Class.forName("java.lang.String")]
            args1 = [url.__str__()]
            qtDataRefConstructor = qtDataRefClass.getConstructor(types1)
            qtFile = qtDataRefConstructor.newInstance(args1)
            types2 = [qtDataRefClass, Integer.TYPE]
            args2 = [qtFile, int(0)]
            fromDataRef = movieClass.getMethod("fromDataRef", types2)
            return fromDataRef.invoke(None, args2)
        except Exception as ex:
            raise ErrorException(ex)

    #  Private method: setControllerVisible(flag) 
    # 
    #  * Sets whether the controller is visible.
    #  
    def setControllerVisible(self, flag):
        """ generated source for method setControllerVisible """
        if not hasQuickTime or movie == None:
            return
        if flag != controllerVisible:
            try:
                types = [Boolean.TYPE]
                args = [bool(flag)]
                setVisible = movieControllerClass.getMethod("setVisible", types)
                setVisible.invoke(controller, args)
            except Exception as ex:
                raise ErrorException(ex)
            controllerVisible = flag

    #  Private method: getCurrentTime() 
    # 
    #  * Returns the movie time as maintained by the controller.
    #  
    def getCurrentTime(self):
        """ generated source for method getCurrentTime """
        if not hasQuickTime or movie == None:
            return 0
        try:
            getCurrentTime = movieControllerClass.getMethod("getCurrentTime", [None] * 0)
            return (int(self.getCurrentTime.invoke(controller, [None] * 0))).intValue()
        except Exception as ex:
            raise ErrorException(ex)

    #  Private method: setCurrentTime(time) 
    # 
    #  * Sets the movie time.  As with the other <code>set</code> operations, this
    #  * code makes the changes in the controller to ensure that its controls are
    #  * updated.
    #  
    def setCurrentTime(self, time):
        """ generated source for method setCurrentTime """
        if not hasQuickTime or movie == None:
            return
        try:
            types = [timeRecordClass]
            args = [createTimeRecord(time)]
            goToTime = movieControllerClass.getMethod("goToTime", types)
            goToTime.invoke(controller, args)
        except Exception as ex:
            raise ErrorException(ex)

    #  Private method: setControllerVolume(volume) 
    # 
    #  * Sets the controller volume.
    #  
    def setControllerVolume(self, volume):
        """ generated source for method setControllerVolume """
        if not hasQuickTime or movie == None:
            return
        try:
            types = [Float.TYPE]
            args = [float(float(volume))]
            setVolume = movieControllerClass.getMethod("setVolume", types)
            self.setVolume.invoke(controller, args)
        except Exception as ex:
            raise ErrorException(ex)

    #  Private method: setRate(rate) 
    # 
    #  * Sets the movie playback rate.
    #  
    def setRate(self, volume):
        """ generated source for method setRate """
        if not hasQuickTime or movie == None:
            return
        try:
            types = [Float.TYPE]
            args = [float(float(volume))]
            setRate = movieClass.getMethod("setRate", types)
            self.setRate.invoke(movie, args)
        except Exception as ex:
            raise ErrorException(ex)

    #  Private method: isStopped() 
    # 
    #  * Returns whether the controller is currently stopped.
    #  
    def isStopped(self):
        """ generated source for method isStopped """
        if not hasQuickTime or movie == None:
            return True
        try:
            getPlayRate = movieControllerClass.getMethod("getPlayRate", [None] * 0)
            return (float(getPlayRate.invoke(controller, [None] * 0))).floatValue() == 0.0
        except Exception as ex:
            raise ErrorException(ex)

    #  Private method: getQTDuration() 
    # 
    #  * Returns the duration in movie time units.
    #  
    def getQTDuration(self):
        """ generated source for method getQTDuration """
        if not hasQuickTime or movie == None:
            return 0
        try:
            getDuration = movieClass.getMethod("getDuration", [None] * 0)
            return (int(self.getDuration.invoke(movie, [None] * 0))).intValue()
        except Exception as ex:
            raise ErrorException(ex)

    #  Private method: getQTTimeScale() 
    # 
    #  * Returns the movie time in units per second.
    #  
    def getQTTimeScale(self):
        """ generated source for method getQTTimeScale """
        if not hasQuickTime or movie == None:
            return DEFAULT_TIME_SCALE
        try:
            getTimeScale = movieClass.getMethod("getTimeScale", [None] * 0)
            return (int(getTimeScale.invoke(movie, [None] * 0))).intValue()
        except Exception as ex:
            raise ErrorException(ex)

    #  Private method: createTimeRecord() 
    # 
    #  * Creates a <code>TimeRecord</code> object, which is required in the call
    #  * to <code>goToTime</code>.
    #  
    def createTimeRecord(self, time):
        """ generated source for method createTimeRecord """
        try:
            types = [Integer.TYPE, Long.TYPE]
            args = [int(self.getQTTimeScale()), long(time)]
            newTimeRecord = timeRecordClass.getConstructor(types)
            return newTimeRecord.newInstance(args)
        except Exception as ex:
            raise ErrorException(ex)

    #  Private constants 
    MIN_QUICKTIME_VERSION = 7
    CONTROLLER_HEIGHT = 16
    DEFAULT_TIME_SCALE = 600
    DEFAULT_SIZE = Dimension(300, 200)

    #  Private instance variables 
    movieClass = None
    movieControllerClass = None
    openMovieFileClass = None
    qdRectClass = None
    qtDataRefClass = None
    qtFactoryClass = None
    qtFileClass = None
    qtSessionClass = None
    timeRecordClass = None
    controller = None
    movie = None
    movieName = None
    errorMessage = None
    version = int()
    hasQuickTime = bool()
    controllerVisible = bool()
    clipVolume = float()
    clipRate = float()

    #  Private class variables 
    lock = object()

#  Package class: MovieClipListener 
# 
#  * This class encapsulates the listeners for the movie clip.
#  
class MovieClipListener(ComponentListener):
    """ generated source for class MovieClipListener """
    def componentResized(self, e):
        """ generated source for method componentResized """
        (e.getSource()).validate()

    def componentHidden(self, e):
        """ generated source for method componentHidden """

    def componentMoved(self, e):
        """ generated source for method componentMoved """

    def componentShown(self, e):
        """ generated source for method componentShown """

#  Package class: ErrorWindow 
# 
#  * This class is displayed in the movie container if QuickTime does not exist
#  * on the system or the movie can't be found.
#  
class ErrorWindow(Component):
    """ generated source for class ErrorWindow """
    #  Constructor: ErrorWindow 
    # 
    #  * Constructs an error window, passing in the movie name and the error message string.
    #  
    def __init__(self, name, msg):
        """ generated source for method __init__ """
        super(ErrorWindow, self).__init__()
        movieName = name
        errorMessage = msg

    #  Overridden method: paint 
    # 
    #  * Paints the name of the movie and the error message.
    #  
    def paint(self, g):
        """ generated source for method paint """
        size = getSize()
        fm = g.getFontMetrics()
        g.setColor(Color.WHITE)
        g.fillRect(0, 0, size.width, size.height)
        g.setColor(Color.BLACK)
        x = (size.width - fm.stringWidth(movieName)) / 2
        y = size.height / 2 - fm.getHeight()
        g.drawString(movieName, x, y)
        g.setColor(Color.RED)
        x = (size.width - fm.stringWidth(errorMessage)) / 2
        y += 2 * fm.getHeight()
        g.drawString(errorMessage, x, y)

    #  Private instance variables 
    movieName = None
    errorMessage = None

