#include <iostream>
#include <memory>

#include "Greeter.hpp"
#include "LazyUpdater.h"

int main(){
    auto updater = std::make_unique<LazyUpdater>();

    Greeter greeter(std::move(updater));
    greeter.greet();
}
