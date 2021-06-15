// https://leetcode.com/problems/print-foobar-alternately/

// Suppose you are given the following code:

// The same instance of FooBar will be passed to two different threads. Thread A
// will call foo() while thread B will call bar(). Modify the given program to
// output "foobar" n times.

////////////////////////////////////////////////////////////////////////////////

#include <semaphore.h>
class FooBar {
private:
    int n;
    sem_t s1, s2;

public:
    FooBar(int n) {
        this->n = n;
        sem_init(&s1, 0, 0);
        sem_init(&s2, 0, 1);
    }

    void foo(function<void()> printFoo) {
        for (int i = 0; i < n; i++) {
            sem_wait(&s2);
            // printFoo() outputs "foo". Do not change or remove this line.
            printFoo();
            sem_post(&s1);
        }
    }

    void bar(function<void()> printBar) {
        for (int i = 0; i < n; i++) {
            sem_wait(&s1);
            // printBar() outputs "bar". Do not change or remove this line.
            printBar();
            sem_post(&s2);
        }
    }
};
