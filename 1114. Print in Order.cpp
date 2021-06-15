// https://leetcode.com/problems/print-in-order/

// Suppose we have a class:

// The same instance of Foo will be passed to three different threads. Thread A
// will call first(), thread B will call second(), and thread C will call third().
// Design a mechanism and modify the program to ensure that second() is executed
// after first(), and third() is executed after second().

// Note:

// We do not know how the threads will be scheduled in the operating system, even
// though the numbers in the input seem to imply the ordering. The input format you
// see is mainly to ensure our tests' comprehensiveness.

////////////////////////////////////////////////////////////////////////////////

#include <future>
class Foo {
private:
    std::promise<void> p1;
    std::promise<void> p2;
    
public:
    Foo() {}

    void first(function<void()> printFirst) {
        // printFirst() outputs "first". Do not change or remove this line.
        printFirst();
        p1.set_value();
    }

    void second(function<void()> printSecond) {
        p1.get_future().wait();
        // printSecond() outputs "second". Do not change or remove this line.
        printSecond();
        p2.set_value();
    }

    void third(function<void()> printThird) {
        p2.get_future().wait();
        // printThird() outputs "third". Do not change or remove this line.
        printThird();
    }
};
