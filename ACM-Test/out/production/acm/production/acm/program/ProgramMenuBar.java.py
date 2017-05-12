#!/usr/bin/env python
""" generated source for module ProgramMenuBar """
from __future__ import print_function
# 
#  * @(#)ProgramMenuBar.java   1.99.1 08/12/08
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
#  -- V2.0 --
#  Feature enhancement 2-Mar-07 (ESR)
#    1. Added menu options to implement the "Export Applet" and
#       "Submit Project" items.
# 
#  Feature enhancement 21-May-08 (ESR)
#    1. Significant redesign of package to support easier extensions.
#    2. Added program argument to the constructor.
# package: acm.program
#  Class: ProgramMenuBar 
# 
#  * This class standardizes the menu bars used in the ACM program package.
#  * The fundamental principles behind the design of this package are:
#  *
#  * <p><ol>
#  * <li>The most common menu operations (including, for example, the standard
#  *     editing operations <b>cut</b>, <b>copy</b>, and <b>paste</b>) should
#  *     always be available and require no action on the part of the programmer.
#  * <p>
#  * <li>It should be easy to extend the menu bar without interfering with the
#  *     standard operations.
#  * <p>
#  * <li>Menu bars should work in a familiar way on each of the major platforms.
#  *     In particular, Macintosh users expect there to be a single menu bar
#  *     at the top of the screen rather than a menu bar in each window.
#  * </ol>
#  *
#  * <p>These goals turn out to be difficult to achieve simultaneously.  In
#  * particular, supporting both Macintosh-style and Windows-style menu bars
#  * requires creating a parallel <code>MenuBar</code> structure behind the
#  * underlying <code>JMenuBar</code>, which accounts for much of the complexity
#  * in this implementation.
#  *
#  * <p><b>Using the <code>ProgramMenuBar</code> class</b>
#  *
#  * The <code>ProgramMenuBar</code> class supports two distinct disciplines
#  * for listening for menu actions:
#  *
#  * <p><ul>
#  * <li><b>Focused items</b> correspond to actions that are relevant only to the
#  * component with the keyboard focus (such as <b>Cut</b>, <b>Copy</b>, and
#  * <b>Paste</b>).  Clients create focused items by calling
#  * <a href="#createFocusedItem(String)"><code>createFocusedItem</code></a>.
#  * Activating a focused item passes an action event to the listener set by calling
#  * <a href="#setFocusedListener(ActionListener)"><code>setFocusedListener</code></a>,
#  * which should be called whenever a component interested in responding to menu
#  * actions gains the keyboard focus.
#  * <p>
#  * <li><b>Program items</b> correspond to actions that are relevant throughout
#  * the lifetime of the program (such as <b>Quit</b> and <b>Print</b>).
#  * Clients create program items by calling
#  * <a href="#createProgramItem(String)"><code>createProgramItem</code></a>.
#  * Activating a program item passes an action event to the <code>menuAction</code>
#  * method in the <code>Program</code> object that created the menu bar.
#  * </ul>
#  
class ProgramMenuBar(JMenuBar, Iterable, JMenuItem):
    """ generated source for class ProgramMenuBar """
    #  Constant: SHIFT 
    # 
    #  * Constant indicating that an accelerator key requires the SHIFT modifier.
    #  
    SHIFT = 0x20000

    #  Constructor: ProgramMenuBar(program) 
    # 
    #  * Creates an empty <code>ProgramMenuBar</code>.
    #  *
    #  * @usage ProgramMenuBar mbar = new ProgramMenuBar(owner);
    #  * @param owner The <code>Program</code> that owns this menu bar.
    #  
    def __init__(self, owner):
        """ generated source for method __init__ """
        super(ProgramMenuBar, self).__init__()
        program = owner
        menuBarListener = ProgramMenuBarListener(self)
        focusedListener = None
        accelerators = HashMap()
        focusedItems = HashSet()
        macMenuBarFlag = True
        addMenus()

    #  Method: getProgram() 
    # 
    #  * Returns the <code>Program</code> object associated with this menu.
    #  *
    #  * @usage Program program = mbar.getProgram();
    #  * @return The program associated with this menu bar
    #  
    def getProgram(self):
        """ generated source for method getProgram """
        return program

    #  Method: createStandardItem(action) 
    # 
    #  * Creates one of the standard menu items implemented by the
    #  * <code>ProgramMenuBar</code> class.   The menu item is identified
    #  * by its action command.
    #  *
    #  * @usage JMenuItem item = mbar.createStandardItem(action);
    #  * @param action The action command identifying the menu item to be created
    #  
    def createStandardItem(self, action):
        """ generated source for method createStandardItem """
        item = None
        if action == "Quit":
            item = createProgramItem(action)
            if Platform.isMac():
                setAccelerator(item, 'Q')
            else:
                item.setName("Exit")
        elif action == "Cut":
            item = createFocusedItem(action, 'X')
            if not Platform.isMac():
                item.setName("Cut (x)")
        elif action == "Copy":
            item = createFocusedItem(action, 'C')
            if not Platform.isMac():
                item.setName("Copy (c)")
        elif action == "Paste":
            item = createFocusedItem(action, 'V')
            if not Platform.isMac():
                item.setName("Paste (v)")
        elif action == "Select All":
            item = createFocusedItem(action, 'A')
        elif action == "Save":
            item = createFocusedItem(action, 'S')
        elif action == "Save As":
            item = createFocusedItem(action)
        elif action == "Print":
            item = createProgramItem(action, 'P')
            item.setName("Print...")
        elif action == "Print Console":
            item = createProgramItem(action)
        elif action == "Script":
            item = createProgramItem(action)
            item.setName("Script...")
        elif action == "Export Applet":
            item = createProgramItem(action)
            item.setName("Export Applet...")
        elif action == "Submit Project":
            item = createProgramItem(action)
            item.setName("Submit Project...")
        else:
            raise ErrorException("Illegal standard menu item: " + action)
        return item

    #  Method: createProgramItem(action) 
    # 
    #  * Creates a program menu item with the specified action command.  The
    #  * initial item has the same label as the action command, but clients
    #  * can change this name by calling <code>setName</code> on the item.
    #  *
    #  * @usage JMenuItem item = createProgramItem(action);
    #  * @param action The action command generated by this menu item
    #  
    @overloaded
    def createProgramItem(self, action):
        """ generated source for method createProgramItem """
        item = JMenuItem(action)
        item.setActionCommand(action)
        item.addActionListener(menuBarListener)
        return item

    #  Method: createProgramItem(action, key) 
    # 
    #  * Creates a program menu item with the specified action command and accelerator key.
    #  *
    #  * @usage JMenuItem item = createProgramItem(action, key);
    #  * @param action The action command generated by this menu item
    #  * @param key The integer value of the keystroke accelerator
    #  
    @createProgramItem.register(object, str, int)
    def createProgramItem_0(self, action, key):
        """ generated source for method createProgramItem_0 """
        item = self.createProgramItem(action)
        setAccelerator(item, key)
        return item

    #  Method: createFocusedItem(action) 
    # 
    #  * Creates a focused menu item with the specified action command.
    #  *
    #  * @usage JMenuItem item = createFocusedItem(action);
    #  * @param action The action command generated by this menu item
    #  
    @overloaded
    def createFocusedItem(self, action):
        """ generated source for method createFocusedItem """
        item = self.createProgramItem(action)
        focusedItems.add(item)
        return item

    #  Method: createFocusedItem(action, key) 
    # 
    #  * Creates a focused menu item with the specified action command and accelerator key.
    #  *
    #  * @usage JMenuItem item = createFocusedItem(action, key);
    #  * @param action The action command generated by this menu item
    #  * @param key The integer value of the keystroke accelerator
    #  
    @createFocusedItem.register(object, str, int)
    def createFocusedItem_0(self, action, key):
        """ generated source for method createFocusedItem_0 """
        item = self.createFocusedItem(action)
        setAccelerator(item, key)
        return item

    #  Method: isFocusedItem(item) 
    # 
    #  * Returns <code>true</code> if the item is a focused item.
    #  *
    #  * @usage if (mbar.isFocusedItem(item)) . . .
    #  * @param item A menu item installed in the menu bar
    #  * @return <code>true</code> if the item is a program item
    #  
    def isFocusedItem(self, item):
        """ generated source for method isFocusedItem """
        return focusedItems.contains(item)

    #  Method: setAccelerator(item, key) 
    # 
    #  * Sets the accelerator for the item as appropriate to the operating system
    #  * conventions.
    #  *
    #  * @usage mbar.setAccelerator(item, key);
    #  * @param item The menu item triggered by this accelerator
    #  * @param key The integer value of the keystroke accelerator
    #  
    def setAccelerator(self, item, key):
        """ generated source for method setAccelerator """
        mask = KeyEvent.META_MASK if (Platform.isMac()) else KeyEvent.CTRL_MASK
        if key > 0x10000:
            key -= self.SHIFT
            mask |= KeyEvent.SHIFT_MASK
        stroke = KeyStroke.getKeyStroke(str(key), mask)
        accelerators.put(stroke, item)
        if Platform.isMac():
            item.setAccelerator(stroke)
        else:
            item.setMnemonic(key)

    #  Method: setEnabled(action, flag) 
    # 
    #  * Enables or disables any menu items that generate the specified action command.
    #  *
    #  * @usage mbar.setEnabled(action, flag);
    #  * @param action The action command triggered by the menu item
    #  * @param flag <code>true</code> to enable the item, <code>false</code> to disable it
    #  
    @overloaded
    def setEnabled(self, action, flag):
        """ generated source for method setEnabled """
        nMenus = getMenuCount()
        i = 0
        while i < nMenus:
            self.setEnabled(getMenu(i), action, flag)
            i += 1

    #  Method: install(comp) 
    # 
    #  * Installs the menu bar in the <code>JFrame</code> or <code>Program</code>
    #  * object enclosing the component <code>comp</code>.
    #  *
    #  * @usage mbar.install(comp);
    #  * @param comp A descendant of the frame in which the menu is to be installed
    #  
    def install(self, comp):
        """ generated source for method install """
        contentPane = program.getContentPane()
        while comp != None and not (isinstance(comp, (JFrame, ))):
            comp = comp.getParent()
            if comp == contentPane and program.isAppletMode():
                if not Platform.isMac() or not macMenuBarFlag:
                    program.setJMenuBar(self)
                return
        if comp == None:
            return
        frame_ = comp
        if Platform.isMac() and macMenuBarFlag:
            if oldStyleMenuBar == None:
                oldStyleMenuBar = createOldStyleMenuBar()
            frame_.setMenuBar(oldStyleMenuBar)
        else:
            frame_.setJMenuBar(self)
            frame_.validate()

    #  Method: setMacMenuBarFlag(flag) 
    # 
    #  * Sets a flag indicating whether applications running on the Macintosh
    #  * should use standard Mac menus.  The default is <code>true</code>.
    #  * Setting this value to <code>false</code> means that Mac programs
    #  * use the same in-window <code>JMenuBar</code> approach used on other
    #  * platforms.
    #  *
    #  * @usage setMacMenuBarFlag(flag);
    #  * @param flag <code>true</code> to use Mac menu style; <code>false</code> otherwise
    #  
    def setMacMenuBarFlag(self, flag):
        """ generated source for method setMacMenuBarFlag """
        macMenuBarFlag = flag

    #  Method: getMacMenuBarFlag() 
    # 
    #  * Retrieves the setting of the Mac menu bar flag.
    #  *
    #  * @usage boolean flag = getMacMenuBarFlag();
    #  * @return <code>true</code> if Mac menu style is supported; <code>false</code> otherwise
    #  
    def getMacMenuBarFlag(self):
        """ generated source for method getMacMenuBarFlag """
        return macMenuBarFlag

    #  Method: fireActionListeners(e) 
    # 
    #  * Fires the action listeners responsible for handling the specified event.
    #  * The process of choosing the appropriate handlers takes into account
    #  * whether the action command is designated as program or focused.
    #  
    def fireActionListeners(self, e):
        """ generated source for method fireActionListeners """
        if focusedListener != None and focusedItems.contains(e.getSource()):
            focusedListener.actionPerformed(e)
        else:
            program.menuAction(e)

    #  Method: fireAccelerator(e) 
    # 
    #  * Triggers the accelerator associated with the keystroke implied by the key event.
    #  * This method returns <code>true</code> if such an accelerator exists.
    #  
    def fireAccelerator(self, e):
        """ generated source for method fireAccelerator """
        stroke = KeyStroke.getKeyStrokeForEvent(e)
        item = accelerators.get(stroke)
        if item != None:
            item.doClick(0)
            return True
        return False

    #  Method: setFocusedListener(listener) 
    # 
    #  * Registers a listener that responds while the caller holds the keyboard
    #  * focus.  The caller should register its listener when it acquires the
    #  * keyboard focus and set it to <code>null</code> when it loses it.
    #  *
    #  * @usage setFocusedListener(listener);
    #  * @param listener An <code>ActionListener</code> that responds to focused items
    #  
    def setFocusedListener(self, listener):
        """ generated source for method setFocusedListener """
        focusedListener = listener

    #  Method: iterator() 
    # 
    #  * Returns an iterator that enumerates the individual menu items under the
    #  * control of the menu bar.
    #  *
    #  * @usage Iterator<JMenuItem> iterator = mbar.iterator();
    #  * return An iterator that enumerates the menu items
    #  
    def iterator(self):
        """ generated source for method iterator """
        itemList = ArrayList()
        i = 0
        while i < getMenuCount():
            addItemToList(itemList, getMenu(i))
            i += 1
        return itemList.iterator()

    #  Protected methods 
    #  Protected method: addMenus() 
    # 
    #  * Adds menus to the menu bar.  Subclasses that wish to change the composition
    #  * of the menu bar beyond the default <code>File</code> and <code>Edit</code>
    #  * menus should override this method with one that adds the desired menus.
    #  
    def addMenus(self):
        """ generated source for method addMenus """
        addFileMenu()
        addEditMenu()

    #  Protected method: addFileMenu() 
    # 
    #  * Installs the <code>File</code> menu.
    #  *
    #  * @usage mbar.addFileMenu();
    #  
    def addFileMenu(self):
        """ generated source for method addFileMenu """
        fileMenu = JMenu("File")
        fileMenu.setMnemonic('F')
        addFileMenuItems(fileMenu)
        add(fileMenu)

    #  Protected method: addEditMenu() 
    # 
    #  * Installs the <code>Edit</code> menu.
    #  *
    #  * @usage mbar.addEditMenu();
    #  
    def addEditMenu(self):
        """ generated source for method addEditMenu """
        editMenu = JMenu("Edit")
        editMenu.setMnemonic('E')
        addEditMenuItems(editMenu)
        add(editMenu)

    #  Protected method: addFileMenuItems(menu) 
    # 
    #  * Adds the standard <code>File</code> items to the specified menu.  Subclasses
    #  * can override this method to change the list of items.
    #  *
    #  * @usage mbar.addFileMenuItems(menu);
    #  * @param menu The menu to which the <code>File</code> items are added
    #  
    def addFileMenuItems(self, menu):
        """ generated source for method addFileMenuItems """
        menu.add(self.createStandardItem("Save"))
        menu.add(self.createStandardItem("Save As"))
        menu.addSeparator()
        menu.add(self.createStandardItem("Print"))
        menu.add(self.createStandardItem("Print Console"))
        menu.add(self.createStandardItem("Script"))
        menu.addSeparator()
        menu.add(self.createStandardItem("Export Applet"))
        menu.add(self.createStandardItem("Submit Project"))
        menu.addSeparator()
        menu.add(self.createStandardItem("Quit"))

    #  Protected method: addEditMenuItems(menu) 
    # 
    #  * Adds the standard <code>Edit</code> items to the specified menu.  Subclasses
    #  * can override this method to change the list of items.
    #  *
    #  * @usage mbar.addEditMenuItems(menu);
    #  * @param menu The menu to which the <code>Edit</code> items are added
    #  
    def addEditMenuItems(self, menu):
        """ generated source for method addEditMenuItems """
        menu.add(self.createStandardItem("Cut"))
        menu.add(self.createStandardItem("Copy"))
        menu.add(self.createStandardItem("Paste"))
        menu.add(self.createStandardItem("Select All"))

    #  Private method: addItemToList(itemList, item) 
    # 
    #  * Adds the specified menu item to the list.  If <code>item</code> is itself
    #  * a menu, this method expands the item recursively.
    #  *
    #  * @usage mbar.addItemToList(itemList, item);
    #  * @param itemList The <code>ArrayList</code> to which items are added
    #  * @param item The item to be added
    #  
    def addItemToList(self, itemList, item):
        """ generated source for method addItemToList """
        if item == None:
            return
        if isinstance(item, (JMenu, )):
            menu = item
            i = 0
            while i < menu.getItemCount():
                self.addItemToList(itemList, menu.getItem(i))
                i += 1
        else:
            itemList.add(item)

    #  Private method: createOldStyleMenuBar 
    # 
    #  * Creates a <code>MenuBar</code> that has the same effect as the
    #  * specified <code>JMenuBar</code>.
    #  *
    #  * @usage MenuBar oldMenuBar = mbar.createOldStyleMenuBar();
    #  * @return A <code>MenuBar</code> whose actions are paired with the original
    #  
    def createOldStyleMenuBar(self):
        """ generated source for method createOldStyleMenuBar """
        mbar = MenuBar()
        nMenus = getMenuCount()
        i = 0
        while i < nMenus:
            mbar.add(createOldStyleMenu(getMenu(i)))
            i += 1
        return mbar

    #  Private method: createOldStyleMenu 
    # 
    #  * Creates a <code>Menu</code> that has the same effect as the
    #  * specified <code>JMenu</code>.
    #  
    def createOldStyleMenu(self, jmenu):
        """ generated source for method createOldStyleMenu """
        menu = Menu(jmenu.getText())
        nItems = jmenu.getItemCount()
        i = 0
        while i < nItems:
            menu.add(createOldStyleMenuItem(jmenu.getItem(i)))
            i += 1
        return menu

    #  Private method: createOldStyleMenuItem 
    # 
    #  * Creates a <code>MenuItem</code> that has the same effect as the
    #  * specified <code>JMenuItem</code>.
    #  
    def createOldStyleMenuItem(self, jitem):
        """ generated source for method createOldStyleMenuItem """
        if jitem == None:
            return MenuItem("-")
        elif isinstance(jitem, (JMenu, )):
            return self.createOldStyleMenu(jitem)
        elif isinstance(jitem, (JCheckBoxMenuItem, )):
            return OldStyleCheckBoxMenuItem(jitem)
        elif isinstance(jitem, (JMenuItem, )):
            return OldStyleMenuItem(jitem)
        raise ErrorException("Unsupported menu item type")

    #  Private method: setEnabled(menu, action, flag) 
    # 
    #  * Updates the enabled state of everything in the menu that has the specified action.
    #  
    @setEnabled.register(object, JMenu, str, bool)
    def setEnabled_0(self, item, action, flag):
        """ generated source for method setEnabled_0 """
        menu = item
        nItems = menu.getItemCount()
        i = 0
        while i < nItems:
            subItem = menu.getItem(i)
            if subItem != None:
                self.setEnabled(subItem, action, flag)
            i += 1

    #  Private method: setEnabled(item, action, flag) 
    # 
    #  * Updates the enabled state of the menu item if it has the specified action.
    #  
    @setEnabled.register(object, JMenuItem, str, bool)
    def setEnabled_1(self, item, action, flag):
        """ generated source for method setEnabled_1 """
        if action == item.getActionCommand():
            item.setEnabled(flag)

    #  Private instance variables 
    program = None
    menuBarListener = None
    focusedListener = None
    accelerators = None
    focusedItems = None
    oldStyleMenuBar = None
    macMenuBarFlag = bool()

