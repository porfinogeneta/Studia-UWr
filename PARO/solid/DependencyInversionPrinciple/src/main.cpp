#include "Address.hpp"
#include "EventLog.hpp"
#include "SqlStorage.hpp"

int main()
{
    SqlStorage sqlStorage(Address{"sql://127.0.0.1:61123/"})
    EventLog log(sqlStorage);
    log.log("Application started");

    // ...
    log.log("Performed some operation");

    // ...
    log.log("Some event occurred");

    // ...
    log.log("Application terminates");
}
