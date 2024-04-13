package app.actions

import app.plugins._





object Actions {

    abstract class Pluginable extends Reverting with LowerCasing with SingleSpacing with NoSpacing with DuplicateRemoval
        with Rotating with Doubling with Shortening

    class PluginableA extends Pluginable {
        def plugin(s: String) =
            shortening(doubling(singleSpacing(s)))
    }

    class PluginableB extends Pluginable {
        def plugin(s: String) =
            doubling(noSpacing(shortening(s)))
    }

    class PluginableC extends Pluginable {
        def plugin(s: String) =
            lowerCasing(doubling(s))
    }

    class PluginableD extends Pluginable {
        def plugin(s: String) =
            rotating(duplicateRemoval(s))
    }

    class PluginableE extends Pluginable {
        def plugin(s: String) =
            reverting(doubling(shortening(noSpacing(s))))
    }

    class PluginableF extends Pluginable {
        def plugin(s: String) =
            (1 to 5).foldLeft(s)((str, _) => reverting(str))
    }

    class PluginableG extends Pluginable {
        def plugin(s: String) =
            actionB.plugin(actionA.plugin(s))
    }



    val actionA: Pluginable = 
        new PluginableA

    val actionB: Pluginable =
        new PluginableB

    val actionC: Pluginable =
        new PluginableC

    val actionD: Pluginable =
        new PluginableD

    val actionE: Pluginable =
        new PluginableE

    val actionF: Pluginable =
        new PluginableF

    val actionG: Pluginable =
        new PluginableG
}