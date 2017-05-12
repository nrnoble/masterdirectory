# Classes that require special handling during the serialization and
 # deserialization process must implement special methods with these exact
 # signatures:
 #
 # <PRE>
 # private void writeObject(java.io.ObjectOutputStream out)
 #     throws IOException
 # private void readObject(java.io.ObjectInputStream in)
 #     throws IOException, ClassNotFoundException;
 # private void readObjectNoData()
 #     throws ObjectStreamException;
 # </PRE>
 #
 # <p>The writeObject method is responsible for writing the state of the
 # object for its particular class so that the corresponding
 # readObject method can restore it.  The default mechanism for saving
 # the Object's fields can be invoked by calling
 # out.defaultWriteObject. The method does not need to concern
 # itself with the state belonging to its superclasses or subclasses.
 # State is saved by writing the individual fields to the
 # ObjectOutputStream using the writeObject method or by using the
 # methods for primitive data types supported by DataOutput.
 #
 # <p>The readObject method is responsible for reading from the stream and
 # restoring the classes fields. It may call in.defaultReadObject to invoke
 # the default mechanism for restoring the object's non-static and
 # non-transient fields.  The defaultReadObject method uses information in
 # the stream to assign the fields of the object saved in the stream with the
 # correspondingly named fields in the current object.  This handles the case
 # when the class has evolved to add new fields. The method does not need to
 # concern itself with the state belonging to its superclasses or subclasses.
 # State is saved by writing the individual fields to the
 # ObjectOutputStream using the writeObject method or by using the
 # methods for primitive data types supported by DataOutput.
 #
 # <p>The readObjectNoData method is responsible for initializing the state of
 # the object for its particular class in the event that the serialization
 # stream does not list the given class as a superclass of the object being
 # deserialized.  This may occur in cases where the receiving party uses a
 # different version of the deserialized instance's class than the sending
 # party, and the receiver's version extends classes that are not extended by
 # the sender's version.  This may also occur if the serialization stream has
 # been tampered; hence, readObjectNoData is useful for initializing
 # deserialized objects properly despite a "hostile" or incomplete source
 # stream.
 #
 # <p>Serializable classes that need to designate an alternative object to be
 # used when writing an object to the stream should implement this
 # special method with the exact signature:
 #
 # <PRE>
 # ANY-ACCESS-MODIFIER Object writeReplace() throws ObjectStreamException;
 # </PRE><p>
 #
 # This writeReplace method is invoked by serialization if the method
 # exists and it would be accessible from a method defined within the
 # class of the object being serialized. Thus, the method can have private,
 # protected and package-private access. Subclass access to this method
 # follows java accessibility rules. <p>
 #
 # Classes that need to designate a replacement when an instance of it
 # is read from the stream should implement this special method with the
 # exact signature.
 #
 # <PRE>
 # ANY-ACCESS-MODIFIER Object readResolve() throws ObjectStreamException;
 # </PRE><p>
 #
 # This readResolve method follows the same invocation rules and
 # accessibility rules as writeReplace.<p>
 #
 # The serialization runtime associates with each serializable class a version
 # number, called a serialVersionUID, which is used during deserialization to
 # verify that the sender and receiver of a serialized object have loaded
 # classes for that object that are compatible with respect to serialization.
 # If the receiver has loaded a class for the object that has a different
 # serialVersionUID than that of the corresponding sender's class, then
 # deserialization will result in an {@link InvalidClassException}.  A
 # serializable class can declare its own serialVersionUID explicitly by
 # declaring a field named <code>"serialVersionUID"</code> that must be static,
 # final, and of type <code>long</code>:
 #
 # <PRE>
 # ANY-ACCESS-MODIFIER static final long serialVersionUID = 42L;
 # </PRE>
 #
 # If a serializable class does not explicitly declare a serialVersionUID, then
 # the serialization runtime will calculate a default serialVersionUID value
 # for that class based on various aspects of the class, as described in the
 # Java(TM) Object Serialization Specification.  However, it is <em>strongly
 # recommended</em> that all serializable classes explicitly declare
 # serialVersionUID values, since the default serialVersionUID computation is
 # highly sensitive to class details that may vary depending on compiler
 # implementations, and can thus result in unexpected
 # <code>InvalidClassException</code>s during deserialization.  Therefore, to
 # guarantee a consistent serialVersionUID value across different java compiler
 # implementations, a serializable class must declare an explicit
 # serialVersionUID value.  It is also strongly advised that explicit
 # serialVersionUID declarations use the <code>private</code> modifier where
 # possible, since such declarations apply only to the immediately declaring
 # class--serialVersionUID fields are not useful as inherited members. Array
 # classes cannot declare an explicit serialVersionUID, so they always have
 # the default computed value, but the requirement for matching
 # serialVersionUID values is waived for array classes.
 #
 # @author  unascribed
 # @see java.io.ObjectOutputStream
 # @see java.io.ObjectInputStream
 # @see java.io.ObjectOutput
 # @see java.io.ObjectInput
 # @see java.io.Externalizable
 # @since   JDK1.1
 #/