#  Package class: ProgramMenuBarListener 
# 
#  * This class implements the listener for the standard menu items that
#  * forwards their action back to the program.
#  
class ProgramMenuBarListener(ActionListener):
    """ generated source for class ProgramMenuBarListener """
    #  Constructor: ProgramMenuBarListener(mbar) 
    # 
    #  * Creates a new listener for the standard menu items that will be added to this
    #  * menu bar.
    #  
    def __init__(self, mbar):
        """ generated source for method __init__ """
        super(ProgramMenuBarListener, self).__init__()
        menuBar = mbar

    #  Method: actionPerformed(e) 
    # 
    #  * Responds to an action event in the corresponding menu.   The effect of an
    #  * action event is to forward the action command back to the program.
    #  
    def actionPerformed(self, e):
        """ generated source for method actionPerformed """
        menuBar.fireActionListeners(e)

    #  Private instance variables 
    menuBar = None

#  Package class: OldStyleMenuItem 
# 
#  * This class represents a standard Macintosh <code>MenuItem</code> that listens to
#  * a <code>JMenuItem</code> and tracks its changes.
#  
class OldStyleMenuItem(MenuItem, ActionListener, ChangeListener):
    """ generated source for class OldStyleMenuItem """
    #  Constructor: OldStyleMenuItem(jitem) 
    # 
    #  * Creates a new <code>MenuItem</code> that tracks the changes in the specified
    #  * <code>JMenuItem</code>.
    #  
    def __init__(self, jitem):
        """ generated source for method __init__ """
        super(OldStyleMenuItem, self).__init__(jitem.getText())
        twin = jitem
        addActionListener(self)
        twin.addChangeListener(self)
        setEnabled(twin.isEnabled())
        accelerator = twin.getAccelerator()
        if accelerator != None:
            setShortcut(createShortcut(accelerator))

    #  Method: actionPerformed(e) 
    # 
    #  * Responds to an action event in the Mac menu and forwards it along to
    #  * the actual <code>JMenuItem</code> that the client has created.
    #  
    def actionPerformed(self, e):
        """ generated source for method actionPerformed """
        if e != e:
            #  Avoid the unused parameter warning 
        twin.doClick(0)

    #  Method: stateChanged(e) 
    # 
    #  * Monitors the state of the <code>JMenuItem</code> and replicates changes
    #  * in the enabled state.
    #  
    def stateChanged(self, e):
        """ generated source for method stateChanged """
        setEnabled(twin.isEnabled())

    #  Private method: createShortcut(accelerator) 
    # 
    #  * Creates an old-style menu shortcut from the new-style accelerator.
    #  
    def createShortcut(self, accelerator):
        """ generated source for method createShortcut """
        isShifted = (accelerator.getModifiers() & Event.SHIFT_MASK) != 0
        return MenuShortcut(accelerator.getKeyCode(), isShifted)

    #  Private instance variables 
    twin = None

