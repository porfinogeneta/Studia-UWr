#include <memory>

#include "Console.hpp"
#include "Handlers.hpp"

int main()
{
    Console console;

    console.addHandler(std::make_unique<Quitter>());
    console.addHandler(std::make_unique<Printer>());
    console.addHandler(std::make_unique<HelloWorld>());

    console.run();
    return 0;
}