class Serializable():
    pass



 #
 # An iterator over a collection.  {@code Iterator} takes the place of
 # {@link Enumeration} in the Java Collections Framework.  Iterators
 # differ from enumerations in two ways:
 #
 # <ul>
 #      <li> Iterators allow the caller to remove elements from the
 #           underlying collection during the iteration with well-defined
 #           semantics.
 #      <li> Method names have been improved.
 # </ul>
 #
 # <p>This interface is a member of the
 # <a href="{@docRoot}/../technotes/guides/collections/index.html">
 # Java Collections Framework</a>.
 #
 # @param <E> the type of elements returned by this iterator
 #
 # @author  Josh Bloch
 # @see Collection
 # @see ListIterator
 # @see Iterable
 # @since 1.2
 #/
class Iterator():
     #
     # Returns {@code true} if the iteration has more elements.
     # (In other words, returns {@code true} if {@link #next} would
     # return an element rather than throwing an exception.)
     #
     # @return {@code true} if the iteration has more elements
     #/
    def hasNext(self):
        pass
    #
    # Returns the next element in the iteration.
    #
    # @return the next element in the iteration
    # @throws NoSuchElementException if the iteration has no more elements
    #/
    def next(self):
        pass
        #
    # Removes from the underlying collection the last element returned
    # by this iterator (optional operation).  This method can be called
    # only once per call to {@link #next}.  The behavior of an iterator
    # is unspecified if the underlying collection is modified while the
    # iteration is in progress in any way other than by calling this
    # method.
    #
    # @implSpec
    # The default implementation throws an instance of
    # {@link UnsupportedOperationException} and performs no other action.
    #
    # @throws UnsupportedOperationException if the {@code remove}
    #         operation is not supported by this iterator
    #
    # @throws IllegalStateException if the {@code next} method has not
    #         yet been called, or the {@code remove} method has already
    #         been called after the last call to the {@code next}
    #         method
    #
    def remove(self):
        # throw new UnsupportedOperationException("remove");
        pass

    #
    # Performs the given action for each remaining element until all elements
    # have been processed or the action throws an exception.  Actions are
    # performed in the order of iteration, if that order is specified.
    # Exceptions thrown by the action are relayed to the caller.
    #
    # @implSpec
    # <p>The default implementation behaves as if:
    # <pre>{@code
    #     while (hasNext())
    #         action.accept(next());
    # }</pre>
    #
    # @param action The action to be performed for each element
    # @throws NullPointerException if the specified action is null
    # @since 1.8
    #
    # def forEachRemaining(Consumer<? super E> action):
    def forEachRemaining(self):
        # Objects.requireNonNull(action)
        # while (hasNext())
        #  action.accept(next())
        pass