#  Package class: OldStyleCheckBoxMenuItem 
# 
#  * This class represents a standard Macintosh <code>CheckBoxMenuItem</code> that
#  * listens to a <code>JCheckBoxMenuItem</code> and tracks its changes.
#  
class OldStyleCheckBoxMenuItem(CheckboxMenuItem, ActionListener, ChangeListener):
    """ generated source for class OldStyleCheckBoxMenuItem """
    #  Constructor: OldStyleCheckBoxMenuItem(jitem) 
    # 
    #  * Creates a new <code>CheckBoxMenuItem</code> that tracks the changes in the specified
    #  * <code>JCheckBoxMenuItem</code>.
    #  
    def __init__(self, jitem):
        """ generated source for method __init__ """
        super(OldStyleCheckBoxMenuItem, self).__init__(jitem.getText())
        twin = jitem
        addActionListener(self)
        twin.addChangeListener(self)
        setState(twin.getState())
        setEnabled(twin.isEnabled())
        accelerator = twin.getAccelerator()
        if accelerator != None:
            setShortcut(createShortcut(accelerator))

    #  Method: actionPerformed(e) 
    # 
    #  * Responds to an action event in the Mac menu and forwards it along to
    #  * the actual <code>JMenuItem</code> that the client has created.
    #  
    def actionPerformed(self, e):
        """ generated source for method actionPerformed """
        if e != e:
            #  Avoid the unused parameter warning 
        twin.doClick(0)

    #  Method: stateChanged(e) 
    # 
    #  * Monitors the state of the <code>JMenuItem</code> and replicates changes
    #  * in the enabled state.
    #  
    def stateChanged(self, e):
        """ generated source for method stateChanged """
        setState(twin.getState())
        setEnabled(twin.isEnabled())

    #  Private method: createShortcut(accelerator) 
    # 
    #  * Creates an old-style menu shortcut from the new-style accelerator.
    #  
    def createShortcut(self, accelerator):
        """ generated source for method createShortcut """
        isShifted = (accelerator.getModifiers() & Event.SHIFT_MASK) != 0
        return MenuShortcut(accelerator.getKeyCode(), isShifted)

    #  Private instance variables 
    twin = None

