cmake_minimum_required(VERSION 3.10)
project(leafGen)

set(CMAKE_CXX_STANDARD 17)

set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} -m64 -march=native -fopt-info-vec-optimized -O3" )


add_executable(leafGen
        include/fast_marching_method.hpp
        include/jpge.cpp
        include/jpge.h
        src/main.cpp
        src/Obj/Parser.cpp
        src/Obj/Parser.hh
        src/Obj/Object.cpp
        src/Obj/Object.hh
        src/Obj/Point3D.cpp
        src/Obj/Point3D.hh
        src/Obj/Material.cpp
        src/Obj/Material.hh
        src/Obj/Point2D.cpp
        src/Obj/Point2D.hh
        src/Obj/Vector3D.cpp
        src/Obj/Vector3D.hh
        src/Obj/Texture2D.cpp
        src/Obj/Texture2D.hh
        src/Obj/PointEl.cpp
        src/Obj/PointEl.hh
        src/Obj/FaceEl.cpp
        src/Obj/FaceEl.hh
        src/Obj/LineEl.cpp
        src/Obj/LineEl.hh
        src/Obj/Scene.cpp
        src/Obj/Scene.hh
        src/Obj/Element.cpp
        src/Obj/Element.hh
        src/Utils/Strutils.cpp
        src/Utils/Strutils.hh
        src/Tree/Node.cpp
        src/Tree/Node.hh
        src/Obj/Generator.cpp
        src/Obj/Generator.hh
        src/L-Systems/LNode.cpp
        src/L-Systems/LNode.hh
        src/L-Systems/LObject.cpp
        src/L-Systems/LObject.hh
        src/L-Systems/LRuleBasic.hh
        src/L-Systems/LTranslator.cpp
        src/L-Systems/LTranslator.hh
        src/L-Systems/TurtleTranslator.hh
        src/L-Systems/TurtleTranslator.hxx
        src/L-Systems/LRuleBasic.cpp
        src/L-Systems/Turtle.cpp
        src/L-Systems/Turtle.hh
        src/L-Systems/LRuleStoch.cpp
        src/L-Systems/LRuleStoch.hh
        src/L-Systems/LRule.cpp
        src/L-Systems/LRule.hh
        src/L-Systems/LRuleContext.cpp
        src/L-Systems/LRuleContext.hh
        src/L-Systems/LRuleParametric.cpp
        src/L-Systems/LRuleParametric.hh
        src/L-Systems/Condition.cpp
        src/L-Systems/Condition.hh
        src/L-Systems/Environment.cpp
        src/L-Systems/Environment.hh
        src/L-Systems/LVar.cpp
        src/L-Systems/LVar.hh
        src/L-Systems/LNodeFunc.cpp
        src/L-Systems/LNodeFunc.hh
        src/Obj/Meshes/Cylinder.cpp
        src/Obj/Meshes/Cylinder.hh
        src/Tree/TreeTranslator.cpp
        src/Tree/TreeTranslator.hh
        src/Obj/Meshes/Linker.cpp
        src/Obj/Meshes/Linker.hh
        src/Obj/Meshes/Triangle.cpp
        src/Obj/Meshes/Triangle.hh
        src/Utils/Color.cpp
        src/Utils/Color.hh
        src/Utils/Chronometer.cpp
        src/Utils/Chronometer.hh
        src/Utils/dblutils.cpp
        src/Utils/dblutils.hh
        src/Texturing/TextureGenerator.cpp
        src/Texturing/TextureGenerator.hh
        src/Texturing/Texture.cpp
        src/Texturing/Texture.hh
        src/Texturing/Rasterize/Draw.cpp
        src/Texturing/Rasterize/Draw.hh
        src/Texturing/Rasterize/Edge.cpp
        src/Texturing/Rasterize/Edge.hh
        src/Texturing/Rasterize/Span.cpp
        src/Texturing/Rasterize/Span.hh
        src/Texturing/Rasterize/RasterPoint.cpp
        src/Texturing/Rasterize/RasterPoint.hh
        src/Texturing/Morphology/Morphology.cpp
        src/Texturing/Morphology/Morphology.hh
        src/AlgoLeaf_Particle/gen_random.cpp
        src/AlgoLeaf_Particle/gen_random.hh
        src/AlgoLeaf_Particle/leaf_object.cpp
        src/AlgoLeaf_Particle/leaf_object.hh
        src/AlgoLeaf_Particle/math_stuff.cpp
        src/AlgoLeaf_Particle/math_stuff.hh
        src/AlgoLeaf_Particle/particle_object.cpp
        src/AlgoLeaf_Particle/particle_object.hh
        src/AlgoLeaf_Particle/Growth/leafGrowth.cpp
        src/AlgoLeaf_Particle/Growth/leafGrowth.hh
        src/AlgoLeaf_Particle/Equations/Parametric.cpp
        src/AlgoLeaf_Particle/Equations/Parametric.hh
        src/AlgoLeaf_Particle/Equations/Polar.cpp
        src/AlgoLeaf_Particle/Equations/Polar.hh
        src/AlgoLeaf_Auxin/Leaf.cpp
        src/AlgoLeaf_Auxin/Leaf.hh
        src/AlgoLeaf_Auxin/Leafshape.cpp
        src/AlgoLeaf_Auxin/Leafshape.hh
        src/AlgoLeaf_Auxin/mathStuff.cpp
        src/AlgoLeaf_Auxin/mathStuff.hh
        src/AlgoLeaf_Auxin/Nodes.cpp
        src/AlgoLeaf_Auxin/Nodes.hh
        src/Examples.cpp
        src/Examples.hh
        src/LeafWriter.cpp src/LeafWriter.hh)
