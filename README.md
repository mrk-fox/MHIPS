
<img src="https://github.com/mrk-fox/MHIPS/blob/main/pictures/MHIPS%20Zine.png" style="width:auto;">

<h1 align="center">MHIPS</h1>
<div align="center">Modular Human Interface Panels System</div>
<br> <br>
# Introduction
As controlling any type of craft with electronical components reqiring human intervention to function grows with the complexity of the craft and its tasks, I have decided to design a controlling system which is modular and uses near-aerospace-safety protocolls.


**Please pay attention to the fact that this project is still being developed. There is no "final solution" or such similar.**

## Functionality and goals

Every sucesfull project resembles a solution for a problem. Thus, the problem needs to be formulated before a solution is deigned. The problem that this project solves is the complexity of digital menus and the lack of haptic response in controlling anything with pure software.
My solution is a _modular, standartized panel system_ 
Hence, a ruleset was reqired to ensure the mulitcompatiability and extensiabiliy of this project.

# Standartization

In this section we define a convention for the MHIPS (Modular Human Interface Panel System).
``` 
1. The abbreviation "MHIPS" stands for "Modular Human Interface Panel System".
      a. A panel is defined as a mounted and rigid resembly of multiple tiles, solving a user-defined task.
      b. A tile is defined as the smallest unit of the system. Any tile consists of the following components:
           b.1. A CAN-Capable read-write PCB as the BusPlate.
           b.2. A casing consisting of the front case and the backplate
           b.3. Input and output elements as Light Emitting Diodes, Buttons, Switches and more mounted into the front plate                  of the casing
      c. A rack is defined as the structure carrying and spacing the tiles.
2. The basic structure for a rack is a 5mm wide frame with the inner sizing of 50x50mm and a thickness of minimum 4mm. By fusing such frames togoether a rack is built. 
``` 
